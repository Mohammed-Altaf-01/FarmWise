import streamlit as st
import streamlit_lottie as st_lottie
from util import *


with open('mainpage.css') as pgdesign:
    st.markdown(f"<style> {pgdesign.read()}</style>", unsafe_allow_html=True)

st.title('FarmWise')
st.caption('A Bright Way To Grow Wise Crops')
st.image("images\Farmer-bro.png", width=300)
st.caption("We Live By Nature and We Preserve Nature")


# creating The tabs section for mainpage
tabs = ["Welcome", '***Developer***']
parts = st.tabs(tabs=tabs)


#        Welcome Tab Starts Here


# section 1 and the question 1 part
with parts[0]:
    st.markdown(' ***Questions We Solve!***')
    q1, q2 = st.columns(2)
    with q1:
        st.markdown(
            ' **What are the Trends of Farming by Using Interactive Plots?**')
        st.markdown(
            'You can use the Graphs Section to Know the Growth of the farming.')
    with q2:
        welcome_bot = lottie_load_json(
            'pages\lottie_json\hello_bot.json')
        st_lottie.st_lottie(welcome_bot, quality='ultrahigh', width=250)

    # question 2
    q3, q4 = st.columns(2)
    with q3:
        st.image("images\Q1.png", width=250)
    with q4:
        st.markdown(
            "**Wanna Know What The Future Of Your Crops Would Be?**")
        st.markdown(
            "Help You With Predictions Based On Your Soil's Health and It's Location")


st_lottie.st_lottie(lottie_load_json(
    'pages\lottie_json\\boygirl.json'))
#        Welcome Tab Ends Here


with parts[1]:
    st.markdown('Mohit Goud and Mohammed Altaf')
    st.markdown(
        'The Developers of This app belongs to Anurag University, Currently Pursuing there Third Year.   '
        "    From The Department of Mechanical Engineering! Curious Enthusiast's Wanna Do Something useful for the Society")

    co1, co2, co3, co4 = st.columns(4)

    with co1:
        # crating and adding github logo
        logo = lottie_load_json('pages\lottie_json\github.json')
        st_lottie.st_lottie(
            logo, loop=True, quality="high", width=90
        )
        st.markdown('[Code!!](www.github.com)')
    with co2:
        mail_logo = lottie_load_json('pages\lottie_json\gmail.json')
        st_lottie.st_lottie(mail_logo, loop=True, quality='high', width=90)
        mail_link = '<a href="mailto:20eg103319@anurag.edu.in">ClickHere</a>'
        st.markdown(mail_link, unsafe_allow_html=True)

    with co3:
        twitter_logo = lottie_load_json("pages\lottie_json\\twitter.json")
        st_lottie.st_lottie(twitter_logo, loop=True, quality='high', width=100)
        st.markdown('[Tweet!!](https://twitter.com/_MohammedAltaf)')

    with co4:
        linkedln_logo = lottie_load_json('pages\lottie_json\linkedin.json')
        st_lottie.st_lottie(linkedln_logo, loop=True, width=100)
        st.markdown(
            '[Post](https://www.linkedin.com/in/mohammed-altaf-850b56259/)')

    st.markdown('---')
    st.caption('𝒜 𝒮𝒾𝓂𝓅𝓁𝑒  𝐵𝑜𝑜𝓈𝓉  𝒯𝑜   𝒪𝓊𝓇   𝐼𝓂𝒶𝑔𝒾𝓃𝒶𝓉𝒾𝑜𝓃')
