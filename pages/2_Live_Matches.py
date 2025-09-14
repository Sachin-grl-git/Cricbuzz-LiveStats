import streamlit as st
from utils.api_handler import fetch_live_matches

st.title("📡 Live Matches")

data = fetch_live_matches()

if "typeMatches" in data:
    for match_type in data["typeMatches"]:
        st.subheader(match_type.get("matchType", "Unknown Format"))
        for series in match_type.get("seriesMatches", []):
            series_wrapper = series.get("seriesAdWrapper", {})
            for match in series_wrapper.get("matches", []):
                info = match.get("matchInfo", {})
                t1 = info.get("team1", {}).get("teamName")
                t2 = info.get("team2", {}).get("teamName")
                venue = info.get("venueInfo", {}).get("ground")
                st.write(f"**{t1} vs {t2}** at {venue}")
                st.write("---")
else:
    st.warning("⚠️ No live matches right now.")
