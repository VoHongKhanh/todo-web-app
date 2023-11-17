import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

st.title("About author")
st.subheader("Võ Hồng Khanh")
st.write("<a href='mailto:khanhvh.fpt@gmail.com'>khanhvh.fpt@gmail.com</a> # <a href='tel:0976755191'>0976 755 191</a>", unsafe_allow_html=True)

st.write("<hr/>", unsafe_allow_html=True)

# Start the camera
camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_image = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_image)

