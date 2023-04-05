import streamlit as st
import pickle
import pandas as pd
import numpy as np
import openai
from util import ChatGPT_conversation
import time


with open('pages\static\custom_homepage.css') as pgdesign:
    st.markdown(f"<style> {pgdesign.read()}</style>", unsafe_allow_html=True)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# getting the model and loading it
prediction = pickle.load(open("pages\\static\\NavieBayes.pkl", "rb"))
# reading the csv file
df_pred = pd.read_csv('pages\static\crop_recommendation.csv')
columns = df_pred.columns[0:6]
st.markdown("""
<h1 style="color: #333; font-family: 'Comic Sans MS', sans-serif; font-size: 35px; font-weight: bold; transition: color 0.1s ease-in-out;"
>My <span style="display: inline-block; transition: color 0.3s ease-in-out;"
>Know What To Grow</span>🌾</h1>
""", unsafe_allow_html=True)
with open("pages\static\\vizcss.css") as h:
    st.markdown(f"<style> {h.read()}</style>", unsafe_allow_html=True)
st.markdown("***Make Sure To Enter The Ratio's Between The Values*** :smile: ")
st.markdown("<a href=https://www.gardeningknowhow.com/garden-how-to/soil-fertilizers/fertilizer-numbers-npk.htm>Example</a>", unsafe_allow_html=True)

val1, val2 = st.columns(2)
with val1:
    n = st.number_input(
        "**Nitrogen**", min_value=df_pred['N'].min(), max_value=df_pred['N'].max())
    k = st.number_input('**Potassium**',
                        min_value=df_pred['K'].min(), max_value=df_pred['K'].max())

with val2:
    p = st.number_input('**Phosphorus**', min_value=df_pred['P'].min(),
                        max_value=df_pred['P'].max())
    type_crop = st.text_input('**Crop You Want To Grow**',
                              max_chars=20, placeholder='Optional', key="crop_type")

button = st.button('Predict')

if (k or p) == 0 or n < 0:
    st.warning('Please fill all the Values! :fire:')
else:
    if button:
        # to run a progress bar and make the app asthetic
        st.balloons()

        # we need 7 features as input - got 3 from user taking other inputs as random each time submit is clicked
        temperature = df_pred['temperature'].sample(
            random_state=np.random.randint(0, high=len(df_pred['temperature'])))
        ph = df_pred['ph'].sample(
            random_state=np.random.randint(0, high=len(df_pred['ph'])))
        humidity = df_pred['humidity'].sample(
            random_state=np.random.randint(0, high=len(df_pred['humidity'])))
        rainfall = df_pred['rainfall'].sample(
            random_state=np.random.randint(0, high=len(df_pred['rainfall'])))
        values = np.array([[n, p, k, temperature, ph, humidity, rainfall]])

        if type_crop:  # optional parameter to grow the crop is given by the user then this condition is True
            bar = st.progress(2, text=":heart: Please wait!")
            # call the api here and let it load until the bar is finished then print it later
            question = []
            question.append(
                {'role': 'system',
                 'content': f"What should I do If I want to Grow {type_crop} in my farm in India,\
                  with the values of fertilizer's of proportions as nitrogen:**{n}**,phosphorus:**{p}**,and pottasium:**{k}**?"})
            question = ChatGPT_conversation(question)
            for percent_complete in range(100):
                time.sleep(0.0001)
                bar.progress(percent_complete, text=":heart: Please wait!")
            st.subheader(type_crop)
            # # adding this in the drop down  for better readibility
            st.write('{0}\n'.format(
                question[-1]['content'].strip()))

        else:
            prediction = prediction.predict(values)
            crop = ''.join([val for val in prediction])
            st.subheader(
                f':smile: Your Farm is Suitable for Growing {crop}')
