import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time 
import plotly.graph_objects as go
st.set_page_config(
    layout="wide", initial_sidebar_state="auto", page_icon="📽")


with open('pages/pages_StyleSheet.css') as pgdesign:
    st.markdown(f"<style> {pgdesign.read()}</style>", unsafe_allow_html=True)
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


def spinner():
    with st.spinner('Loading Please wait ...'):
      time.sleep(3)
if "counter" not in st.session_state:
    st.session_state.counter = 1

if st.session_state.counter ==1:
    spinner()
    st.session_state.counter += 1
# heading of our page
st.markdown("""
<h1 style="color: #333; font-family: 'Comic Sans MS', sans-serif; font-size: 35px; font-weight: bold; transition: color 0.1s ease-in-out;"
> <span style="display: inline-block; transition: color 0.3s ease-in-out;"
>Know the Trends and Patterns in the Indian Agriculture Market!!</span> 📈</h1>
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
      var text = "Select Corresponding State's and There District's "; // Replace with your own text
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


# 3 datasets for graphs
df_gdp = pd.read_csv('pages/datasets/GDP.csv')
df_prices = pd.read_csv('pages/datasets/Prices.csv')
df_yield = pd.read_csv('pages/datasets//raw_districtwise_yield_data.csv')
df_gdp_columns = df_gdp.columns
df_price_columns = df_prices.columns


st.write('---')
# dividing and working with columns on our page
col1, col2 = st.columns([2,2])
with col2:

        state = st.selectbox(label='***Select the Indian State*** 👇',
                             options=df_gdp['State Name'].unique())
        a = df_gdp['State Name'] == state
        dist = df_gdp.loc[a, 'Dist Name']
        dist = st.selectbox(label='***Select The District***',
                            options=dist.unique())
        sector = st.selectbox(label='***Select The Sector***',
                              options=df_gdp_columns[5:],)

    # plotting the figure ..
        flush = df_gdp['Dist Name'] == dist
        new_df = df_gdp.loc[flush, ['Year', sector, 'State Name']]
        fig = px.line(new_df, x='Year',
                  y=sector, color='State Name', title=f'{sector} in {dist}')
        fig4 = px.bar(new_df, x='Year', y=sector)
        fig.update_traces(line_color='purple')
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        st.plotly_chart(fig4, theme="streamlit", use_container_width=True)


with col1:
    price_state = st.selectbox(label='***Select the Indian State*** 👇',
                               options=df_prices['State Name'].unique(), key='StatePrices')
    dist_price = df_prices['State Name'] == price_state
    dist_price = st.selectbox(
        label='***Select The District***', options=df_prices.loc[dist_price, "Dist Name"].unique(), key="distprice")
    crop = st.selectbox(label="Select The Crop🌾",
                        options=df_price_columns[5:])
    flush = df_prices['Dist Name'] == dist_price
    price_df = df_prices.loc[flush, ['Year', crop, 'State Name']]
    fig2 = px.line(price_df, x='Year', y=crop, color="State Name",
                   title=f"{crop} in {dist_price}")
    fig3 = px.bar(price_df, x='Year', y=crop)

    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)

# figures end here


# creating map using stereamlit

# df_map = pd.read_excel('pages//altitude.xlsx')
# fig_map = px.scatter_mapbox(
#     df_map, lat="Latitude", lon="Longitude", color_discrete_sequence=["fuchsia"], zoom=3, height=500)


# fig_map.update_layout(mapbox_style="open-street-map")
# fig_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# st.plotly_chart(fig_map, theme='streamlit', use_container_width=True)
