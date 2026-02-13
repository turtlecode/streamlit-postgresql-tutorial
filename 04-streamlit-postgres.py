import streamlit as st
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="turtlecode"
    )

st.title("Create Table")

if st.button("Create Users Table"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            password VARCHAR(100)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

    st.success("Table created successfully!")