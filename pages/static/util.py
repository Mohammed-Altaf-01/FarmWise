# third party imports 
import speech_recognition as sr  
import pyttsx3 
import openai
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# built-in imports 
import requests
import os
import json


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
    '''
    The function takes in a prompt as input and output will be the answer from the gpt-3.5 turbo api

    '''
    question = []
    question.append({'role': 'system','content':conversation })
    conversation = question
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


  
def AudioInput(language):
    lang_dict = {'हिंदी':'Hindi','ਪੰਜਾਬੀ':'Punjabi',"తెలుగు":'Telugu',"தமிழ்":"Tamil","اردو":'Urdu','English':'English'}
    languages_key__dict = {'Hindi':"hi-IN",'Telugu':"te-IN","English":"en-IN","Tamil":"ta-IN","Punjabi":"pa-Guru-IN","Urdu":"ur-IN","Bengali":"bn-BD","Marathi":"mr-IN"}
    speech_lang = lang_dict[language] #get specified language
    speech_lang = languages_key__dict[speech_lang]  # get key for that language
    r = sr.Recognizer() # initializing speech recognition class
    with sr.Microphone() as source:
        # seconds of non-speaking audio before 
        # a phrase is considered complete
        # replace with st.write and add translation with 'please start speaking !'
        st.write(f"Please Speak in {lang_dict[language]}")
        st.write("Listening....")
        r.pause_threshold = 0.7  
        # r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)  
        try:
            st.write("Processing")
            Query = r.recognize_google(audio, language=speech_lang )
        
        # handling the exception, so that assistant can 
        # ask for telling again the command
        except Exception as e:
            st.write("Say that again sir")
            return "None"
        return Query
  
  


