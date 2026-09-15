import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")


def create_embedding(text_list):
    # Ollama embedding
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "bge-m3",
            "input": text_list
        }
    )

    embedding = r.json()["embeddings"]
    return embedding


# Load embeddings
df = joblib.load('RAG PROJECT/embeddings.joblib')


# Get user question
incoming_query = input("Ask a Question: ")

question_embedding = create_embedding([incoming_query])[0]


# Calculate similarity
similarities = cosine_similarity(
    np.vstack(df['embedding']),
    [question_embedding]
).flatten()


# Get top 5 results
top_results = 5
max_indx = similarities.argsort()[::-1][0:top_results]

new_df = df.loc[max_indx]


# Create RAG prompt
prompt = f'''I am teaching DSA in 90 Days for Placements course. Here are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:

{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}
---------------------------------
"{incoming_query}"

User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course
'''


with open("prompt.txt", "w", encoding="utf-8") as f:
    f.write(prompt)


# OpenRouter API call
response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "openrouter/free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        # "reasoning": {
        #     "enabled": True
        # }
    }
)


# Check for API errors
response.raise_for_status()

result = response.json()

# Get AI answer
answer = result["choices"][0]["message"]["content"]

print(answer)


# Save response
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(answer)