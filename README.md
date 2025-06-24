# Diabetes Prediction Using Machine Learning

**Predict whether a patient has diabetes using ML models (e.g. XGBoost).**

---

## 🚀 Table of Contents

- [Overview](#overview)  
- [Dataset](#dataset)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Model Training & Evaluation](#model-training--evaluation)  
- [Results & Performance](#results--performance)  
- [Contributing](#contributing)  
- [License](#license)  

---

## 🧠 Overview

This project builds machine learning models to predict diabetes status using the Pima Indians dataset (female patients aged ≥21). The final model is an optimized XGBoost classifier trained via cross-validation, achieving strong performance (e.g., ~90% CV score) :contentReference[oaicite:1]{index=1}.

Use this project to:
- Load and preprocess biomedical data  
- Train and tune XGBoost classifiers  
- Evaluate model accuracy, sensitivity, specificity

---

## 📊 Dataset

The dataset (Pima Indians Diabetes Dataset) consists of 768 samples with 8 medical features:
- Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age  
Outcome is binary (1: positive, 0: negative) :contentReference[oaicite:2]{index=2}.

---

## 🗂 Project Structure

