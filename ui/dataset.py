import streamlit as st
import pandas as pd

def dataset():
  st.subheader('About Dataset')
  st.link_button("Kaggle", "https://www.kaggle.com/datasets/denkuznetz/housing-prices-regression")
  st.markdown('''
  This task involves predicting the price of real estate properties based on various features that influence the value of a property. The dataset contains several attributes of real estate properties such as square footage, the number of bedrooms, bathrooms, floors, the year the property was built, whether the property has a garden or pool, the size of the garage, the location score, and the distance from the city center.
  The goal is to build a regression model that can predict the Price of a property based on the provided features.
  Dataset Columns:

  | Column Name | Description |
  |---|---|
  | Square_Feet | The area of the property in square meters. |
  | Num_Bedrooms | The number of bedrooms in the property. |
  | Num_Bathrooms | The number of bathrooms in the property. |
  | Num_Floors | The number of floors in the property. |
  | Year_Built | The year the property was built. |
  | Has_Garden | Indicates whether the property has a garden (1 for yes, 0 for no). |
  | Has_Pool | Indicates whether the property has a pool (1 for yes, 0 for no). |
  | Garage_Size | The size of the garage in square meters. |
  | Location_Score | A score from 0 to 10 indicating the quality of the neighborhood (higher scores indicate better neighborhoods). |
  | Distance_to_Center | The distance from the property to the city center in kilometers. |
  | Price | The target variable that represents the price of the property. This is the value we aim to predict.|


  **Objective**:
  The goal of this task is to develop a regression model that predicts the Price of a real estate property using the other features as inputs. The model should be able to learn the relationship between these features and the price, providing an accurate prediction for unseen data
    ''')
  df = pd.read_csv("sources/dataset.csv", index_col=False)
  st.dataframe(df)