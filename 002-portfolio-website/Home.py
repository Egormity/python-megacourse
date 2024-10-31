import streamlit
import pandas

PATH = r"C:\Users\kotla\Desktop\python-megacourse\002-portfolio-website"

streamlit.set_page_config(layout="wide")

col1, col2 = streamlit.columns(2)

with col1:
    streamlit.image(f"{PATH}/images/photo.png")

with col2:
    streamlit.title("My boring App")
    streamlit.info("Hello, *World!* :sunglasses:")

col3, empty_col, col4 = streamlit.columns([1, 0.1, 1])

df = pandas.read_csv(f"{PATH}/data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        if index % 2 == 0: continue

        streamlit.header(row["title"])
        streamlit.write(row["description"])
        streamlit.image(f"{PATH}/images/{row['image']}")
        streamlit.write(f"[Source code]({row['url']})")
    
with col4:
    for index, row in df.iterrows():
        if index % 2 == 1: continue

        streamlit.header(row["title"])
        streamlit.write(row["description"])
        streamlit.image(f"{PATH}/images/{row['image']}")
        streamlit.write(f"[Source code]({row['url']})")