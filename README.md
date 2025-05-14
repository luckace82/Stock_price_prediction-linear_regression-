# 📈 Stock Price Prediction App

This project is a simple machine learning web app built using **Linear Regression** to predict **Tesla stock closing prices** based on historical stock data. It features a user-friendly **Streamlit interface** and allows users to enter values such as Open, High, Low, and Volume to predict the Close price.

---

## 🚀 Features

- Predict stock close price based on user input
- Streamlit-powered interactive web interface
- Supports extracted/scaled models using `joblib`
- Can be extended to other stocks or features

---

## 🧠 Technologies Used

- Python
- Pandas, NumPy
- scikit-learn (LinearRegression)
- Streamlit
- joblib (for model saving/loading)

---

## 🗂️ Project Structure

├── main.py # Streamlit app
├── linear_regression_model.pkl # Trained regression model
├── TSLA.csv
├── README.md 
├── .gitignore
├── requirements.txt
└── stock_price.ipynb


---

## ⚙️ How to Run the App

### 🔧 1. Install Dependencies

```bash
pip install streamlit scikit-learn pandas numpy joblib

## Run the Streamlit App
streamlit run app.py
