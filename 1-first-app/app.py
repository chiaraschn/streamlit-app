# SETUP

import streamlit as st
import pandas as pd


#-------------------
# CREATE DATA

# Simple dataframe
df = pd.DataFrame({
    'A': [1, 4, 3, 2],
    'B': [10, 20, 30, 40]
    })

#-------------------
# START OF APP

#-------------------
# HEADER

st.title('Meine erste App')

# Add header
st.header("Mein Header")
# Add a gif from https://giphy.com/
st.markdown("![Frau](https://media.giphy.com/media/i2n8MdobrFTFiUkyxg/giphy.gif)")

#st.image('hdm-logo.jpg')
#-------------------
# BODY

#-------------------
# Show static DataFrame
st.dataframe(df)

#-------------------
# Bar chart
st.bar_chart(df)

# SIDEBAR

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"))


#WIDGET

age = st.sidebar.slider('How old are you?', 0, 130, 25)
st.sidebar.write("I'm ", age, 'years old')

from datetime import datetime
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)