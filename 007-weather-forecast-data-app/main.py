import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.title("Weather Forecast")
place = st.text_input("Place: ")
days_amount = st.slider("Days: ", min_value=1, max_value=5, value=3, step=1, help="Number of days to forecast")

option = st.selectbox("Data to view: ", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days_amount} days")

figure = px.line(x=[1 + i for i in range(days_amount)], y=[random.random() * 10 for i in range(days_amount)], labels={"x": "Day", "y": option})
st.plotly_chart(figure)