# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from flask import Flask, render_template, request

import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', prediction=None)

@app.route('/home')
def home():
    return render_template('index.html', prediction=None)

@app.route('/estimate', methods=['POST'])
def estimate():
    # Retrieve user input data from the form
    distance = float(request.form['distance'])
    source = request.form['source']
    destination = request.form['destination']
    product_id = request.form['product_id']
    cab_type = request.form['car_type']
    # Replace this with your actual diabetes prediction model
    # For demonstration, we'll use a simple rule-based prediction
    model=joblib.load('uber_fare_prediction_model.pkl')
    prediction=model.predict([[distance,destination,source,product_id,cab_type]])[0]
    return render_template('index.html', prediction=f'{round(prediction,2)}')

if __name__ == '__main__':
    app.run(debug=True)
    