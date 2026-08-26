import streamlit as st
st.title("Years to 100")
age = st.number_input("How old are you", min_value=0, max_value=120, value=23)
years_left = 100-age
if years_left > 0:
    st.write(f"You have {years_left} to reach a hudred years")
else:
    st.write(f"You areabove 100: {years_left}")

st.header("how streamlit works")
st.subheader("starting")
button1 = st.button("click me 1")
print(button1)

button2 = st.button("click me 2")
print(button2)

st.subheader("ending")
# it runs your code from top to bottom
# it also returns the code each time something happens

# CORE INPUT WIDGET
# text, paragraph, number, chice, multi, on, level, clicked

#What's a widget? : app component
text = st.text_input("Enter your name")
paragragh = st.text_area("Long input, eg a prompt")
number = st.number_input("A number: ", min_value=0)
choice = st.selectbox("pick one", ["GPT-2", "CLAUDE", "GEMINI", 'LAMNSOGPT'])
print(choice)

multi = st.multiselect("Pick from this", ["free", "premium", "pro"])
print(multi)

on = st.checkbox("Enable notifications")
enable_notification = st.toggle("enable notification", value=True)

#Forms in streamlit
st.subheader("FORMS")

username = st.text_input("What's your username")
user_age = st.number_input("What's your agae?")

submit_btn = st.button("submit form")

if submit_btn:
    st.write(f"your info is: {username} and {user_age}")


# Form Batching
# inp1
# inp2
#inp3

with st.form("settings_form"):
    model = st.selectbox("Model", ["Claude", "gpt-2", "gemini-2"])
    temperature = st.slider("Temperature", 0.0, 1.0, 0.5)
    submitted = st.form_submit_button("Save settings")
if submitted:
    st.write("Thank you for submitting")
    st.success(f"You are using: {model} at temperature {temperature}")