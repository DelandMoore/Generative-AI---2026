# #What is streamlit: It's a UI library used to build AI applications
# #Saving: house_price.pkl [a normal user does not understand]

# import streamlit as st

# #Rendering: draw unto our canvas(browser, mobile app):
# st.title("Banking AI Agent")

# # take the user input and welcome the user to the course
# name = st.text_input("What is your name")

# if name:
#     st.write(f"Welcome {name} to this amazing course")


# # Exercise 1: Create a file called ex1.py and write an app that tell

import streamlit as st

names = ("john","paul", "romeo")
#what is tuple  unpacking
#name1, name2, name3 = names

col1, col2=st.columns(2)
print(f"col1: {col1}, col2:{col2}")

with col1:
    st.subheader("Model response A")
    st.write("Response")
    st.markdown("""
                ## RESPONSE A..
                1. messi
                2. Maradona
                3. Pele
                4. Ronaldo
                
                [goat.com](https://goat.com)
                
                
                """)

with col2:
    st.subheader("Model response B")
    st.write("Response")
    st.markdown("""
                
                ![PlaceHolder Text](https://)
                ## RESPONSE A..
                1. messi
                2. Maradona
                3. Pele
                4. Ronaldo
                
                [goat.com](https://goat.com)
                
                
                """)
    
    
