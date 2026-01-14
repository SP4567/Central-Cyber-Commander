import os
from rag.embedder import Embedder
from rag.vector_store import VectorStore

THREAT_FEED_PATH = "data/threat_feed"

def build_vector_db():
    embedder = Embedder("sentence-transformers/all-MiniLM-L6-v2")
    store = VectorStore(dim=384)

    for file in os.listdir(THREAT_FEED_PATH):
        path = os.path.join(THREAT_FEED_PATH, file)
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    vec = embedder.embed(line)
                    store.add(vec, line.strip())

    print("[+] Vector DB built with threat intelligence")
    return store
