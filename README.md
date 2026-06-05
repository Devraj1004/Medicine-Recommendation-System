# 🩺 Medicine Recommendation System

### An Intelligent, Safety-Aware Healthcare ML Application

> **Role Fit:** Machine Learning Engineer | AI/ML Engineer | Software Engineer (ML)
> **Core Skills Demonstrated:** Python, Machine Learning, Data Engineering, Feature Mapping, Model Deployment, Safety Logic, Clean Code Architecture

## 🚀 Project Summary

The **Medicine Recommendation System** is a **production-minded Machine Learning application** that predicts diseases based on user-reported symptoms and recommends appropriate medicines.

What makes this project **stand out** is not just disease prediction—but how it **handles real-world complexity**:

* Human-friendly symptom language (what patients *actually* say)
* Safety-aware overrides for critical diseases
* Robust validation to prevent misleading outputs
* Clean modular architecture ready for scaling

This project demonstrates **end-to-end ML ownership**—from raw data to deployment-ready logic.

---

## 🎯 Business & Real-World Relevance

In real healthcare settings:

* Patients describe symptoms informally (“bukhar”, “cold”, “body pain”)
* ML models require structured, standardized inputs
* Incorrect predictions (e.g., AIDS, heart attack) can cause panic

### ✅ This system solves all three problems.

It bridges **human language → machine understanding → safe medical suggestions**, making it suitable for:

* Healthcare chatbots
* Triage systems
* Telemedicine assistants
* ML-based decision support tools

---

## 🧠 System Architecture (High-Level)

```
User Symptoms (Natural Language)
        ↓
Symptom Normalization & Mapping
        ↓
Feature Vector Construction (132 symptoms)
        ↓
Trained ML Model (Decision Tree)
        ↓
Safety Rule Overrides (Critical Diseases)
        ↓
Disease Prediction
        ↓
Medicine Recommendation
```

---

## 🧩 Key Features

### ✅ 1. Human-Centric Symptom Mapping

* Converts **500+ common symptom phrases** into dataset-recognized medical terms
* Supports Indian conversational inputs:

  * “bukhar” → `high_fever`
  * “loose motions” → `diarrhoea`
  * “throat pain” → `patches_in_throat`

📌 This shows **domain understanding + UX thinking**.

---

### ✅ 2. Machine Learning Model

* Algorithm: **Decision Tree Classifier**
* Dataset: Disease Prediction (Kaggle)
* Input: Binary symptom vector (132 features)
* Output: Disease class (41 diseases)

Model artifacts are persisted using **joblib**, ensuring:

* Fast inference
* Reusability
* Deployment readiness

---

### ✅ 3. Safety-Aware Prediction Logic 🔒

Critical diseases require **mandatory symptom evidence**:

| Disease      | Safety Requirement                                   |
| ------------ | ---------------------------------------------------- |
| AIDS         | Weight loss, blood transfusion, unsterile injections |
| Tuberculosis | Chronic cough, blood in sputum                       |
| Heart Attack | Chest pain + breathlessness + sweating               |

If requirements are **not met**, predictions are **automatically downgraded**.

📌 This is **production-grade thinking**, not academic ML.

---

### ✅ 4. Medicine Recommendation Engine

* Uses a structured CSV (`disease_to_medicine.csv`)
* Clean separation of concerns:

  * Disease prediction ≠ medicine mapping
* Easy to update or extend

---

### ✅ 5. Robust Input Validation

* Requires **at least 2–3 valid symptoms**
* Handles:

  * Unknown inputs
  * Partial mappings
  * Repeated execution without crashing

📌 Demonstrates defensive programming and reliability.

---

## 📂 Project Structure (Clean & Scalable)

```
MEDICINE_RECOMMENDATION_SYSTEM/
│
├── Data/
│   ├── Training.csv
│   ├── Testing.csv
│   └── disease_to_medicine.csv
│
├── models/
│   ├── disease_model.pkl
│   └── feature_names.pkl
│
├── app.py                     # Main CLI application
├── train_model.py             # Model training pipeline
├── recommender.py             # Disease prediction logic
├── medicine_recommender.py    # Disease → Medicine mapping
├── symptoms_mapper.py         # Human → Dataset symptom mapping
├── test_model.py              # Model testing & validation
├── list_symptoms.py           # Displays valid dataset symptoms
│
├── requirements.txt           # Dependencies
└── README.md                  # Documentation
```

📌 This structure reflects **industry-level code organization**.

---

## ⚙️ Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Core programming     |
| pandas       | Data preprocessing   |
| numpy        | Numerical operations |
| scikit-learn | ML model             |
| joblib       | Model persistence    |

---

## ▶️ How to Run the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Sample Input

```
fever, cold, headache
```

### Sample Output

```
🧠 Predicted Disease: Common Cold
💊 Recommended Medicine: Paracetamol
```

---

## 📊 Dataset Details

* Total Symptoms: **132**
* Total Diseases: **41**
* Format: Binary-encoded symptom presence
* Source: Kaggle (Disease Prediction Dataset)

---

## 🎓 What This Project Demonstrates

From a recruiter’s perspective, this project proves:

* ✅ End-to-end ML pipeline ownership
* ✅ Real-world problem solving
* ✅ Safety-first AI design
* ✅ Clean, maintainable code
* ✅ Strong Python & ML fundamentals
* ✅ Ability to think beyond accuracy metrics

---

## 🚀 Future Enhancements

* Web interface using **Streamlit**
* Confidence scoring for predictions
* Multi-medicine recommendations
* Severity estimation
* Integration with medical APIs

---

## 👨‍💻 Author

**Devraj D. Korgaonkar**
B.Tech – Computer Science Engineering (AI & ML)
Aspiring Machine Learning Engineer

📌 *Actively seeking opportunities in AI/ML, Data Science, and Software Engineering roles.*

---

## ⚠️ Disclaimer

This application is developed **strictly for educational purposes**.
It does **not replace professional medical advice**. Always consult a certified healthcare professional.

---
