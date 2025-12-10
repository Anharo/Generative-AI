import os
import warnings
from dotenv import load_dotenv

warnings.filterwarnings("ignore")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# ALL MEMORY TYPES
from langchain.memory import (
    ConversationBufferMemory,          # 1️⃣ Basic memory – stores entire chat
    ConversationBufferWindowMemory,    # 2️⃣ Window memory – last N messages
    ConversationSummaryMemory,         # 3️⃣ Summary memory – ❌ not stable with Gemini
    ConversationSummaryBufferMemory    # 4️⃣ Summary+buffer – ❌ not stable with Gemini
)

from langchain.chains import LLMChain

# Load API Key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not found. Add it to your .env file.")

# Choose best free model for your account
MODEL_NAME = "gemini-2.0-flash-lite"

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7
)

#  MEMORY OPTIONS (Only ONE active)
# 1. BEST MEMORY → Works perfectly with Gemini
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# 2. WINDOW MEMORY (Keeps only last 5 messages)
# memory = ConversationBufferWindowMemory(
#     k=5,
#     memory_key="chat_history",
#     return_messages=True
# )

# 3. SUMMARY MEMORY (Summarizes chat — ❌ NOT recommended for Gemini)
# memory = ConversationSummaryMemory(
#     llm=llm,
#     memory_key="chat_history"
# )

# 4. SUMMARY + BUFFER MEMORY (❌ Not stable with Gemini)
# memory = ConversationSummaryBufferMemory(
#     llm=llm,
#     memory_key="chat_history",
#     max_token_limit=300
# )

# PROMPT WITH MEMORY
prompt = PromptTemplate(
    input_variables=["chat_history", "user_input"],
    template=(
        "You are the user's funny best friend. Talk casually, jokingly, and like a real human friend.\n\n"
        "Chat History:\n{chat_history}\n"
        "User: {user_input}\n"
        "BestFriend:"
    )
)

# CHAIN
chat_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

# CHAT LOOP
def chatbot():
    print(f"🤖 Gemini BestFriend Chatbot WITH MEMORY ({MODEL_NAME}) | Type 'exit' to quit\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ("exit", "quit"):
            print("👋 Goodbye bro!")
            break

        if user_input == "":
            continue

        try:
            response = chat_chain.invoke({"user_input": user_input})
            print("Bot:", response["text"])

        except Exception as e:
            print("Bot: Bro something went wrong 💀 (likely quota exceeded)")
            print("Error:", e)

if __name__ == "__main__":
    chatbot()
