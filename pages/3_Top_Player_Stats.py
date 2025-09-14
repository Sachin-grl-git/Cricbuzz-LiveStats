import streamlit as st
import pandas as pd
from utils.db_connection import get_db_connection

st.title("🏆 Top Player Stats")

engine = get_db_connection()
query = "SELECT full_name, playing_role, runs, wickets, average, strike_rate FROM player_stats JOIN players USING(player_id) ORDER BY runs DESC LIMIT 10;"

try:
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
except Exception as e:
    st.error(f"Database Error: {e}")
