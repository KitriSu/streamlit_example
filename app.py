import streamlit as st
import pandas as pd
from model import model

st.title("Iris Species Predictor")
st.write("This app predicts the species of an Iris flower based on its measurements.")

# Input sliders for features
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

# Create a DataFrame for prediction
input_data = pd.DataFrame(
    [[sepal_length, sepal_width, petal_length, petal_width]],
    columns=[
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ],
)

# Predict the species
prediction = model.predict(input_data)
st.write("Predicted Species:", prediction[0])
