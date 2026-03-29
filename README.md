# 🌦️ Weather Prediction Model (ML + Flask)

A machine learning-based web application that predicts weather conditions based on various atmospheric parameters. This project demonstrates the end-to-end workflow of building, training, and deploying an ML model using Python and Flask.

---

## 🚀 Features

* 🔍 Predict weather conditions using input data
* ⚙️ Built with Scikit-learn (Random Forest Classifier)
* 🧠 Handles both categorical & numerical features using Pipeline
* 🌐 Flask-based web interface for user interaction
* 📦 Model saved using Pickle for easy deployment

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Flask**
* **HTML, CSS**

---

## 📊 Input Features

The model takes the following inputs:

* Temperature
* Humidity
* Wind Speed
* Precipitation (%)
* Atmospheric Pressure
* UV Index
* Visibility (km)
* Cloud Cover
* Season
* Location

---

## 🧠 Model Details

* Algorithm: **Random Forest Classifier**
* Preprocessing:

  * OneHotEncoding for categorical data
  * StandardScaler for numerical data
* Pipeline used for efficient workflow

---

## 📁 Project Structure

```
├── model.py
├── model.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── weather_classification_data.csv
├── app.py
└── README.md
```

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/Yogi7557/Whether_predict_model_render.git
```

2. Navigate to project folder:

```
cd Whether_predict_model_render
```

3. Create virtual environment:

```
python -m venv myenv
myenv\Scripts\activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```

5. Run the Flask app:

```
python app.py
```

6. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🌍 Future Improvements

* Add real-time weather API integration
* Improve UI/UX design
* Deploy on cloud (Render / AWS)
* Add model accuracy visualization

---

## 👨‍💻 Author

**Yoginder Kumar**
Aspiring Data Analyst / ML Developer

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub!

