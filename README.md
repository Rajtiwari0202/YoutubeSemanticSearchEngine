# YouTube Semantic Search Engine

An AI-powered search engine that finds the exact moments inside YouTube videos where a concept is discussed.

Instead of relying on video titles, descriptions, or keyword matching, this system uses semantic embeddings and vector similarity search to understand the meaning of a query and retrieve the most relevant video segments with precise timestamps.

---

## Problem Statement

Traditional YouTube search is limited to:

* Video titles
* Descriptions
* Tags
* Exact keyword matches

This makes it difficult to locate:

> "Where does this video explain Binary Search Trees?"

or

> "Show me the timestamp where the speaker talks about Redis caching."

Even if the information exists inside a video, YouTube search may never find it.

This project solves that problem by converting video transcripts into semantic vectors and performing meaning-based retrieval.

---

# Demo Workflow

User Query

```
How does Redis improve performance?
```

↓

Embedding Model converts query into vector

↓

Vector Search retrieves most similar transcript chunks

↓

Results returned

```
Video: Redis Crash Course
Timestamp: 12:31
Similarity: 0.91

Transcript:
"Redis significantly improves application performance by storing frequently accessed data in memory..."
```

↓

Click timestamp

↓

Jump directly to exact video moment

---

# Features

## Semantic Search

Search by meaning rather than exact keywords.

Examples:

```
How does JWT authentication work?
```

can match

```
JSON Web Tokens are used to verify user identity...
```

even if "JWT Authentication" never appears.

---

## Timestamp-Level Retrieval

Returns exact:

* Video
* Timestamp
* Transcript Chunk
* Similarity Score

instead of entire videos.

---

## AI Embeddings

Convert transcript chunks into dense vectors using modern embedding models.

Supported models:

* all-MiniLM-L6-v2
* BGE Small
* BGE Base
* E5 Small
* OpenAI Embeddings (optional)

---

## Vector Database Search

Store embeddings inside a vector database for fast similarity retrieval.

Supported databases:

* ChromaDB
* Redis Vector Search
* PostgreSQL + pgvector
* Pinecone

---

## Transcript Processing Pipeline

Automatically:

* Fetch transcripts
* Clean text
* Restore punctuation
* Create chunks
* Generate embeddings
* Store vectors

---

## Multi-Video Search

Search across:

* Single video
* Playlist
* Channel
* Entire knowledge base

---

## Future RAG Integration

Use retrieved transcript chunks as context for LLMs.

Example:

```
Answer my question based on these videos.
```

This converts the project into a YouTube RAG Assistant.

---

# System Architecture

```
                ┌─────────────────┐
                │ YouTube Videos  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Transcript API  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Text Cleaning   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Chunking Engine │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Embedding Model │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Vector Database │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Semantic Search │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Search Results  │
                └─────────────────┘
```

---

# Tech Stack

## Backend

* Python
* FastAPI
* LangChain
* Pydantic

---

## NLP

* Sentence Transformers
* HuggingFace
* NLTK
* spaCy

---

## Vector Database

Phase 1:

* ChromaDB

Phase 2:

* PostgreSQL + pgvector

Phase 3:

* Redis Vector Search

---

## Frontend

* Streamlit (MVP)

Future:

* Next.js
* TailwindCSS
* ShadCN UI

---

## Deployment

* Docker
* Railway
* Render
* AWS EC2

---

# Project Structure

```bash
YoutubeSemanticSearchEngine/

├── backend/
│   ├── api/
│   ├── services/
│   ├── embeddings/
│   ├── search/
│   ├── vectorstore/
│   └── models/
│
├── data/
│   ├── transcripts/
│   ├── chunks/
│   └── embeddings/
│
├── frontend/
│   ├── streamlit_app.py
│
├── scripts/
│   ├── fetch_transcripts.py
│   ├── chunk_transcripts.py
│   ├── generate_embeddings.py
│
├── tests/
│
├── docker/
│
├── docs/
│
└── README.md
```

---

# Development Roadmap

## Phase 1 — MVP

Goal:

Search inside a single YouTube video.

Tasks:

* Extract transcript
* Clean transcript
* Create chunks
* Generate embeddings
* Store in ChromaDB
* Build search API
* Return timestamps

Deliverable:

```
Query → Exact Timestamp
```

---

## Phase 2 — Multi-Video Search

Goal:

Search across many videos.

Tasks:

* Video metadata storage
* Playlist ingestion
* Bulk processing pipeline
* Ranking improvements

Deliverable:

```
Query → Best Timestamp Across Videos
```

---

## Phase 3 — Production Search Engine

Goal:

Scale to thousands of videos.

Tasks:

* PostgreSQL
* pgvector
* Redis caching
* Background workers
* Batch indexing

Deliverable:

```
YouTube Knowledge Base
```

---

## Phase 4 — Hybrid Search

Goal:

Improve retrieval quality.

Combine:

```
Semantic Search
+
Keyword Search
+
Metadata Search
```

Tools:

* BM25
* Elasticsearch
* Reciprocal Rank Fusion

---

## Phase 5 — YouTube RAG Assistant

Goal:

Chat with videos.

User:

```
Summarize all videos about Redis.
```

System:

```
Retrieve relevant chunks
+
Provide LLM answer
```

Models:

* Gemini
* OpenAI
* Claude
* Local LLMs

---

## Phase 6 — AI Copilot

Goal:

Transform YouTube into a searchable knowledge platform.

Features:

* Notes generation
* Flashcards
* Quiz generation
* Topic extraction
* Learning paths
* Knowledge graph generation

---

# API Endpoints

## Index Video

```http
POST /videos/index
```

Request

```json
{
  "url": "https://youtube.com/watch?v=xyz"
}
```

---

## Search

```http
POST /search
```

Request

```json
{
  "query": "What is vector database?"
}
```

---

## Health Check

```http
GET /health
```

---

# Example Search Result

```json
{
  "video_title": "Vector Databases Explained",
  "timestamp": "08:12",
  "similarity_score": 0.92,
  "transcript_chunk":
  "Vector databases store embeddings and allow efficient similarity search..."
}
```

---

# Future Improvements

* Multi-language support
* Speaker diarization
* Video chapter generation
* Automatic summarization
* RAG chatbot
* Hybrid retrieval
* Redis caching
* Elasticsearch integration
* Agentic search workflows
* Learning analytics

---

# Learning Outcomes

By building this project you will gain hands-on experience with:

* Information Retrieval
* Embeddings
* Vector Databases
* Semantic Search
* FastAPI
* LangChain
* ChromaDB
* PostgreSQL + pgvector
* Redis
* RAG Systems
* AI Backend Engineering
* Production AI Architecture

---

# Inspiration

Building the bridge between YouTube content and semantic knowledge retrieval.

Turning videos into a searchable knowledge base powered by AI.
