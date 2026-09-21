import streamlit as st
from DeepAgentTask import agent

st.set_page_config(page_title="Deep Agent Researcher")
st.title("Deep Agent Researcher")

@st.cache_resource
def get_deep_agent():
    return agent
DeepAgentTask = get_deep_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

query = st.chat_input("Ask your research agent something")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)
    with st.chat_message("assistant"):
        todo_placeholder = st.empty()
        answer_placeholder = st.empty()
        final_content = ""
        last_chunk = {}

        for chunk in DeepAgentTask.stream(
            {"messages": [{"role": "user", "content": query}]},
            stream_mode = "values",
        ) :
            last_chunk = chunk
            todos = chunk.get("todos", [])  
            if todos:
                todo_text =  "\n".join(f"- [{t['status']}] {t['content']}" for t in todos)
                todo_placeholder.markdown(f"**To-dos:**\n{todo_text}")

            if chunk.get("messages"):
                last = chunk["messages"][-1]
                if hasattr(last, "content") and last.content:
                    final_content = last.content 
                    answer_placeholder.write(final_content)

        st.session_state.messages.append({"role": "assistant", "content": final_content})
        files = last_chunk.get("files", {})
        if files:
            st.subheader("Generated files")
            for fname, content in files.items():
                with st.expander(fname):
                    st.code(content)
            