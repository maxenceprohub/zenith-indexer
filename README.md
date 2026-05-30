<div align="center">

# ZENITH INDEXER

### High-Performance Local Knowledge Retrieval System

<p align="center">
  <img src="https://img.shields.io/badge/C++-17%20%2F%2020-blue?style=flat-square&logo=c%2B%2B" />
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Status-Prototype-orange?style=flat-square" />
</p>

</div>

---

# Overview

Zenith-Indexer is an experimental local knowledge retrieval system focused on combining:

- a Python prototype for rapid development, workflow automation, and AI integration,
- a future C++ core for performance-oriented indexing and processing.

The project currently provides a robust Python-based prototype capable of scanning local directories, calculating keyword metrics, generating automated reports, and querying documents using a secure local AI integration (OpenAI API).

The long-term objective is to explore high-performance indexing, scalable document processing, and advanced Retrieval-Augmented Generation (RAG) architectures.

---

# Project Structure

```text
zenith-indexer/
│
├── ai-interface/
│   └── main.py
│
├── core-engine/       # Reserved for C++ engine
│
├── documents/         # Place your .txt files here
│
├── tests/
│
├── .env               # Local environment variables (API Keys - DO NOT COMMIT)
├── .gitignore         # Prevents secrets from being pushed to GitHub
├── README.md
└── LICENSE
