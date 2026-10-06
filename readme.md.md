<div align="center">

# 🚗 Car Price Predictor

An end-to-end Machine Learning web application that predicts used car market valuations based on vehicle specifications and historical sales data.

[![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📌 Overview

This project cleans messy, unstructured raw data of used cars scraped from Quikr, handles outliers and categorical encodings, trains a **Linear Regression** model using a Scikit-Learn Pipeline, and serves real-time predictions via an interactive **Flask** web application.

---

## 🏗️ Project Architecture & Pipeline

```text
quikr_car.csv (Raw) 
       │
       ▼
 [ FILTER DATA.PY ] ──> Data Cleaning & Feature Extraction
       │
       ▼
 orgnized_data.csv ──> Cleaned & Normalized Dataset
       │
       ▼
  [ MODEL.PY ]      ──> OneHotEncoder + Linear Regression (Pipeline)
       │
       ▼
LinearRegressionModel.pkl ──> Serialized Model Artifact
       │
       ▼
   [ app.py ]       ──> Flask API & Web Interface (HTML/CSS)
```

1. **Data Cleaning (`FILTER DATA.PY`)**:
   - Stripped unwanted labels and non-numeric characters from the `year`, `kms_driven`, and `Price` columns.
   - Cleaned out unpriced listings (`Ask For Price`) and `NaN` fuel records.
   - Trimmed car names to standard 3-word brand and model tokens.
   - Filtered out extreme price outliers ($> 6,000,000$).

2. **Model Training (`MODEL.PY`)**:
   - Encoded categorical features (`name`, `company`, `fuel_type`) using `ColumnTransformer` and `OneHotEncoder`.
   - Iterated across 1,000 train-test splits to locate optimal variance and stability, achieving maximum $R^2$ score.
   - Exported the complete estimator pipeline directly into `LinearRegressionModel.pkl`.

3. **Web Application (`app.py`)**:
   - Dynamic dropdown selectors powered by Flask routes and backend CSV lookups.
   - Prediction endpoint accepting POST data, formatting feature matrices, and delivering live predictions.

---

## 🚀 Live Demo & Features

- **Company & Model Dynamism**: Select from over 25 car manufacturers and hundreds of supported models.
- **Robust Feature Handling**: Auto-encodes fuel types (Petrol, Diesel, LPG) alongside mileage and registration year.
- **Instant Valuation**: Real-time pricing predictions rendered instantly.

---

## ⚙️ Local Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
```

### 2. Create a Virtual Environment
```bash
# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## 📂 Project Structure

```text
├── app.py                      # Flask entry point and routing
├── FILTER DATA.PY              # Data cleaning and preprocessing script
├── MODEL.PY                    # Model architecture and training script
├── LinearRegressionModel.pkl   # Serialized trained pipeline
├── orgnized_data.csv           # Cleaned dataset
├── quikr_car.csv               # Raw dataset
├── templates/
│   └── index.html              # Frontend user interface
├── requirements.txt            # Project dependencies
├── Procfile                    # Production server config (Gunicorn)
└── README.md                   # Project documentation
```

---

## ☁️ Deployment Guide

### Deploying for Free on Render.com

1. Push your repository to **GitHub**.
2. Sign up or log into [Render](https://render.com/).
3. Click **New +** > **Web Service**.
4. Connect your GitHub repository.
5. Set the configurations:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Choose the **Free** instance type and click **Deploy Web Service**.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).