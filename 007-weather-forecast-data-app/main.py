import streamlit as st
import pandas as pd
import plotly.express as px
from backend import get_data

st.title("Weather Forecast")
place = st.text_input("Place: ")
days_amount = st.slider("Days: ", min_value=1, max_value=5, value=3, step=1, help="Number of days to forecast")

option = st.selectbox("Data to view: ", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days_amount} days")

if place:
    try:
        data = get_data(place, days_amount, option)

        if (option == "Temperature"):
            figure = px.line(x=data["days"], y=data["temp"], labels={"x": "Day", "y": option})
            st.plotly_chart(figure)

        if (option == "Sky"):
            paths = []
            for condition in range(data["sky"]):
                path.append(f"007-weather-forecast-data-app\images\clear{condition}.png")
            st.image(paths, width=120)
    except: KeyError
        st.write(f"The place '{place}' is invalid")