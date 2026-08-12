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

Zenith-Indexer is an advanced, production-ready local knowledge retrieval system built from the ground up in **pure Python**. It bridges the gap between high-performance local text processing, automated data auditing, and intelligent LLM-driven orchestration. 

Eliminating the need for complex, multi-language stacks, the system delivers an optimized, lightweight Python architecture capable of hot-scanning directories, extracting deep text metrics, generating automated compliance reports, and conducting seamless, stateful AI Q&A sessions via a secure local integration with OpenAI's models (`gpt-4o-mini`).

The core objective of Zenith Indexer is to push the boundaries of pure Python engineering to build an enterprise-grade, high-performance Retrieval-Augmented Generation (RAG) architecture featuring sub-millisecond semantic search and neural reranking.

---

## Project Structure

```text
zenith-indexer/
│
├── src/                      # 🧠 Application Source Code (Pure Python)
│   ├── __init__.py           # Makes 'src' a formal Python package
│   └── main.py               # Core pipeline (Scanner, Metrics, Logging, AI Chat)
│
├── documents/                # 📁 Local Data Repository
│   ├── sample.txt            # Local text knowledge base
│   └── document.pdf          # Next-gen PDF files integration (Roadmap)
│
├── tests/                    # 🧪 Automated Testing Suite
│   └── test_logic.py         # Unit tests for core processing logic
│
├── .env                      # 🔑 Local Environment Secrets (DO NOT COMMIT)
├── .gitignore                # 🛡️ Git Guard (Excludes .env, reports, and logs)
├── run.py                    # ⚡ Centralized App Entry Point (Micro-Launcher)
├── zenith.log                # 📝 Automated Production-Grade System Logs
├── README.md                 # 📖 Project Documentation & Showcase
└── LICENSE                   # ⚖️ MIT Software License
```

---

## 🏗️ System Architecture

The project is engineered around a clean, decoupled, and unified Python architecture designed for stability and rapid scaling:

```
[ Central Launchpad (run.py) ]
│
▼ ( Native System Execution )
[ Core Processing Engine (src/main.py) ]
│
┌───────┴───────┐
▼               ▼
[ Local Analytics ] [ Semantic LLM Orchestration ]
( Metrics & Reports )   ( Continuous AI Chat Loop )
```
At the moment:
* **`run.py`** acts as the centralized micro-launcher at the root, securing a clean system-level execution context (`python3`).
* **`src/`** encapsulates the entire core logic, isolating file scanning, advanced text normalization, density metrics, and the stateful conversational AI loop.
* **`documents/`** serves as the hot-swappable local data repository for automatic indexing.

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose | Status |
| :--- | :--- | :--- | :--- |
| **System Orchestration** | Python 3.10+ | Centralized workflow automation and rapid native file parsing | **Active** |
| **LLM Intelligence** | OpenAI API (`gpt-4o-mini`) | Context-aware, semantic RAG orchestration and continuous chat loop | **Active** |
| **Environment Control** | `python-dotenv` | Production-grade, secure injection of local API credentials | **Active** |
| **Event Auditing** | Native `logging` Module | Enterprise dual-stream tracing (Console + `zenith.log`) with microsecond precision | **Active** |
| **Quality Assurance** | Python Test Suite | Validation of text cleansing engines and metrics calculation algorithms | **Active** |

---

## 🚀 Current Features

- ** ⚡ Centralized Entry Point & Launchpad** Features a standalone `run.py` script at the root level utilizing native system execution (`python3`) to ensure a clean, decoupled environment activation.

- ** 📁 Automated Hot-Directory Scanning** Automated auditing of the local `documents/` repository to instantly fetch, validate, and list available knowledge bases.

- ** 🧹 Custom Text Cleansing Engine** Low-level punctuation-filtering and case-normalization pipeline designed to ensure flawless token segmentation and exact keyword matching.

- ** 📊 Advanced Analytics & Compliance Reporting** Calculates exact word token counts, performs precise keyword density metrics, and automatically generates structured local audit files (`rapport_*.txt`) with resolved absolute system paths.

- ** 🛡️ Enterprise Event Auditing & Logging** Simultaneous dual-stream tracing that writes real-time operations, security warnings, and runtime errors into both the live terminal and the `zenith.log` system file.

- ** 🤖 Context-Injected Conversational AI** An interactive, stateful chat loop (`while True`) that injects the loaded document directly into the system prompt of OpenAI's `gpt-4o-mini`, enabling deep, contextual, and secure document Q&A.

- ** 🧱 Robust Fail-Safe Architecture** Production-grade defensive programming with dedicated catch-blocks for `UnicodeDecodeError` (format validation), `PermissionError` (access control), and API exception routing.

---

## 🗺️ Cutting-Edge Roadmap (Python RAG Architecture)

The project's engineering roadmap is focused on evolving Zenith Indexer into an enterprise-grade, high-performance semantic search platform using pure Python:

- [ ] ** 📄 Native Multi-Page PDF Extraction**
  Integration of `pypdf` or `pdfplumber` pipelines to cleanly extract unstructured text from complex layouts and multi-page corporate PDF documents.

- [ ] ** 🧩 Context-Aware Semantic Chunking**
  Transitioning from arbitrary string splitting to intelligent text chunking based on document structure, sentences, and semantic boundaries to maintain context integrity before vectorization.

- [ ] ** 🧬 Vector Embeddings Pipeline**
  Upgrading the search engine from keyword-frequency analytics to true dense mathematical representations using state-of-the-art local models (via `sentence-transformers`).

- [ ] ** 🗄️ High-Performance Embedded Vector Database**
  Seamless integration of ultra-fast local indices like **ChromaDB**, **Qdrant**, or **FAISS** to store and query embeddings with sub-millisecond latent execution.

- [ ] ** 🎯 Neural Cross-Encoder Reranking**
  Implementation of a local reranking pipeline (such as BGE-Reranker) to score and re-order retrieved contexts, ensuring only the highest-quality insights are fed to the LLM.

---

## ⚡ Getting Started

Follow these steps to deploy, configure, and initialize the Zenith Indexer platform locally on your machine.

### 1. Clone the Repository
Clone the codebase directly from the production repository and navigate straight into the project root folder:
```bash
git clone [https://github.com/maxenceprohub/zenith-indexer.git](https://github.com/maxenceprohub/zenith-indexer.git)
cd zenith-indexer
```

### 2. Configure Environment & Dependencies
Install the required enterprise-grade libraries using the explicit Python 3 package manager to completely avoid global environment or version conflicts:
```bash
python3 -m pip install openai python-dotenv
```
Generate a secure local environment configuration file at the root level to isolate your private application credentials:

```bash
touch .env
```
> **Note:** The `.env` file is ignored by git to keep your credentials secure

Open the .env file and append your private OpenAI security key using the standard system syntax:

```bash
OPENAI_API_KEY=sk-your_actual_api_key_here
```

### 3. Add Documents

Place your `.txt` files directly inside the `documents/` folder at the root of the project.

### 4. Run the Python Prototype

```bash
python3 run.py
```

Once initialized, the platform will seamlessly execute its multi-format directory audit, calculate your advanced text metrics, instantly generate a structured analytics report (`rapport_*.txt`), and spin up a stateful, interactive AI session enabling you to chat live with your local documents.

---

## 📊 System Development Status

| Architecture Component | Engine Status | Implementation Layer |
| :--- | :--- | :--- |
| **Automated Directory Auditing** | 🟢 **Production Ready** | Pure Python (`src/main.py`) |
| **Text Cleansing & Analytics Engine** | 🟢 **Production Ready** | Pure Python (`src/main.py`) |
| **Compliance Report Generation** | 🟢 **Production Ready** | Pure Python (`src/main.py`) |
| **Context-Injected AI Loop** | 🟢 **Production Ready** | OpenAI `gpt-4o-mini` Integration |
| **Enterprise Event Logging** | 🟢 **Production Ready** | Dual-Stream Native System |
| **Centralized Micro-Launcher** | 🟢 **Production Ready** | Unified Root Script (`run.py`) |
| **Semantic Vector Search (RAG)** | ⚙️ **Active Development** | ChromaDB & `sentence-transformers` |

---

## 🤝 Contributing & Open Source Collaboration

Contributions, feature requests, and feedback are highly appreciated to help push Zenith Indexer forward. Whether you are fixing bugs, optimizing performance, or proposing new RAG architectures, your input is welcome!

### Development Workflow

Follow this clean Git workflow to submit your enhancements to the codebase:

```bash
# 1. Create a dedicated branch for your feature or fix
git checkout -b feature/amazing-capability

# 2. Commit your changes using descriptive, conventional commit messages
git commit -m "feat: implement semantic vector chunking pipeline"

# 3. Push your branch directly to the upstream remote repository
git push origin feature/amazing-capability
```

---

## License

License information will be added later in the project lifecycle.

---

## 👤 Author

**Maxence** — Software Engineering Student & Systems Architecture Enthusiast.

Driven by a passion for creating highly optimized software, my technical focus centers on:
* **Advanced Artificial Intelligence** & Next-Gen Retrieval-Augmented Generation (RAG) Systems.
* **High-Performance Python Engineering** & Enterprise-Grade Workflow Automation.
* **Systems Programming** & Low-Level Software Architecture Concepts.
* **Data Pipelines Optimization** & Secure Local Knowledge Management.

```
_____ _                 _       __     __
 |_   _| |__   __ _ _ __ | | __   \ \   / /__  _   _
   | | | '_ \ / _` | '_ \| |/ /    \ \ / / _ \| | | |
   | | | | | | (_| | | | |   <      \ V / (_) | |_| |
   |_| |_| |_|\__,_|_| |_|_|\_\      |_| \___/ \__,_|

```
