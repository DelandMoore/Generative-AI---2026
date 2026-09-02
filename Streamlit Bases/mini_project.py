import streamlit as st
with st.form("settings_form"):
    student_name = st.text_input("Enter your name")
    topics_understood = st.multiselect("Select the topics that you have a clear understnding", ["Deep Learning", "Machine Learning", "LLMs"])
    module_rating = st.slider("Module Rating", 1, 5, 2)
    feedback = st.text_area("Give us a brief description about your journey so far")
    

    submit = st.form_submit_button("SUBMIT")
if submit:
    st.markdown(f"My name is {student_name}. The topic(s) i understood best is/are {topics_understood} with an overall rating of {module_rating}. Here is a feedback of my journey so far: {feedback} ")