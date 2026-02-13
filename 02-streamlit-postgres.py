import streamlit as st

st.title("Button Example")

name = st.text_input("Enter your name:")

if st.button("Say Hello"):
    st.success(f"Hello, {name} 👋")