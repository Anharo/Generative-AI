import os
import pandas as pd
import json
from dotenv import load_dotenv
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnablePassthrough

# 1. Configuration and Data Setup
def initialize_environment():
    load_dotenv()
    return ChatGoogleGenerativeAI(
    model="models/gemini-3-flash-preview", 
    max_retries=6,  
    temperature=0
    )

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    column_mapping = {
        "artist_name": "track_artist",
        "genre": "playlist_genre"
    }
    df = df.rename(columns=column_mapping)
    cols = ["track_name", "track_artist", "playlist_genre", "danceability", "energy", "valence", "tempo", "popularity"]
    
    existing_cols = [c for c in cols if c in df.columns]
    df = df[existing_cols].dropna()
    
    features = ["danceability", "energy", "valence", "tempo", "popularity"]
    scaler = MinMaxScaler()
    df[features] = scaler.fit_transform(df[features])
    
    return df

# 2. Mood Analysis Logic 
def get_mood_analyzer_chain(llm):
    prompt = ChatPromptTemplate.from_template(
        """Analyze the user's mood from this text: "{user_text}"
        
        Return ONLY a JSON object with:
        - mood (happy, sad, calm, energetic, romantic)
        - energy (low, medium, high)
        - preferred_genre
        """
    )
    chain = prompt | llm | JsonOutputParser()
    return chain

# 3. Filtering and Recommendation Logic
def map_mood_to_filters(mood_data):
    mood = mood_data.get("mood", "calm")
    
    mood_map = {
        "sad": ["acoustic", "indie", "soul"],
        "happy": ["pop", "dance", "latin"],
        "calm": ["chill", "ambient", "classical"],
        "energetic": ["edm", "rock", "rap"],
        "romantic": ["r&b", "pop"]
    }
    
    return mood_map.get(mood, ["pop"])

def get_recommendations(df, user_text, mood_chain, top_n=5):
    mood_data = mood_chain.invoke({"user_text": user_text})
    genres = map_mood_to_filters(mood_data)
    filtered = df[df["playlist_genre"].str.lower().isin([g.lower() for g in genres])]
    
    if filtered.empty:
        filtered = df 

    features = ["danceability", "energy", "valence", "tempo", "popularity"]
    similarity = cosine_similarity(filtered[features])
    scores = similarity.mean(axis=0)
    top_indices = scores.argsort()[-top_n:][::-1]

    return filtered.iloc[top_indices][["track_name", "track_artist"]]

# 4. Main Execution
def main():
    llm = initialize_environment()
    df = load_and_preprocess_data("SpotifyFeatures.csv")
    mood_chain = get_mood_analyzer_chain(llm)
    
    user_input = input("Describe your current mood or situation for song recommendations: ")
    print(f"--- Analyzing mood for: '{user_input}' ---")
    
    recs = get_recommendations(df, user_input, mood_chain)
    
    print("\n🎧 Recommended Songs:")
    print(recs.to_string(index=False))

if __name__ == "__main__":
    main()