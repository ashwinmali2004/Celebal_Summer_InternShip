import numpy as np
import joblib
from sklearn.datasets import load_iris

def load_model(path='model/trained_model.pkl'):
    """Load the trained machine learning model."""
    return joblib.load(path)

def get_iris_features():
    """Return Iris dataset feature names."""
    iris = load_iris()
    return iris.feature_names, iris.target_names

def make_prediction(model, input_list):
    """Make prediction from input list of features."""
    input_array = np.array(input_list).reshape(1, -1)
    prediction = model.predict(input_array)
    proba = model.predict_proba(input_array)
    return prediction[0], proba[0]
