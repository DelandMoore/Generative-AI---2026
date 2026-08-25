from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np

uploaded_file = st.file_uploader("Choose a file", type = ["png","jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='uploaded image')