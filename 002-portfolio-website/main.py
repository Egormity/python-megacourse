import streamlit as st

PATH = r"C:\Users\kotla\Desktop\python-megacourse\002-portfolio-website\images"

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(f"{PATH}/photo.png")

with col2:
    st.title("My boring App")
    st.info("Hello, *World!* :sunglasses:")

st.write('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')