from pages.static.helper import *
import streamlit as st
import re
from pages.static.util import Retreiving_Details
from PIL import ImageOps, Image
from matplotlib import pyplot as plt
import time
import io

# configuring the page and adding the custom css layout
st.set_page_config(
    layout="wide", initial_sidebar_state="collapsed", page_icon="🍁")
with open('pages/pages_StyleSheet.css') as pgdesign:
    st.markdown(f"<style> {pgdesign.read()}</style>", unsafe_allow_html=True)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
if "counter" not in st.session_state:
    st.session_state.counter = 1

if st.session_state.counter ==1:
    spinner()
    st.session_state.counter += 1

# adding header to our page
st.markdown("""
<h1 style="color: #333; font-family: 'Comic Sans MS', sans-serif; font-size: 35px; font-weight: bold; transition: color 0.1s ease-in-out;"
><span style="display: inline-block; transition: color 0.3s ease-in-out;"
>HEALTHY OR NOT  </span>🤔</h1>
""", unsafe_allow_html=True)

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

        white-space: nowrap;
        overflow: hidden;
        border-right: 1px solid black;
        padding:0;
      }
    </style>
  </head>
  <body>
    <!-- Add an empty div to display the typewriter effect -->
    <div id="typewriter"></div>

    <!-- Add a script to create the typewriter effect -->
    <script>
      var text = "To know weather If your plants are healthy or not upload or click a pick of Leaf🍀 "; // Replace with your own text
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

# ---
st.write('---')


st.markdown("If you want to upload image,click on Upload button below else Choose the available example images give below and don't forget to choose your language below 😊")

col1,col2 = st.columns(2)
with col1:
  saved_images = st.radio("**Select Type**",['Diseased Example','healthy Example','upload','Take a picture','Generate Image'],index=2,horizontal=True)

  match saved_images: 
        case "upload":
            image = st.file_uploader(
            label='Click to Upload an Image 📸')
            if image != None:
              probability = prediction(Image.open(image))
            
        case "Take a picture":
          co1, col2, col3 = st.columns([1, 2, 1])
          col2.markdown(
        '***make sure the image is taken clearly with less background noise if possible***')
          image = col2.camera_input('click to take a picture of the leaf')
            
        case "Diseased Example":
            image = "pages/media/images//apple_scab_disease.JPG"
            probability = prediction(Image.open(image))
        case "healthy Example":
            image = "pages/media/images/healthy.JPG"
            probability = prediction(Image.open(image))
        case "Generate Image":
            prompt = st.text_input("write the description of the Disease!",max_chars=55,placeholder="Example Prompt -->  tomato leaf with black spots on it ")
            if prompt and PromptChecker(prompt):
              image_bytes = StableDiffusion({
	              "inputs": prompt, 
                      })
              image = io.BytesIO(image_bytes)
              probability = prediction(Image.open(image))
            elif PromptChecker(prompt) == False:
                st.warning("Please enter a proper prompt explaining your need!",icon="🛑")
                image = None 
            else:
                image = None 


with col2:
    language_conversion =st.radio("***Choose your language ?***",('English','हिंदी','తెలుగు','தமிழ்','ਪੰਜਾਬੀ','اردو',"ଓଡିଆ"),horizontal=True)

    
if image != None:  # another condition for pic
    view = Image.open(image)
    st.image(image, caption='uploaded Image👆')
    with open('pages/datasets/labels.txt', 'r') as file:
        label = list(file)[probability]
        stripped = re.sub("___|_|__", " ", label)

       # calling the function before the actual button is clicked to improve speed

    button = st.button('Predict')
    if button:
        if 'healthy' in stripped:
                st.write(translation('Your crops are healthy no need to worry,here are few tips to keep your crops and Plants healthy ',language_conversion))
                tips = translation(tips(),language_conversion)
                st.write(tips)
        else:
            lst = stripped.split(' ')
            if len(lst) == 3 or len(lst) == 2:
                text = f'Your crop might have a disease {lst[-1]}'
                st.write(translation(text,language_conversion))
                val = f"disease {lst[-1]}"

            elif len(lst) == 4:
                text = f'Your crop might have a disease {lst[-3]} {lst[-2]} {lst[-1]}'
                st.write(translation(text,language_conversion))
                val = f"disease {lst[-3]} {lst[-2]} {lst[-1]}"
            progress_bar_text = translation("Please wait! We Appreciate Your Patience",language_conversion)
            bar = st.progress(
                2, text=f"💖 {progress_bar_text}")

            # retreiving the api call here 
            question = []
            question.append(
                {'role': 'system',
                 'content': f"how to cure leaf disease named as  {val}"})
            question = Retreiving_Details(question)

            # loading the progress bar after calling api 
            for percent_complete in range(100):
                time.sleep(0.01)
                bar.progress(percent_complete, text=f"💖 {progress_bar_text}")
            subheader_text =f"To Cure {val} Follow Below Tips" 
            st.subheader(f"{translation(subheader_text,language_conversion)} 👇")


            # # adding this in the drop down  for better readibility
            generated_text ='{0}\n'.format(question[-1]['content'].strip()) 
            st.write(translation(generated_text,language_conversion))
            
        st.write('---')
        




# train another model to predict leaf or note using existing data