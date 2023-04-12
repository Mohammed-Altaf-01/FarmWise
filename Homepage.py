import streamlit as st
import streamlit_lottie as st_lottie
from streamlit_extras.switch_page_button import switch_page
from util import *
st.set_page_config(
    page_title="Homepage-FarmWise",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""<html>
<body><h1 class="glow"> Farm Wise </h1></body>
</html>""", unsafe_allow_html=True)

st.markdown("""
<h2 style="color: #333; font-family: 'verdana', sans-serif; font-size: 30px; font-weight: bold; transition: color 0.1s ease-in-out;"
> <span style="display: inline-block; transition: color 0.3s ease-in-out;"
> A Bright Way To Grow Wise Crops </span> </h2>""", unsafe_allow_html=True)
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
        padding-right: 10px;
      }
    </style>
  </head>
  <body>
    <!-- Add an empty div to display the typewriter effect -->
    <div id="typewriter"></div>

    <!-- Add a script to create the typewriter effect -->
    <script>
      var text = "Farmers are the backbone of our society "; // Replace with your own text
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
st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 300px;
            }}
        </style>
    ''',
    unsafe_allow_html=True
)

st.image("images/Farmer-bro.png", width=300)
st.caption("We Live By Nature and We Preserve Nature")
# css styling applied to the page here :

with open('mainpage.css') as pgdesign:
    st.markdown(f"<style> {pgdesign.read()}</style>", unsafe_allow_html=True)

# hiding the side bar and appname at the bottom
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>

       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# css styling part ends here


# creating The tabs section for mainpage
tabs = ["Welcome", '***Developer***']
parts = st.tabs(tabs=tabs)


#        Welcome Tab Starts Here


# section 1 and the question 1 part
with parts[0]:

    q1, v1 = st.columns(2)
    with q1:
        st.markdown("<h3>Navigate Yourself Properly Using This Video Here 👉</h3>",
                    unsafe_allow_html=True)

        st.markdown('')
        st.markdown("""<p> This is the main page which has two tabs in it. The first Tab provides a guide to the user for proper navigation throught the interface
                    the second Tab has the details of the Developers who worked on creation of this WebPage. Scroll Down to more about the intresting stuff that is Waiting For YOU! 😊
                        </p>""", unsafe_allow_html=True)

        Loved_it = st.button("Click To Chill ❄ ")
        if Loved_it:
            st.snow()

        welcome_bot = lottie_load_json(
            'pages/lottie_json/hello_bot.json')
        st_lottie.st_lottie(welcome_bot, quality='ultrahigh', width=250)
    with v1:
        with open("homepage_vid/homepage.mp4", 'rb') as v:
            st.video(v)
    st.write('---')

    q2, v2 = st.columns(2)
    with q2:
        with open("homepage_vid//viz.mp4", 'rb') as v:
            st.video(v)

    with v2:
        st.markdown("<h3>Know The Current Trends In the Market Using Interactive Graphs 💹</h3>",
                    unsafe_allow_html=True)
        st.markdown("")
        st.markdown("""<p> The vizualization's page consist of line and bar graphs showing the growth and variation in the various sectors 
        as well as it's evolution over the years. You can also know the particular crop growth in a state by selecting your prefered values 
        The graphs are completely Interactive and you can zoom in and out on the go without any trouble.</p>""", unsafe_allow_html=True)
        viz = st.button('Try Vizuals Out ')
        if viz:
            switch_page("vizualizations")
        st.image("images/Q1.png", width=250)

    st.markdown('---')
    q3, v3 = st.columns(2)
    with q3:
        st.markdown("<h3>Know What Crops You should Prefer Growing Based On Soil Nutrients!🌱</h3>",
                    unsafe_allow_html=True)
        st.markdown("""<p> Based On your current location and your state you can know what type of crop is most suitable for your area, and if by chance 
        you wanna grow any other crop, simple name it and know what changes migh require to grow it in your filed without any effort🙅‍♂️</p>""", unsafe_allow_html=True)
        pr = st.button('GO Predict Without Trouble')
        if pr:
            switch_page('predictions')
    with v3:
        with open("homepage_vid/pred.mp4", 'rb') as v:
            st.video(v)
st_lottie.st_lottie(lottie_load_json(
    'pages/lottie_json//boygirl.json'))
#        Welcome Tab Ends Here


with parts[1]:
    st.markdown('Mohit Goud and Mohammed Altaf')
    st.markdown(
        'The Developers of This app belongs to Anurag University, Currently Pursuing there Third Year.   '
        "    From The Department of Mechanical Engineering! Curious Enthusiast's Wanna Do Something useful for the Society")

    co1, co2, co3, co4 = st.columns(4)

    with co1:
        # crating and adding github logo
        logo = lottie_load_json('pages/lottie_json/github.json')
        st_lottie.st_lottie(
            logo, loop=True, quality="high", width=90
        )
        st.markdown(
            '[Code!!](https://github.com/Mohammed-Altaf-01/gfg_hackathon-)')
    with co2:
        mail_logo = lottie_load_json('pages/lottie_json/gmail.json')
        st_lottie.st_lottie(mail_logo, loop=True, quality='high', width=90)
        mail_link = '<a href="mailto:20eg103319@anurag.edu.in">ClickHere</a>'
        st.markdown(mail_link, unsafe_allow_html=True)

    with co3:
        twitter_logo = lottie_load_json("pages/lottie_json//twitter.json")
        st_lottie.st_lottie(twitter_logo, loop=True, quality='high', width=100)
        st.markdown('[Tweet!!](https://twitter.com/_MohammedAltaf)')

    with co4:
        linkedln_logo = lottie_load_json('pages/lottie_json/linkedin.json')
        st_lottie.st_lottie(linkedln_logo, loop=True, width=100)
        st.markdown(
            '[Post](https://www.linkedin.com/in/mohammed-altaf-850b56259/)')

    st.markdown('---')
    st.caption('𝒜 𝒮𝒾𝓂𝓅𝓁𝑒  𝐵𝑜𝑜𝓈𝓉  𝒯𝑜   𝒪𝓊𝓇   𝐼𝓂𝒶𝑔𝒾𝓃𝒶𝓉𝒾𝑜𝓃')
