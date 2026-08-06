# 🏠 California Housing Price Prediction API & UI

An end-to-end Machine Learning web application that predicts median housing values in California block groups using a **RandomForestRegressor** pipeline, deployed via a **FastAPI** backend and an interactive **Streamlit** frontend.

---

## 📌 Project Overview
- **Machine Learning Pipeline:** Data preprocessing (scaling & one-hot encoding) combined with a Random Forest Regressor using `scikit-learn` Pipelines.
- **Backend (FastAPI):** Exposes a REST API endpoint `/predict` with robust Pydantic data validation (handling geographic range limits, string normalization, and logical constraints like `total_bedrooms <= total_rooms`).
- **Frontend (Streamlit):** An intuitive user interface allowing users to input census block metrics and receive real-time price predictions.

---

## 🛠️ Project Structure

```text
Project_Housing/
│
├── model/
│   ├── ML_model.py          # Script for model training, pipeline creation & evaluation
│   ├── model.pkl            # Trained Random Forest Regressor artifact (joblib serialized)
│   └── pipeline.pkl         # Feature transformation pipeline artifact (joblib serialized)
│
├── backend.py               # FastAPI application with Pydantic request validation
├── frontend.py              # Streamlit dashboard connecting to FastAPI endpoint
├── main.py                  # Entry-point execution script / workflow trigger
├── Housing_Price_Analysis.ipynb # Exploratory Data Analysis (EDA) notebook
├── housing.csv              # Dataset (California Census)
├── requirements.txt         # Project dependencies
├── .gitignore               # Files excluded from version control
└── README.md                # Project documentation

🚀 Getting Started1. Clone the RepositoryBashgit clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
cd <your-repo-name>

2. Install DependenciesBashpip install -r requirements.txt
🏃 Running the ApplicationStep 1: Start FastAPI BackendTerminal me backend server start karein:Bashuvicorn backend:app --reload

API Base URL: http://127.0.0.1:8000Interactive API Docs (Swagger UI): http://127.0.0.1:8000/docsStep 2: Start Streamlit FrontendEk naye terminal tab/window me frontend app run karein:Bashstreamlit run frontend.py

Web App Interface: http://localhost:8501📊 Features & Input ValidationsData Integrity Constraints (Pydantic):Logical Check: total_bedrooms cannot be greater than total_rooms.Automatic Normalization: ocean_proximity values are automatically converted to uppercase (e.g., inland $\rightarrow$ INLAND).Boundary Validation: Latitude (32.0 to 42.0) and Longitude (-125.0 to -114.0) are enforced to fit California boundaries.