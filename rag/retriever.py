class Retriever:
    def __init__(self, embedder, store):
        self.embedder = embedder
        self.store = store

    def retrieve(self, query):
        vec = self.embedder.embed(query)
        return self.store.search(vec)