import streamlit as st

#Creating a sidebar
with st.sidebar:
    st.subheader("Settings")
    api_key = st.text_input("API KEY", type="password")
    model = st.selectbox("Model", ["gpt-4", "gpt-5","gemini"])
 