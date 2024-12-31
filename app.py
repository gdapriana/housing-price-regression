import streamlit as st
import pandas as pd
from sources.modeling import regression
from ui.homepage import homepage
from ui.dataset import dataset
from ui.predict import input_features, predict
from sources.preprocessing import cleaning, minmaxscaler

if __name__ == '__main__':
  df = pd.read_csv('sources/dataset.csv')
  x, y = cleaning(df, label_column_name="Price")
  x, scaler = minmaxscaler(x)
  model = regression(x, y)

  st.title("Housing Price Prediction")
  st.markdown(f"<p style='text-align: left;'>Created by <b>I Komang Gede Apriana</b></h2>", unsafe_allow_html=True)
  tab1, tab2, tab3 = st.tabs(["Homepage", "Predict", "Dataset"])
  with tab1:
    homepage()
  with tab2:
    x_input = input_features()
    if x_input is not None:
      result = round(predict(model, scaler, x_input)[0], 0)
      if result <= 0:
        result = 0
      st.markdown(f"<h3 style='text-align: center;'>Predicted: {result}$</h3>", unsafe_allow_html=True)
  with tab3:
    dataset()