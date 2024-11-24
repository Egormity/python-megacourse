import streamlit
from PIL import Image

image_from_camera = streamlit.camera_input("Take a picture", "camera")

if image_from_camera:
    img = Image.open(image_from_camera)
    gray_img = img.convert("L")
    streamlit.image(gray_img)