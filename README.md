# End-to-End-Machine-Learning-API-FastAPI-Scikit-Learn-

A demonstration of how to build and deploy a complete machine learning pipeline as a REST API using FastAPI.
This project focuses on architecture, scalability, and production-readiness, making it easy to swap in different datasets and models.

⸻

📌 Features
	•	Full ML Workflow
	•	Data preprocessing & feature engineering (scikit-learn)
	•	TF-IDF-based text vectorization
	•	Model training & saving as a reusable pipeline (joblib)
	•	Production-Ready FastAPI Backend
	•	Clean, modular folder structure (routers, services, core configs)
	•	/predict endpoint with Pydantic request/response models
	•	Logging & Exception handling implemented
	•	Easily Extensible
	•	Can replace the current dataset or swap in advanced models like XGBoost or BERT without changing API logic.

⸻


📂 Project Structure
movie_review_ml_api/
├── app/
│   ├── core/           # Logging config
│   ├── models/         # Pydantic schemas
│   ├── routers/        # API routes
│   └── services/       # Prediction logic
├── ml_pipeline/
│   ├── custom_transformers.py
│   ├── models/         # Saved ML pipeline (joblib)
│   └── notebooks/      # Training & EDA notebooks
└── logs/               # Application logs

🚀 Getting Started

1. Clone & Install

git clone https://github.com/<your-username>/movie-review-ml-api.git
cd movie-review-ml-api
pip install -r requirements.txt

2. Run FastAPI Server

uvicorn app.main:app --reload
