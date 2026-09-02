import streamlit as st
import pandas as pd

#tabs
tab1, tab2, tab3 = st.tabs(["Results", "Metrics", "Explain"])
with tab1:
    st.write("Prediction results here")
    st.write("Confusion matrix, ROC Curve")
with tab2:
    st.write("Confusion matrix, ROC Curve")
    st.write("Metrics here")
with tab3: 
    st.write("Feature importance/ SHAP")
    st.write("...")