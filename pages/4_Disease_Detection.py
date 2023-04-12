from pages.static.helper import prediction, tips
import streamlit as st
import re
from util import Retreiving_Details
from PIL import ImageOps, Image
from matplotlib import pyplot as plt
import time

# configuring the page and adding the custom css layout
st.set_page_config(
    layout="wide", initial_sidebar_state="collapsed", page_icon="🍁")
with open('pages/static/custom_homepage.css') as pgdesign:
    st.markdown(f"<style> {pgdesign.read()}</style>", unsafe_allow_html=True)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# adding header to our page
st.markdown("""
<h1 style="color: #333; font-family: 'Comic Sans MS', sans-serif; font-size: 35px; font-weight: bold; transition: color 0.1s ease-in-out;"
><span style="display: inline-block; transition: color 0.3s ease-in-out;"
>HEALTHY OR NOT  </span>🤔</h1>
""", unsafe_allow_html=True)
with open("pages/static//vizcss.css") as h:
    st.markdown(f"<style> {h.read()}</style>", unsafe_allow_html=True)
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

selection = st.selectbox('**Click to Select the Type of Configuration** ',
                         options=['Upload', 'Take a Picture'])

if selection == 'Upload':
    image = st.file_uploader(
        label='Click to Upload an Image 📸 ')
    if image != None:
        probability = prediction(Image.open(image))


else:
    co1, col2, col3 = st.columns([1, 2, 1])
    col2.markdown(
        '***make sure the image is taken clearly with less background noise if possible***')
    image = col2.camera_input('click to take a picture of the leaf')
    if image:
        probability = prediction(Image.open(image))

if image != None:  # another condition for pic
    view = Image.open(image)
    st.image(image, caption='Your uploaded Image👆')
    with open('pages/labels.txt', 'r') as file:
        label = list(file)[probability]
        stripped = re.sub("___|_|__", " ", label)

        # calling the function before the actual button is clicked to improve speed

    button = st.button('Predict')
    if button:
        if 'healthy' in stripped:
            st.write(
                'Your crops are healthy no need to worry,here are few tips to keep your crops and Plants healthy ')
            st.write(tips())

        else:
            lst = stripped.split(' ')
            if len(lst) == 3 or len(lst) == 2:
                st.write(f'Your crop might have a disease {lst[-1]}')
                val = f"disease {lst[-1]}"

            elif len(lst) == 4:
                st.write(
                    f'Your crop might have a disease {lst[-3]} {lst[-2]} {lst[-1]}')
                val = f"disease {lst[-3]} {lst[-2]} {lst[-1]}"
            bar = st.progress(
                2, text=":heart: Please wait! **We Appreciate Your Patience**")
    # call the api here and let it load until the bar is finished then print it later
            for percent_complete in range(100):
                time.sleep(0.001)
                bar.progress(percent_complete, text=":heart: Please wait!")
            question = []
            question.append(
                {'role': 'system',
                 'content': f"what should be done to get rid of leaf {val}"})
            question = Retreiving_Details(question)

            st.subheader(val)
            # # adding this in the drop down  for better readibility
            st.write('{0}\n'.format(
                question[-1]['content'].strip()))


# train another model to predict leaf or note using existing data
