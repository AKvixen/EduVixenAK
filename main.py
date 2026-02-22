import streamlit as st

# This must be the VERY FIRST line of code
st.set_page_config(page_title="EduVixenAK", layout="wide")

st.write("## 🦊 EduVixenAK: Connection Successful")
st.balloons()

st.sidebar.title("Dashboard")
st.sidebar.info("System is now connected to GitHub.")

if st.button("Check Server Status"):
    st.write("Server is healthy and responding!")
