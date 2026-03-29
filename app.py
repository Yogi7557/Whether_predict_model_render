from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# load trained pipeline model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        input_data = {
            'Temperature': float(request.form['Temperature']),
            'Humidity': float(request.form['Humidity']),
            'Wind Speed': float(request.form['Wind Speed']),
            'Precipitation (%)': float(request.form['Precipitation (%)']),
            'Cloud Cover': request.form['Cloud Cover'],
            'Atmospheric Pressure': float(request.form['Atmospheric Pressure']),
            'UV Index': float(request.form['UV Index']),
            'Season': request.form['Season'],
            'Visibility (km)': float(request.form['Visibility (km)']),
            'Location': request.form['Location']
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # Prediction
        prediction = model.predict(input_df)[0]

        # 👇 ADD THIS (background class)
        bg_class = str(prediction).lower().strip()

        return render_template(
            "index.html",
            prediction_text=f"🌤 Weather Prediction: {prediction}",
            bg_class=bg_class
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)