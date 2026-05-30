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

## Overview

Zenith-Indexer is an experimental local knowledge retrieval system focused on combining:

- a **Python prototype** for rapid development, workflow automation, and AI integration,
- a **future C++ core** for performance-oriented indexing and processing.

The project currently provides a robust Python-based prototype capable of scanning local directories, calculating keyword metrics, generating automated reports, and querying documents using a secure local AI integration (OpenAI API).

The long-term objective is to explore high-performance indexing, scalable document processing, and advanced Retrieval-Augmented Generation (RAG) architectures.

---

## Project Structure

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
```

---

## Current Architecture

The project currently follows a simple development approach:

```
Prototype logic in Python (File I/O, Metrics, LLM API)
→
Optimize performance-critical components in C++
```

At the moment:
- `ai-interface/` contains the working Python prototype,
- `core-engine/` is reserved for the future C++ implementation.

---

## Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| Core Engine | C++17 / C++20 | Planned high-performance indexing engine |
| AI Interface | Python 3.10+ | Prototype, workflow automation, and AI querying |
| LLM Integration | OpenAI API & python-dotenv | Secure local RAG experimentation |
| Testing | Python test suite | Reliability and validation |

---

## Current Features

- Local `.txt` document processing and automated directory scanning
- Basic analysis pipeline (keyword frequency and density metrics)
- Automated metric report generation (`rapport_*.txt`)
- Robust error handling (format validation, permission checks, API limits)
- **AI-Assisted Querying**: Secure connection to OpenAI's `gpt-4o-mini` for document-based Q&A

---

## Planned Features

The following components are planned but not yet implemented:

- C++ indexing engine (core parsing system)
- Semantic search (vector embeddings)
- GPU acceleration (CUDA)
- Graph-based retrieval structures

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/maxenceprohub/zenith-indexer.git
cd zenith-indexer
```

### 2. Setup the Environment

Install the required Python libraries:

```bash
pip install openai python-dotenv
```

Create a `.env` file at the root of the project and add your OpenAI API key:

```plaintext
OPENAI_API_KEY=sk-your_api_key_here
```

> **Note:** The `.env` file is ignored by git to keep your credentials secure.

### 3. Add Documents

Place your `.txt` files directly inside the `documents/` folder at the root of the project.

### 4. Run the Python Prototype

```bash
python ai-interface/main.py
```

The prototype will scan the files, ask for a keyword, generate an analysis report, and offer an interactive AI prompt to chat with your document.

---

## Development Status

| Component | Status |
|---|---|
| Python Prototype | ✅ Functional |
| Report Generation | ✅ Functional |
| AI Integration | ✅ Functional (Prototype) |
| C++ Core Engine | 🔧 In Development |
| GPU Support (CUDA) | 📋 Planned |

---

## Contributing

Contributions and feedback are welcome.

```bash
git checkout -b feature/my-feature
git commit -m "feat: add my feature"
git push origin feature/my-feature
```

---

## License

License information will be added later in the project lifecycle.

---

## Author

**Maxence** — Software engineering student interested in:

- systems programming
- C++ & performance optimization
- artificial intelligence
- low-level software architecture
