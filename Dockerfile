FROM quay.io/jupyter/datascience-notebook

RUN pip install --user langchain langgraph langchain-openai openai langchain_community azure-identity faiss-cpu


