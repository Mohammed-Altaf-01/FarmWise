import streamlit as st 
from pages.static.helper import *
from pages.static.util import *
import time
import streamlit as st

st.set_page_config(
    layout="wide", initial_sidebar_state="auto", page_icon="🤖")

st.components.v1.html("""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Typewriter Effect</title>
    <style>
      /* Add some basic styling */
      #typewriter {
        font-family: 'Courier New', monospace;
        font-size: 24px;
        text-align: center;
	    font-weight: bold;
        color: #8BC34A;
       width:"100%" 
       border:"0" 
       cellspacing:"0" 
       cellpadding:"0"
        
      }
    </style>
  </head>
  <body>
    <!-- Add an empty div to display the typewriter effect -->
    <div id="typewriter"></div>

    <!-- Add a script to create the typewriter effect -->
    <script>
      var text = "Hi I'am and AI bot Here to Solve your Agriculture Related Queries "; // Replace with your own text
      var i = 0;
      var speed = 90; // Adjust typing speed in milliseconds

      function typeWriter() {
        if (i < text.length) {
          document.getElementById("typewriter").innerHTML += text.charAt(i);
          i++;
          setTimeout(typeWriter, speed);
        }
      }

      // Call the typeWriter function when the page loads
      window.onload = function() {
        typeWriter();
      };
    </script>
  </body>
</html>
""")
st.divider()

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


col1,col2 = st.columns([2, 1]) 
with col1:
    with st.form(key="my-form",clear_on_submit=True):
        prompt = st.text_input("**Ask your Questions**",max_chars=85,placeholder="How can I keep my field always healthy..")
        submit1 =  st.form_submit_button("**ASK**")
with col2:
    with st.form(key="language-form"):
        language = st.selectbox("Select Your Language",('English','हिंदी','తెలుగు','தமிழ்','ਪੰਜਾਬੀ','اردو',"ଓଡିଆ"))
        submit2 =  st.form_submit_button("**change language**")
        





if submit1:
    if PromptChecker(prompt):
        response_prompt = prompt+" answer me in less than 200 words"
        response_prompt = Retreiving_Details(response_prompt)
        response_prompt=translation('{0}\n'.format(response_prompt[-1]['content'].strip()),language)
        st.write(translation(response_prompt,language))
        st.session_state.prompt.append(prompt)
        st.session_state.response.append(response_prompt)
        st.session_state.counter += 1
        st.divider()
    else:
        st.warning("Please Ask an Agriculture Related Question",icon="🌱")


    
if st.session_state.counter >= 2:
        for i in range(st.session_state.counter-1):
            st.caption(f"{i} - Question and it's Response ")
            st.markdown(f"<h3>{st.session_state.prompt[i]}</h3>",unsafe_allow_html=True)
            st.markdown(f"<h7>{st.session_state.response[i]}</h7>",unsafe_allow_html=True)
            st.divider()


if len(st.session_state.prompt) > 5:
    st.session_state.prompt  = []
    st.session_state.response = []
    st.session_state.counter = 0

# this is not wormkking we have to use session state 
