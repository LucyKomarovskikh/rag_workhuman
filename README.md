# MLOps/LLMOps Role:
• Develop a simple python module which can be used by an API for RAG
integration with a Vector Database & an LLM.

• Deploy this as an artifact to AWS

• Technologies - LangChain (or llama-index), SentenceTransformers, Bedrock
(Claude), AWS, Terraform.



SETUP

**Install dependencies**

pip install langchain sentence-transformers boto3 setuptools

**Package the module**

python setup.py sdist bdist_wheel

**Upload to aws**

aws s3 cp dist/ s3://your-bucket-name/path-to-your-package/ --recursive

**Deploy**

terraform init
terraform apply
