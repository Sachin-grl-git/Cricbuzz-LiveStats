QUERIES = {
    "Top 5 Run Scorers": "SELECT full_name, runs FROM player_stats JOIN players USING(player_id) ORDER BY runs DESC LIMIT 5;",
    "Top 5 Wicket Takers": "SELECT full_name, wickets FROM player_stats JOIN players USING(player_id) ORDER BY wickets DESC LIMIT 5;",
    "Team Win Counts": "SELECT winner, COUNT(*) as wins FROM matches GROUP BY winner ORDER BY wins DESC;"
}
