# 🔧 Predictive Maintenance Analysis using Artificial Neural Networks (ANN)

A Machine Learning and Deep Learning-based web application that predicts the likelihood of industrial machine failure using operational parameters. The application is built with **Python**, **TensorFlow/Keras**, and **Streamlit**, providing an interactive interface for real-time predictions.

---

## 📖 Table of Contents

* [Project Overview](#-project-overview)
* [Objectives](#-objectives)
* [Features](#-features)
* [Technologies Used](#-technologies-used)
* [Project Structure](#-project-structure)
* [Dataset](#-dataset)
* [Machine Learning Workflow](#-machine-learning-workflow)
* [Application Workflow](#-application-workflow)
* [Installation](#-installation)
* [How to Run](#-how-to-run)
* [Future Enhancements](#-future-enhancements)
* [Author](#-author)

---

# 📌 Project Overview

Unexpected machine failures can lead to production downtime, increased maintenance costs, and reduced operational efficiency. Predictive Maintenance aims to identify potential failures before they occur using historical and operational machine data.

This project implements an **Artificial Neural Network (ANN)** model that predicts machine failure based on important machine parameters. The trained model is deployed using **Streamlit**, allowing users to interact with the prediction system through an intuitive web interface.

---

# 🎯 Objectives

* Predict machine failures before they occur.
* Reduce unexpected equipment downtime.
* Demonstrate an end-to-end Machine Learning workflow.
* Deploy a trained ANN model using Streamlit.
* Provide an easy-to-use interface for real-time predictions.

---

# 🚀 Features

* Interactive Streamlit dashboard
* Real-time machine failure prediction
* Artificial Neural Network (ANN) model
* Data preprocessing using StandardScaler
* Supports different machine types (L, M, H)
* Failure probability visualization
* Clean and responsive user interface
* Simple and user-friendly input controls

---

# 🛠️ Technologies Used

| Category             | Technology        |
| -------------------- | ----------------- |
| Programming Language | Python            |
| Deep Learning        | TensorFlow, Keras |
| Data Processing      | Pandas, NumPy     |
| Machine Learning     | Scikit-learn      |
| Visualization        | Matplotlib        |
| Web Framework        | Streamlit         |
| Model Storage        | `.keras`, Pickle  |
| Version Control      | Git & GitHub      |

---

# 📂 Project Structure

```text
Predictive-Maintenanace-Analysis/
│
├── app.py                  # Streamlit application
├── ann_model.keras         # Trained ANN model
├── scaler.pkl             # StandardScaler object
├── requirements.txt       # Required Python packages
└── README.md
```

---

# 📊 Dataset

The project is based on an industrial predictive maintenance dataset containing machine operating conditions.

### Input Features

* Air Temperature (K)
* Process Temperature (K)
* Rotational Speed (RPM)
* Torque (Nm)
* Tool Wear (minutes)
* Machine Type (L / M / H)

### Output

* Machine Failure Prediction

  * ✅ Low Risk
  * ⚠️ High Risk

---

# 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Encoding
4. Feature Scaling using StandardScaler
5. ANN Model Training
6. Model Evaluation
7. Save Trained Model
8. Deploy using Streamlit

---

# ⚙️ Application Workflow

```text
User Inputs
      │
      ▼
Input Validation
      │
      ▼
Feature Encoding
      │
      ▼
StandardScaler
      │
      ▼
ANN Model (.keras)
      │
      ▼
Failure Probability
      │
      ▼
Prediction Result
      │
      ▼
Visualization
```

---

# ▶️ Installation

## Clone the Repository

```bash
git clone https://github.com/isai90420/Predictive-Maintenanace-Analysis.git
```

## Navigate to the Project Folder

```bash
cd Predictive-Maintenanace-Analysis
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will start locally and can be accessed through your browser.

---

## 📸 Application Screenshots

### Home Page

![Home Page](images/home.png)

### Prediction Result

![Prediction Result](images/prediction.png)

---

# 📈 Output

The application displays:

* Failure probability
* Machine status prediction
* Graphical comparison of failure probability

---

# 🔮 Future Enhancements

* Compare multiple Machine Learning models
* Improve model accuracy using hyperparameter tuning
* Deploy the application to the cloud
* Integrate real-time IoT sensor data
* Add prediction history and analytics dashboard
* Implement user authentication

---

# 👩‍💻 Author

**V. Isaipriya**

B.Tech – Artificial Intelligence and Data Science

Easwari Engineering College

GitHub: https://github.com/isai90420

---

## ⭐ Support

If you found this project useful, consider giving the repository a **Star ⭐** on GitHub.
