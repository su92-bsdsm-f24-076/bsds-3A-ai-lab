
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model_svc.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = float(request.form["age"])
    weight = float(request.form["weight"])
    height = float(request.form["height"])
    gender = request.form["gender"]

    gender_val = 1 if gender.lower() == "male" else 0

    features = np.array([[age, weight, height, gender_val]])
    prediction = model.predict(features)[0]

    return render_template("index.html", prediction_text=prediction)

if __name__ == "__main__":
    app.run(debug=True)
