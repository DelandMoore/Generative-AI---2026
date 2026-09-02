#sessions

# counter: which is going to update when we click tthe button

import streamlit as st 
# counter=0
 
# increment = st.button("increment")

 
# if counter:
#     counter+=1;
# st.write(f"counter is: {counter}")

# session state is used to allocate memory


if "counter" not in st.session_state:
    st.session_state.counter=0
increment = st.button("increment")
if increment:
    st.session_state.counter+=1
    st.write(f"updated count: {st.session_state.counter}")