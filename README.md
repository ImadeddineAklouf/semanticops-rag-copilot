# SemanticOps RAG Platform

Modern Retrieval-Augmented Generation platform built with FastAPI, ChromaDB and Python.

## Features

- Multi-format ingestion
- Chunking engine
- Embedding pipeline
- Vector database
- Retrieval engine
- RAG pipeline
- Monitoring
- Evaluation
- REST API

## Architecture

Document
↓
Loader
↓
Chunker
↓
Embeddings
↓
ChromaDB
↓
Retriever
↓
Context Builder
↓
Prompt Builder
↓
LLM
↓
Answer

## API

POST /upload

POST /ingest

POST /query

GET /health

GET /metrics

GET /evaluation

GET /config

GET /debug/chunks

## Tech Stack

- Python 3.13
- FastAPI
- ChromaDB
- Pydantic
- Pytest

## Run locally

```bash
python -m venv .venv

pip install -r requirements.txt

uvicorn app.api.main:app --reload
