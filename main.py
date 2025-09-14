import streamlit as st

st.set_page_config(page_title="Cricbuzz LiveStats", layout="wide")

st.title("🏏 Cricbuzz LiveStats Dashboard")
st.sidebar.success("Select a page from the sidebar 👈")

st.markdown("""
Welcome to **Cricbuzz LiveStats**, a real-time cricket analytics platform.  

Use the sidebar to explore:
- 📡 Live Match Updates  
- 🏆 Top Player Stats  
- 📊 SQL Analytics  
- 🛠️ CRUD Operations  
""")
