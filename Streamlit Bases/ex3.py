import streamlit as st

#
with st.sidebar:
    model = st.selectbox("Model",["gpt-2","Claude","Gemini"])
    slider = st.slider("Temperature",0,100,20)
    
col1, col2 = st.columns(2)

with col1:
    st.subheader("Draft")
    draft = st.text_area("Draft text", height=200)
    # with st.expander("Debug info"):
    #     st.write(f'{model} and {slider}')
with col2:
    st.subheader("Final")
    final = st.text_area("Final text",height=200)
    
with st.expander("Debug info"):
        st.write(f'Model:{model}')
        st.write(f"Slider: {slider}")
 