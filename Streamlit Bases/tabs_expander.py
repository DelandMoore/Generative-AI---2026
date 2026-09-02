import streamlit as st

tab1, tab2 = st.tabs(["Chat", "Research"])


with tab1:
    st.write("Chatting is happening here")
    #simply put the logic under here
    
with tab2:
    st.write("Model settings go here")
    
    
with st.expander("Show agent search results"):
    st.write("put the content researched by the agent")