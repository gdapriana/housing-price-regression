import streamlit as st
import numpy as np


def input_features():
  col1, col2 = st.columns(2)

  with col1:
    square_feet = st.number_input("Square feet (m2)", min_value=0.0, step=0.01, value=1.0)
    num_bathroom = st.number_input("Number of Bathroom", min_value=0)
    year_build = st.number_input("Year build", min_value=1000)
    location_score = st.number_input("Location Score (1-10)", value=5, min_value=0, max_value=10)

  with col2:
    num_bedrooms = st.number_input("Number of bedrooms", min_value=0)
    num_floor = st.number_input("Number of floor", min_value=0)
    garage_size = st.number_input("Garage size (m2)", min_value=0.0, step=0.01, value=1.0)
    distance_to_center = st.number_input("Distance to center (km)", min_value=0.0, step=0.01, value=1.0)
    col21, col22 = st.columns(2)
    with col21:
      has_pool = st.checkbox("Has Pool", value=False)
      if has_pool:
        has_pool = 1
      else:
        has_pool = 0
    with col22:
      has_garden = st.checkbox("Has garden", value=False)
      if has_garden:
        has_garden = 1
      else:
        has_garden = 0

  x = np.array([[square_feet,
                num_bedrooms,
                num_bathroom,
                num_floor,
                year_build,
                has_garden,
                has_pool,
                garage_size,
                location_score,
                distance_to_center]])
  clicked = st.button("Predict", use_container_width=True)

  if clicked:
    return x


def predict(model, scaler, x):
  x = scaler.transform(x)
  return model.predict(x)