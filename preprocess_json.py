import requests
import os
import json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib


def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={"model": "all-minilm", "input": text_list},
    )
    # print(r.json())
    embedding = r.json()["embeddings"]
    return embedding

jsons = os.listdir("new_jsons")  # List all the jsons
# print(jsons)
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(f"new_jsons/{json_file}") as f:
        content = json.load(f)
    print(f"Creating Embeddings for {json_file}")
    embeddings = create_embedding([c["text"] for c in content["chunks"]])
    # 👉 Extracts all chunk texts from the JSONS File and sends them together to the embedding model to get one embedding per chunk.
    for i, chunk in enumerate(content["chunks"]):
        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)

df = pd.DataFrame.from_records(my_dicts)
df.to_excel("output1.xlsx", index=True)
# Save this dataframe
joblib.dump(df, 'embeddings.joblib')


