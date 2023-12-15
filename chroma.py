# ！/usr/bin env python3
# -*- coding: utf-8 -*-
# author: yangyunlong time:2023/12/15
import chromadb


class ChromaDB():

    def __init__(self, path):
        self.path = path
        self.client = chromadb.PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection("search")

    def load(self, file_path):
        self.path = file_path
        self.client = chromadb.PersistentClient(path=file_path)
        self.collection = self.client.get_collection("search")

    def search(self, vector, n_results):
        results = self.collection.query(query_embeddings=[vector], n_results=n_results)
        return results['documents'][0]

    def from_texts(self, vectors, documents):
        ids = []
        for i, doc in enumerate(documents):
            ids.append(str(i) + "_" + doc)
        self.collection.add(embeddings=vectors, documents=documents, ids=ids)

    def add_texts(self, vectors, documents, ids):
        self.collection.upsert(embeddings=vectors, documents=documents, ids=ids)
