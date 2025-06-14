# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yVDzNjRPQa2apbMobR9SFKu_xpvkTONV
"""

# prompt: give me a code to load data csv from google drive

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

csv_file_path = '/content/drive/My Drive/diabetes.csv' # Replace with your file path
df = pd.read_csv(csv_file_path)
print(df.head())



# prompt: berikan saya code untuk menampilkan data tersebut pada streamlit

import streamlit as st
import pandas as pd

# Assumes the DataFrame df is already loaded in your Colab environment
# If not, include the Colab file loading code here:
# from google.colab import drive
# drive.mount('/content/drive')
# csv_file_path = '/content/drive/My Drive/diabetes.csv'
# df = pd.read_csv(csv_file_path)

# Display the DataFrame using Streamlit
st.title('Diabetes Dataset')
st.write("Here is the first few rows of the dataset:")
st.dataframe(df)
