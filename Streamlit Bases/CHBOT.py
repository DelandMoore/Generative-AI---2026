import streamlit as st
from transformers import pipeline

model_path = r"C:\Users\ATZ COMPUTERS\Desktop\my_local_gpt2"

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model=model_path,
        tokenizer=model_path
    )

pipe = load_model()

if "messages" not in st.session_state:
    st.session_state.messages = []

def clear_conversation():
    st.session_state.messages = []

st.sidebar.title("Conversation")

st.sidebar.button(
    "Clear Conversation",
    on_click=clear_conversation
)

st.sidebar.write(
    f"Messages exchanged: {len(st.session_state.messages)}"
)

st.title("Local GPT-2 Curriculum Assistant")

st.write(
    "Ask me about deadlines, notebooks, datasets, "
    "assignments, or course information."
)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask a question about the curriculum...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    gpt_prompt = f"Student: {prompt}\nAssistant:"

    with st.chat_message("assistant"):

        result = pipe(
            gpt_prompt,
            return_full_text=False
        )

        response = result[0]["generated_text"].strip()

        st.write(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )