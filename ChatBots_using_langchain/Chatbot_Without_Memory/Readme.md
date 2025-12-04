# 🤖 Gemini Chatbot (LangChain | No Memory)

A simple **terminal-based chatbot** built using **LangChain** and **Google Gemini Free API**.  
This chatbot does **not maintain conversation memory**, meaning each user query is processed independently.

---

## 🚀 Features

- ✅ Uses **Google Gemini FREE API**
- ✅ Built with **LangChain**
- ✅ **No memory** (stateless chatbot)
- ✅ Simple terminal-based interaction
- ✅ Beginner-friendly code structure
- ✅ Easy to extend (memory, UI, API)

---

## 🛠️ Technologies Used

- Python 3.9+
- LangChain
- Google Gemini (`gemini-1.0-pro`)
- `python-dotenv` for environment variables

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/gemini-langchain-chatbot.git
cd gemini-langchain-chatbot
```
### 2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```
### 3️⃣ Install dependencies
```bash
pip install langchain langchain-google-genai google-generativeai python-dotenv
```
### 🔑 Setup Google Gemini API Key

Go to Google AI Studio
Generate a free API key
Create a .env file in the project root:
```bash
GOOGLE_API_KEY=your_api_key_here
```
⚠️ Never commit your .env file to GitHub.

### ▶️ Run the Chatbot
```bash
python chatbot.py
```
