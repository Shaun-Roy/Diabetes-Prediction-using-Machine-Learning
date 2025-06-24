from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html', prediction=None, probability=None)


@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from form input
    try:
        features = [float(request.form.get(col)) for col in
                    ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                     'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
    except Exception as e:
        return jsonify({'error': f'Invalid input: {str(e)}'})

    # Scale features and predict
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)[0]
    proba = model.predict_proba(features_scaled)[0][1]

    return render_template('index.html', prediction=prediction, probability=proba)

if __name__ == '__main__':
    app.run(debug=True)
