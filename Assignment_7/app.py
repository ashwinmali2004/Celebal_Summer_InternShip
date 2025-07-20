import streamlit as st
import numpy as np
import joblib
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load model
model = joblib.load('model/trained_model.pkl')
iris = load_iris()

# Title
st.title("Iris Flower Classifier 🌸")

# Input fields
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2)

# Predict button
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Class: {iris.target_names[prediction[0]]}")

    # Feature importance plot
    st.subheader("Feature Importance")
    fig, ax = plt.subplots()
    ax.barh(iris.feature_names, model.feature_importances_)
    ax.set_xlabel("Importance")
    st.pyplot(fig)
