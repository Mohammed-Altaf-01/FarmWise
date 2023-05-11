import streamlit as st 
from pages.static.helper import *
from pages.static.util import *
import time
import streamlit as st

# from streamlit.ScriptRunner import RerunException
st.set_page_config(
    layout="wide", initial_sidebar_state="collapsed", page_icon="🤖")

if 'response' not in st.session_state:
    st.session_state.response = []
if "prompt" not in st.session_state:
    st.session_state.prompt = []
if 'counter' not in st.session_state:
    st.session_state.counter = 0 

def spinner():
    with st.spinner('Calling Your 🤖 ...'):
        time.sleep(2)
if len(st.session_state.prompt)==0:
    spinner()




prompt = st.text_input("**Ask your Questions**",max_chars=100,placeholder="How can I keep my field always healthy..")
if prompt:
    st.session_state.prompt.append(prompt)
    st.session_state.response.append("hi")
    st.session_state.counter += 1
    


    
if st.session_state.counter >= 2:
        for i in range(st.session_state.counter-1):
            st.write(st.session_state.prompt[i])
            st.write(st.session_state.response[i])
            st.divider()
elif st.session_state.counter == 1:
        st.write(st.session_state.prompt[0])
        st.write(st.session_state.response[0])
        st.divider()
if len(st.session_state.prompt) > 5:
    st.session_state.prompt  = []
    st.session_state.response = []
    st.session_state.counter = 0
   