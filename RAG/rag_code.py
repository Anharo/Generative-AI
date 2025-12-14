import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings

from sklearn.metrics.pairwise import cosine_similarity

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def load_document(path):
    loader = TextLoader(path, encoding="utf-8")
    documents = loader.load()

    splitter = CharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)
    print(f"Loaded and split into {len(chunks)} chunks.")
    return chunks

def embed_chunks(chunks):
    embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectors = embedding_model.embed_documents([c.page_content for c in chunks])
    return embedding_model, vectors

def get_best_chunk(query, embedding_model, chunk_vectors, chunks):
    query_vec = embedding_model.embed_query(query)
    scores = cosine_similarity([query_vec], chunk_vectors)[0]

    best_index = scores.argmax()
    best_score = scores[best_index]

    return chunks[best_index].page_content, best_score

def make_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3
    )

def generate_answer(llm, context, question):
    prompt = f"""
You are a helpful assistant. Use ONLY the context below to answer. If answer is not in context, say "Not found in document."

Context:
{context}

Question: {question}

Answer:
"""
    response = llm.invoke(prompt)
    return response.content

def rag_chatbot():
    PATH = "football_corpus.txt"

    print("Loading document...")
    chunks = load_document(PATH)

    print("Embedding chunks...")
    embedding_model, vectors = embed_chunks(chunks)

    llm = make_llm()

    print("\nRAG chatbot ready! Ask anything. Type 'exit' to quit.\n")

    while True:
        question = input("You: ")

        if question.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        best_chunk, score = get_best_chunk(question, embedding_model, vectors, chunks)

        print(f"\n[Matched chunk similarity score: {score:.4f}]\n")

        answer = generate_answer(llm, best_chunk, question)

        print("Assistant:", answer)
        print("-" * 60)

rag_chatbot()