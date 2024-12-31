import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def homepage():
  df = pd.read_csv('sources/dataset.csv')
  header(df)
  distribution(df)
  relaiton(df)
  descriptive(df)
  correlation(df)


def header(df):
  col_header_1, col_header_2, col_header_3 = st.columns(3)
  with col_header_1:
    st.button(f"{len(df.to_numpy())} Total Data", use_container_width=True)
  with col_header_2:
    st.button(f"{len(df[df['Price'] > 500000].to_numpy())} House above 500000$", use_container_width=True)
  with col_header_3:
    st.button(f"{len(df[df['Price'] <= 500000].to_numpy())} House under 500000$", use_container_width=True)
def relaiton(df):
  st.subheader("Relation Between Feature")
  columns = df.columns
  col_relation_1, col_relation_2 = st.columns(2)
  with col_relation_1:
    feature_1 = st.selectbox("", columns, key="feature_1")
  with col_relation_2:
    feature_2 = st.selectbox("", columns, key="feature_2")
  st.scatter_chart(data=df, x=feature_1, y=feature_2)
def descriptive(df):
  st.subheader("Descriptive Analysis")
  st.dataframe(df.describe())
def correlation(df):
  st.subheader("Correlation")
  fig, ax = plt.subplots()
  sns.heatmap(df.corr(), ax=ax, annot=False, cmap="YlGnBu")
  st.write(fig)
def distribution(df):
  above_2000 = df[df['Year_Built'] >= 2000]
  under_2000 = df[df['Year_Built'] < 2000]
  has_pool = df[df['Has_Pool'] == 1]
  hasnt_pool = df[df['Has_Pool'] == 0]
  has_garden = df[df['Has_Garden'] == 1]
  hasnt_garden = df[df['Has_Garden'] == 0]


  st.subheader("Distribution")
  col1, col2, col3 = st.columns(3)
  with col1:
    fig, ax = plt.subplots()
    year_categories = ['Year >= 2000', 'Year < 2000']
    year_values = [len(above_2000), len(under_2000)]
    ax.bar(year_categories, year_values, color=['blue', 'orange'])
    ax.set_title('Comparison of Total Values')
    ax.set_xlabel('Year Category')
    ax.set_ylabel('Total Value')
    st.pyplot(fig)

  with col2:
    fig, ax = plt.subplots()
    pool_categories = ['Has pool', 'No pool']
    pool_values = [len(has_pool), len(hasnt_pool)]
    ax.bar(pool_categories, pool_values, color=['blue', 'orange'])
    ax.set_title('Comparison of Total Values')
    ax.set_xlabel('Has pool/not')
    ax.set_ylabel('Total Value')
    st.pyplot(fig)

  with col3:
    fig, ax = plt.subplots()
    garden_categories = ['Has garden', 'No garden']
    garden_values = [len(has_garden), len(hasnt_garden)]
    ax.bar(garden_categories, garden_values, color=['blue', 'orange'])
    ax.set_title('Comparison of Total Values')
    ax.set_xlabel('Has garden/not')
    ax.set_ylabel('Total Value')
    st.pyplot(fig)
