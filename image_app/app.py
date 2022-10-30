from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="Image App",
    page_icon="📷",
    layout="wide"
)

st.title("image processing app")
st.sidebar.header("select image file")
image_file=st.sidebar.file_update("upload image",type=["png","jpg","jpeg"])
if image_file is not None:
    image=Image.open(image_file)
    st.image(images,caption=image_file.name)
