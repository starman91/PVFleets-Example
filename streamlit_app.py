import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os
from PIL import Image

local=True

#def main():


#Display banner
if local:
    #If using direct app, use image opener. ON Streamlit cloud just call directly
    dmt_image=Image.open('https://raw.githubusercontent.com/starman91/Iris-Example/main/images/logo-duramat-reversed-600.png')
    st.image(dmt_image)
else:
    st.image('https://raw.githubusercontent.com/starman91/Iris-Example/main/images/logo-duramat-reversed-600.png')

st.subheader("Hello Researcher")
    
values = construct_sidebar()

model.fit(x_train, y_train)
values_to_predict = np.array(values).reshape(1, -1)
values_to_predict = np.array(values).reshape(1, -1)
prediction = model.predict(values_to_predict)
prediction_str = iris_data.target_names[prediction[0]]
probabilities = model.predict_proba(values_to_predict)    

st.markdown(
    """
    <style>
    .header-style {
        font-size:25px;
        font-family:sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .font-style {
        font-size:20px;
        font-family:sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    '<p class="header-style"> Iris Data Predictions </p>',
    unsafe_allow_html=True
)

column_1, column_2 = st.columns(2)
column_1.markdown( f'<p class="font-style" >Prediction </p>', unsafe_allow_html=True )
column_1.write(f"{prediction_str}")

column_2.markdown( '<p class="font-style" >Probability </p>', unsafe_allow_html=True )
column_2.write(f"{probabilities[0][prediction[0]]}")

fig = plot_pie_chart(probabilities)
st.markdown( '<p class="font-style" >Probability Distribution</p>', unsafe_allow_html=True )
st.plotly_chart(fig, use_container_width=True)    
    
      
#if __name__ == '__main__':
    #main()
