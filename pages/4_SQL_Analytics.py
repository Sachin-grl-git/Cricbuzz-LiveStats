import streamlit as st
import pandas as pd
from utils.queries import QUERIES
from utils.db_connection import get_db_connection

st.title("📊 SQL Analytics")

engine = get_db_connection()
choice = st.selectbox("Choose a query", list(QUERIES.keys()))

if st.button("Run Query"):
    try:
        with engine.connect() as conn:
            df = pd.read_sql(QUERIES[choice], conn)
            st.dataframe(df)
    except Exception as e:
        st.error(f"Error: {e}")
