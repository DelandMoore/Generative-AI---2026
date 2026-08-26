# 1st task: You will get an image of and output it, width=300
#then we will build a chatbox

import streamlit as st  

st.image("static/digital.png", "chat app logo", width=200)

#format in which you give chat messages

# st.chat_message
#["user":{}, "model":{}]= message

if "messages" not in st.session_state:
    st.session_state.messages=[]


# Redraw the full convo on every rerun
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
    # role = model | user
    
prompt = st.chat_input("Say something")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt })
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # placeholder response -> in real systems, this going to be a response from llm (gpt-2)

    reply = f"you said : {prompt}"
    st.session_state.messages.append({"role": "assistant", "content":reply})
    with st.chat_message("assistant"):
        st.markdown(reply)