# 🎵 Mood-Based Spotify Recommender

An AI-powered music recommendation engine that uses **Google Gemini** and **LangChain (LCEL)** to analyze user sentiment and suggest songs from a Spotify dataset using mathematical similarity.

---

## 🚀 Overview
This project bridges the gap between how we feel and what we listen to. Instead of manually searching for a playlist, users describe their mood in plain English. 

The system follows a three-step pipeline:
1.  **Mood Extraction:** Uses Gemini 1.5 Flash to transform unstructured text into structured JSON data (mood, energy level, and target genres).
2.  **Data Filtering:** Narrow down the Spotify dataset (232k+ tracks) to genres that match the detected mood.
3.  **Vector Similarity:** Uses `cosine_similarity` on audio features (danceability, energy, valence, tempo) to find the top-ranked tracks.



---

## 🛠️ Tech Stack
* **LLM:** Google Gemini 1.5 Flash
* **Orchestration:** LangChain (LCEL - LangChain Expression Language)
* **Data Science:** Pandas, Scikit-Learn
* **Environment:** Python 3.10+

---

## 🔧 Installation & Setup

### 1. Clone the Project
```bash
git clone https://github.com/Anharo/Generative-AI.git
cd Generative-AI\Song Recommendation Using AI + Custom DS
```
### 2. Set Up Virtual Environment
```bash
python -m venv .venv
# Activate on Windows:
.venv\Scripts\activate
# Activate on Mac/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install pandas langchain-google-genai scikit-learn python-dotenv
```

### 4. Configure API Keys
- Create a .env file in the root directory and add your Google AI API Key:
```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 📊 Dataset Structure

The system is designed to work with the **Spotify Features** dataset. To ensure the recommendation engine works correctly, the `SpotifyFeatures.csv` file should contain the following structure:

### 1. Metadata Columns
* **track_name**: The title of the song (used for final display).
* **artist_name** / **track_artist**: The name of the artist or band.
* **genre**: The primary musical category used for initial filtering based on mood.

### 2. Numerical Audio Features
These features are used for the **Cosine Similarity** calculation. They are normalized to a 0.0 - 1.0 scale during preprocessing.
* **danceability**: How suitable a track is for dancing based on tempo, rhythm stability, and beat strength.
* **energy**: A perceptual measure of intensity and activity.
* **valence**: A measure from 0.0 to 1.0 describing the musical positiveness (high valence = happy/cheerful).
* **tempo**: The overall estimated beats per minute (BPM).
* **popularity**: The calculated popularity of the track based on play counts.

---

### 🛠️ Data Processing Pipeline
The code includes a preprocessing function that automatically handles column renaming (e.g., converting `artist_name` to `track_artist`) and applies `MinMaxScaler` to ensure that features like `tempo` (usually 60-200) do not statistically overwhelm features like `energy` (0-1).
