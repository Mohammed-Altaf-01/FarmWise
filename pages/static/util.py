import requests
import openai
import os
import json
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


@st.cache_data
def lottie_load_json(filepath: str):
    '''
    This function is used to load the json GIFs using file paths as only parameter
    '''
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)

@st.cache_resource
# system assistant and user there will be 3 roles.
def Retreiving_Details(conversation):
    apikey =  os.getenv("API_KEY") or st.secrets["API_KEY"] 
    openai.api_key = apikey
    model = 'gpt-3.5-turbo'
    response = openai.ChatCompletion.create(
        model=model,
        messages=conversation
    )
    conversation.append(
        {'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation
