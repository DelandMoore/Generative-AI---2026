import streamlit as st
import pandas as pd
# text display
st.write("This is a simple text display")
st.title("The gods must be crazy")
st.header("Header")
st.subheader("Subheader")
st.markdown("<h1>H1 header</h1>", unsafe_allow_html=True)
st.success("Success Message")
st.info("This is an info")
st.warning("This is a warning")
st.error("this is an error")
st.metric(label="Model Accuracy", value="94.2%", delta = "+1.3%")


data = {
    "Day" :["Tuesday", "Wednesday", "Sunday"],
    'Temperature' : [56,57,54]
}
df = pd.DataFrame(data)
st.dataframe(df)

# user input
# slider input
#height = st.slider("enter your height",min,max,default,step=0.5)
height = st.slider("enter your height",3,19,10,step=2)

st.success(height+2)


#select box
model_name = st.selectbox("model", ["meta ai", "chatgpt", "gemma-3","llama-3"])
st.write(f"I selected {model_name}")

# number input
size = st.number_input("size", min_value=0,max_value=120,value=30)
length = st.number_input("lenght",min_value=10, max_value=20,value=13)
#st.info(f"{size + length}")
if st.button("add"):
    st.success(f"The sum is : {size + length}")
    st.toast("this just performed addition")
run_explain = st.checkbox("Show SHAP explanation")

name = st.text_input("pls enter your name")
chat_input = st.chat_input("pls enter your statement")

# Layouts
# sidebar
with st.sidebar:
    st.header("Controls")
    model = st.selectbox("Model", ["v1", "v2"])
    threshold = st.slider("Threshold", 0.0, 1.0,0.5)
side_value = st.sidebar.number_input("size", min_value=0,max_value=120,value=30)

# column layout
col1, col2, col3 = st.columns([1,1,1])
with col1:
    st.metric(label="Model Accuracy", value="94.2%", delta = "+1.3%")
with col2:
    st.metric(label="Model Precision", value="74.2%", delta = "+2.3%")
with col3:
    st.metric(label="Model Recall", value="84.2%", delta = "-3.3%")


# Expander
with st.expander("See raw prediction scores"):
    st.json({"class_0": 0.12, "class_1": 0.88, "class_2":0.00, "class_3":0.00, "class_4":0.00})