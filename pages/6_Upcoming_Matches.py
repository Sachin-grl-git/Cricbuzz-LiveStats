import streamlit as st
from utils.api_handler import fetch_upcoming_matches

st.set_page_config(page_title="Upcoming Matches", layout="wide")
st.title("📅 Upcoming Matches")

try:
    data = fetch_upcoming_matches()

    if "typeMatches" in data and len(data["typeMatches"]) > 0:
        for match_type in data["typeMatches"]:
            if "seriesMatches" in match_type:
                for series in match_type["seriesMatches"]:
                    if "seriesAdWrapper" in series:
                        series_name = series["seriesAdWrapper"]["seriesName"]
                        st.subheader(f"🏆 {series_name}")
                        for match in series["seriesAdWrapper"]["matches"]:
                            match_info = match["matchInfo"]
                            team1 = match_info["team1"]["teamName"]
                            team2 = match_info["team2"]["teamName"]
                            date = match_info["startDate"]
                            st.write(f"**{team1} vs {team2}** — 🕒 {date}")
    else:
        st.warning("⚠️ No upcoming matches found.")

except Exception as e:
    st.error(f"Error fetching upcoming matches: {e}")
