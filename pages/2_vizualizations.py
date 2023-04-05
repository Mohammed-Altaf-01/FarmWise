import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
st.set_page_config(layout="wide")

with open('static/custom_homepage.css') as pgdesign:
    st.markdown(f"<style> {pgdesign.read()}</style>", unsafe_allow_html=True)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# 3 datasets for graphs
df_gdp = pd.read_csv('pages/datasets/GDP.csv')
df_prices = pd.read_csv('pages/datasets/Prices.csv')
df_yield = pd.read_csv('pages/datasets//raw_districtwise_yield_data.csv')
df_gdp_columns = df_gdp.columns
df_price_columns = df_prices.columns


# heading of our page
st.markdown("""
<h1 style="color: #333; font-family: 'Comic Sans MS', sans-serif; font-size: 35px; font-weight: bold; transition: color 0.1s ease-in-out;"
>My <span style="display: inline-block; transition: color 0.3s ease-in-out;"
>Know the Trends and Patterns in the Indian Agriculture Market!!</span> 📈</h1>
""", unsafe_allow_html=True)
with open("pages/static//vizcss.css") as h:
    st.markdown(f"<style> {h.read()}</style>", unsafe_allow_html=True)
st.write('---')


# dividing and working with columns on our page
col1, col2 = st.columns(2)
with col1:
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

    st.write(fig)
    st.write(fig4)


with col2:
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
    st.write(fig2)
    st.write(fig3)

# figures end here
