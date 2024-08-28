import os
import boto3
from langchain.chains import VectorDBQAChain
from langchain.vectorstores import Chroma
from sentence_transformers import SentenceTransformer

# Initialize AWS Bedrock client
bedrock_client = boto3.client('bedrock-runtime')

class RAGPipeline:
    def __init__(self, vector_db, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.vector_db = vector_db
        self.embedding_model = SentenceTransformer(model_name)

    def embed_query(self, query: str):
        return self.embedding_model.encode([query])[0]

    def query_vector_db(self, query_embedding):
        results = self.vector_db.similarity_search_by_vector(query_embedding)
        return results

    def generate_response(self, context, query):
        # Call AWS Bedrock Claude model
        response = bedrock_client.invoke_model(
            modelId='claude-v2',
            body={
                "inputText": context + "\n" + query
            }
        )
        return response['body']['completions'][0]['text']

    def run_pipeline(self, query: str):
        # Step 1: the query
        query_embedding = self.embed_query(query)

        # Step 2: Retrieve relevant documents from the vector database
        documents = self.query_vector_db(query_embedding)

        # Step 3: Concatenate documents and query, pass to the LLM
        context = "\n".join([doc.page_content for doc in documents])
        response = self.generate_response(context, query)

        return response
