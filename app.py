# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from flask import Flask, render_template, request
import tensorflow
from tensorflow import keras
from tensorflow.keras.models import load_model
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
    
    model=load_model('my_model.h5')
    prediction=model.predict([[distance,destination,source,product_id,cab_type]])[0]
    return render_template('index.html', prediction=f'{round(prediction,2)}')

if __name__ == '__main__':
    app.run(debug=True)
    
