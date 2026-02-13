import streamlit as st

st.title("Login Example")

USERNAME = "admin"
PASSWORD = "1234"

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.success("Login successful!")
        st.session_state.logged_in = True
    else:
        st.error("Invalid credentials")

if "logged_in" in st.session_state and st.session_state.logged_in:
    st.write("Welcome to the dashboard!")