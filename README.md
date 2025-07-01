# FastAPI Learning Repository ⚡

This repo is a **progressive guide to mastering FastAPI**, from scratch to production. Each branch captures a stage in the journey — ideal for backend devs looking to build **fast, scalable, and modern APIs** using Python.

---

## 🎯 Why This Exists

- Learn FastAPI step-by-step, versioned by branches.
- Build real apps that grow in complexity.
- Understand asynchronous Python, type hints, dependency injection, Pydantic models, testing, and deployment.
- Use modern Python practices and clean architecture.

---

## 🌿 Branch Overview

| Branch     | Description                                      |
|------------|--------------------------------------------------|
| `Appv1`    | Basic FastAPI app, single endpoint               |

> Each branch is self-contained and tagged with clean commits for tracking changes.

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/Aeneas06/FastAPI_Learning.git
cd App

# Checkout a version
git checkout Appv3

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
