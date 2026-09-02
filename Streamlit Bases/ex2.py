import streamlit as st

with st.form("settings_form"):
    model = st.selectbox("Model", ["Claude", "gpt-2", "gemini-2"])
    max_response_lenght = st.slider("Maximum Response Lenght", 50, 100, 60)
    on = st.checkbox("Strict Factual Mode")
    

    submit = st.form_submit_button("SUBMIT")
if submit:
    st.write("Thank you for submitting")
    st.success(f"You selected the model {model} with max response lenght of {max_response_lenght}")