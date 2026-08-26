import streamlit as st
import pandas as pd 
import os
# df = pd.DataFrame({
#     "model":["gpt-2","gpt--3", "claude-sonnet", "haiku"],
#     "avg_speed": [820,123,450,390]
# })

# #interactive modes
# st.dataframe(df)

# # static
# st.table(df)

# print(df)

# st.image("static/digital.png", "logo image")
# st.video


# # FILE UPLOADS
# uploaded = st.file_uploader(
#     "upload your files here",
#     type=["pdf","txt","docx"],
#     accept_multiple_files=False
# )

# if uploaded is not None:
#     st.write(f"File name: {uploaded.name}")
#     st.write(f"File size: {uploaded.size} bytes")
#     #read files size content in memory
#     raw_bytes = uploaded.read()


st.title("MY IMAGE UPLOAD APP")

#lets create an aimage uploader widget

uploaded_file = st.file_uploader(
    "Upload an image",
    type = ["png", "jpg","jpeg"]
)

if uploaded_file is not None:
    #show the preview of the uploaded image
    st.image(uploaded_file, caption="this is my uploaded image")
    
    confirm_upload = st.button("confirm and save")
    if confirm_upload:
        #create folder and save the image inside
        os.makedirs("my_images", exist_ok=True)
        save_path = os.path.join("my_images", uploaded_file.name)

        #wb - write bytes
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
            
            st.success(f"saved successfully")