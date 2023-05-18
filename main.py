import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_lottie as st_lottie
from streamlit_extras.switch_page_button import switch_page
from pages.static.util import *
st.set_page_config(
    page_title="Homepage-FarmWise",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""<html>
<body><h1 class="glow"> Farm Wise </h1></body>
</html>""", unsafe_allow_html=True)
st.markdown(f'''
    <style>
    section[data-testid="stSidebar"] .css-ng1t4o {{width: 2rem;}}
     section[data-testid="stSidebar"] .css-1d391kg {{width: 2rem;}}
    </style>
''',unsafe_allow_html=True)
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

st.image("pages/media/images/Farmer-bro.png", width=300)
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
animation_symbol = "❄"  # Load Animation
st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>


    """,
    unsafe_allow_html=True,
)


# css styling part ends here


# creating The tabs section for mainpage
selected = option_menu(None, ["Home", "About Us"], 
    icons=['house', "list-task"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={

        "icon": {"color": "green", "font-size": "5px"}, 
        "nav-link": {"font-size": "25px", "text-align": "center", "margin":"0px", "--hover-color": "#90EE90"},
        "nav-link-selected": {"background-color": "#171818"},
    }
)
# section 1 and the question 1 part
if selected == "Home":
    q1, v1 = st.columns(2)
    with q1: 
        st.markdown("<h3>Navigate Yourself Properly Using This Video Here 👉</h3>",
                    unsafe_allow_html=True)
        st.markdown('')
        st.markdown("""<p> This is the main page which has two tabs in it. The first Tab provides a guide to the user for proper navigation throught the interface
                    the second Tab has the details of the Developers who worked on creation of this WebPage. Scroll Down to know more about the intresting stuff that is Waiting For YOU! 😊
                        </p>""", unsafe_allow_html=True)

        Loved_it = st.button("Click To Chill ❄ ")
        if Loved_it:
            # if the button is clicked snow effects will occur 
            st.snow()
        welcome_bot = lottie_load_json(
            'pages/lottie_json/hello_bot.json')
        st_lottie.st_lottie(welcome_bot, quality='ultrahigh', width=250)
    with v1:
        with open("pages/media/homepage_vid//viz.mp4", 'rb') as v:
            st.video(v)
    st.write('---')


    q2, v2 = st.columns(2)
    with q2:
        with open("pages/media/homepage_vid/viz.mp4", 'rb') as v:
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
        st.image("pages/media/images/Q1.png", width=250)
    st.markdown('---')


    q3, v3 = st.columns(2)
    with q3:
        st.markdown("<h3>Know What Crops You should Prefer Growing Based On Soil Nutrients!🌱</h3>",
                    unsafe_allow_html=True)
        st.markdown("""<p> Based On your current location and your state you can know what type of crop is most suitable for your area, and if by chance 
        you wanna grow any other crop, simple name it and know what changes migh require to grow it in your field without any effort🙅‍♂️</p>""", unsafe_allow_html=True)
        pr = st.button('GO Predict Without Trouble')
        if pr:
            switch_page('predictions')
    with v3:
        with open("pages/media/homepage_vid/pred.mp4", 'rb') as v:
            st.video(v)
    st.markdown('---')


    q4, v4 = st.columns(2)
    with q4:
        with open("pages/media/homepage_vid/disease.mp4", 'rb') as v:
            st.video(v)
    with v4:
        st.markdown("<h3>Know What disease your crops have with just a pic 📸</h3>",
                    unsafe_allow_html=True)
        st.markdown("""<p>choose if you want to upload the picture or take a picture using the front camera or checkout the sample images then, click the button and wait for the suggesions
        the output is provided based on the highest probability of a disease in the leaf, create your way further based on these suggesions. Last but not least choose your language to read them perfectly</p>""", unsafe_allow_html=True)
        pr = st.button('Upload pic and click 🍂')
        if pr:
            switch_page('Disease_Detection')
    st.divider()

    q5,v5 = st.columns(2)
    with q5:
        st.markdown("<h3>Your personal Assistant ask him anything 🤖</h3>",
            unsafe_allow_html=True)
        st.markdown("""<p>Select the language you want to chat with your bot and ask a query in any language you answer will be in the specified language 
        by you. It provides stability and remove the language as a barrier for most of your tasks, and you can easily get your questions answerd within no time.</p>""", unsafe_allow_html=True)
        bot = st.button('Chat with your bot...')
        if bot:
            switch_page("FarmBot")
    with v5:
        with open("pages/media/homepage_vid/farmbot.mp4",'rb') as video:
            st.video(video)

#        Welcome Tab Ends Here


if selected == "About Us":
    st.markdown('**Mohit Goud and Mohammed Altaf**')
    st.markdown(
        'The Developers of This app belongs to Anurag University, Currently Pursuing there Third Year.   '
        "    From The Department of Mechanical Engineering! Curious Enthusiast's Wanna Do Something useful for the Society")

    co1, co2, co3, co4 = st.columns(4)

    with co1:
        # crating and adding github logo
        logo = lottie_load_json('pages/lottie_json/github.json')
        st_lottie.st_lottie(
            logo, loop=True, quality="high", width=350
        )
        st.markdown(
            '[Code!!](https://github.com/Mohammed-Altaf-01/gfg_hackathon-)')
    with co2:
        mail_logo = lottie_load_json('pages/lottie_json/gmail.json')
        st_lottie.st_lottie(mail_logo, loop=True, quality='high', width=280)
        mail_link = '<a href="mailto:20eg103319@anurag.edu.in" align :left>ClickHere</a>'
        st.markdown(mail_link, unsafe_allow_html=True)

    with co3:
        twitter_logo = lottie_load_json("pages/lottie_json//twitter.json")
        st_lottie.st_lottie(twitter_logo, loop=True, quality='high', width=300)
        st.markdown('[Tweet!!](https://twitter.com/_MohammedAltaf)')

    with co4:
        linkedln_logo = lottie_load_json('pages/lottie_json/linkedin.json')
        st_lottie.st_lottie(linkedln_logo, loop=True, width=350)
        st.markdown(
            '[Post](https://www.linkedin.com/in/mohammed-altaf-850b56259/)')

    st.markdown('---')
    st.caption('𝒜 𝒮𝒾𝓂𝓅𝓁𝑒  𝐵𝑜𝑜𝓈𝓉  𝒯𝑜   𝒪𝓊𝓇   𝐼𝓂𝒶𝑔𝒾𝓃𝒶𝓉𝒾𝑜𝓃')



st_lottie.st_lottie(lottie_load_json(
    'pages/lottie_json//boygirl.json'))