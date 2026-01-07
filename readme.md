# AIRecommendationEngine

## Overview
AIRecommendationEngine is a reusable AI/ML-based recommendation engine implemented in Python using modular Clean Architecture design.

This engine is completely product-agnostic and can be integrated with any application via APIs.

## Tech Stack
- Python
- FastAPI
- scikit-learn
- numpy
- pandas
- uvicorn

## Repository Purpose
This repository contains ONLY the generic recommendation logic and ML algorithms.

All product-specific logic will remain inside the Bookmate repository or any other consumer product.

---

## Clean Architecture Layers

This repository follows Clean Architecture principles to keep the recommendation engine reusable and independent from any specific product.

### Domain Layer
Location: `src/domain/`

Contains:
- Core entities
- Exceptions
- Pure business rules

Rules:
- No external libraries
- No database code
- No framework dependencies

---

### Application Layer
Location: `src/application/`

Contains:
- Use cases
- DTOs
- Orchestration logic

Responsibilities:
- Coordinates between domain and infrastructure
- Defines input/output contracts

---

### Infrastructure Layer
Location: `src/infrastructure/`

Contains:
- ML algorithms
- Model training logic
- Model loading and saving

Responsibilities:
- TF-IDF implementation
- Similarity calculations
- Future deep learning models

---

### Interfaces Layer
Location: `src/interfaces/`

Contains:
- FastAPI endpoints
- Request/Response schemas

Responsibilities:
- Expose generic APIs for recommendation

---

## Local Setup

### 1. Clone the Repository
git clone https://github.com/<your-username>/AIRecommendationEngine.git
cd AIRecommendationEngine

### 2. Create Virtual Environment
python -m venv .venv

### 3. Activate Virtual Environment

For Mac/Linux:
source .venv/bin/activate

For Windows PowerShell:
.venv\Scripts\activate

### 4. Install Dependencies
pip install -r requirements.txt

### 5. Run FastAPI Server
uvicorn src.interfaces.main:app --reload

### 6. Verify Service

Open browser:
http://127.0.0.1:8000/

Expected response:
{
  "message": "AI Recommendation Engine Running"
}

---

## Future Integration Plan

Version 1:
- Content-based recommendations using TF-IDF
- Cosine similarity ranking
- FastAPI service

Later versions:
- Collaborative filtering
- Hybrid recommendations
- Deep learning embeddings (BERT/OpenAI)

---

## Consumers

Primary consumer:
- Bookmate product repository

Other possible consumers:
- Media platforms
- Learning platforms
- Any product needing recommendations

---

## Notes

- Keep dataset scripts in `training/`
- Write unit tests in `tests/`
- Algorithm logic must not depend on Bookmate DB

---

Happy Coding 🚀
