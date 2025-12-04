import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API Key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7
)

# Prompt Template (No memory)
prompt = PromptTemplate(
    input_variables=["user_input"],
    template="You are bestfriend of the user and you need to talk like a real funny friend to him.\nUser: {user_input}\nGF:"
)

def chatbot():
    print("🤖 Gemini BestFriend Chatbot (No Memory) | Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        
        response = llm.invoke(
            prompt.format(user_input=user_input)
        )
        
        print(f"Bot: {response.content}\n")

if __name__ == "__main__":
    chatbot()
