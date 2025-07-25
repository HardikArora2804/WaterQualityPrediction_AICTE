
import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st

model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")
 
st.title("water pollutants predictor")
st.write("predict the water pollutants based on year and station id")
 
year_input = st.number_input("enter year", min_value=2000, max_value=2100,value=2022)
station_id= st.text_input("enter station id",value='1')

if st.button('predict'):
     if not station_id:
      st.warning('please enter the staion id')
     else:
      input_df = pd.DataFrame({'year': [year_input],'id':[station_id]})
      input_encoded =pd.get_dummies(input_df, columns=['id'])
 
      for col in model_cols:
            if col not in input_encoded.columns:
               input_encoded[col]=0
      input_encoded = input_encoded[model_cols]
 
      predicted_pollutants= model.predict(input_encoded)[0]
      pollutants = ['O2','NO3','NO2','S04','PO4','CL']

      st.subheader(f"predicted pollutant levels for the station '{station_id}' in {year_input}:")
      predicted_values= {}
      for p, val in zip(pollutants,predicted_pollutants):
         st.write(f'{p} : {val:.2f}')