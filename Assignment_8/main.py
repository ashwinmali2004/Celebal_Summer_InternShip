"""
RAG Q&A chatbot using document retrieval and generative AI for intelligent response generation (can use any light model from hugging face or a license llm(opneai, claude, grok, gemini) if free credits available
""" 


import os
import warnings
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

USE_GEMINI = True
GEMINI_API_KEY = "WRITE_YOUR_API_KEY"  
CSV_PATH = 'Training Dataset.csv'

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
warnings.filterwarnings("ignore")


print("Loading and processing dataset...")
df = pd.read_csv(CSV_PATH)

for col in df.columns:
    if df[col].dtype == 'O':
        df[col] = df[col].fillna("NA")
    else:
        df[col] = df[col].fillna(-1)

documents = df.apply(lambda row: " | ".join([f"{col}: {val}" for col, val in row.items()]), axis=1).tolist()


print("Embedding documents...")
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embed_model.encode(documents, show_progress_bar=False)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def retrieve(query, k=3):
    query_vec = embed_model.encode([query])
    D, I = index.search(np.array(query_vec), k)
    return [documents[i] for i in I[0]]

if USE_GEMINI:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    def generate_answer(context, query):
        prompt = f"""Answer the following question based on the provided loan dataset context:

Context:
{context}

Question:
{query}
"""
        response = model.generate_content(prompt)
        return response.text.strip()
else:
    print(" Gemini not enabled. Please set USE_GEMINI = True and add your key.")
    exit(1)


def chatbot(query):
    context_docs = retrieve(query)
    context = "\n".join(context_docs)
    answer = generate_answer(context, query)
    return answer


if __name__ == "__main__":
    print("RAG Chatbot with Gemini is ready! Type 'exit' to quit.")
    while True:
        user_input = input("\n? You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = chatbot(user_input)
        print("ChatBot:", response)
