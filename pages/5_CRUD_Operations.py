import streamlit as st
from utils.db_connection import get_db_connection

st.title("🛠️ CRUD Operations")
engine = get_db_connection()

# Example: Add Player
with st.form("add_player"):
    name = st.text_input("Full Name")
    role = st.text_input("Role")
    batting = st.text_input("Batting Style")
    bowling = st.text_input("Bowling Style")
    submitted = st.form_submit_button("Add Player")

    if submitted:
        try:
            with engine.begin() as conn:
                conn.execute(
                    "INSERT INTO players (full_name, playing_role, batting_style, bowling_style) VALUES (%s, %s, %s, %s)",
                    (name, role, batting, bowling)
                )
            st.success("✅ Player added successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
