## 🤖 Gemini Chatbot (LangChain + Memory)

A powerful terminal-based chatbot built using LangChain and Google Gemini API, now upgraded with conversation memory so the bot remembers previous messages and chats like a real best friend!
This version includes all types of LangChain memory, with only the best memory (ConversationBufferMemory) enabled.
Other memory types are included but commented out with explanations.
---
##  🚀 Features
- ✔️ Uses Google Gemini Free API
- ✔️ Built with LangChain
- ✔️ Conversation Memory Enabled
- ✔️ Multiple memory options included (buffer, summary, window, etc.)
- ✔️ Simple and beginner-friendly
- ✔️ Perfect for making a fun “best-friend” chatbot
---
## 🧠 Memory Options Included
Active memory (best for Gemini):
- ConversationBufferMemory → Stores complete chat history reliably
 (works best with Gemini models, no API conflicts)
Additional memory types (commented out):
- ConversationSummaryMemory → Summarizes older messages
- ConversationBufferWindowMemory → Only remembers the last k messages
- ConversationSummaryBufferMemory → Hybrid memory (⚠️ not fully compatible with Gemini)

All are included in the code so you can switch anytime.

--- 
## 🛠️ Technologies Used 
- Python 3.9+
- LangChain 
- Google Gemini (gemini-1.0-pro)
- python-dotenv for environment variables

---
