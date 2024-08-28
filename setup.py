from setuptools import setup, find_packages

setup(
    name="rag_pipeline",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "sentence-transformers",
        "boto3"
    ],
)
