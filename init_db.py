import sqlite3

# Connect (this will create cricbuzz.db if not exists)
conn = sqlite3.connect("cricbuzz.db")
cursor = conn.cursor()

# Create tables
cursor.executescript("""
CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT,
    country TEXT
);

CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    country TEXT,
    playing_role TEXT,
    batting_style TEXT,
    bowling_style TEXT
);

CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    team1_id INT,
    team2_id INT,
    venue TEXT,
    match_date TEXT,
    winner TEXT
);

CREATE TABLE IF NOT EXISTS player_stats (
    stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INT,
    format TEXT,
    runs INT,
    wickets INT,
    average REAL,
    strike_rate REAL
);
""")

# Insert sample data
cursor.executescript("""
INSERT INTO teams (team_name, country) VALUES
('India', 'India'),
('Australia', 'Australia'),
('England', 'England');

INSERT INTO players (full_name, country, playing_role, batting_style, bowling_style) VALUES
('Virat Kohli', 'India', 'Batsman', 'Right-hand bat', 'Right-arm medium'),
('Rohit Sharma', 'India', 'Batsman', 'Right-hand bat', 'Right-arm offbreak'),
('Pat Cummins', 'Australia', 'Bowler', 'Right-hand bat', 'Right-arm fast'),
('Joe Root', 'England', 'Allrounder', 'Right-hand bat', 'Right-arm offbreak');

INSERT INTO matches (description, team1_id, team2_id, venue, match_date, winner) VALUES
('India vs Australia - World Cup Final', 1, 2, 'Ahmedabad', '2023-11-19', 'India'),
('England vs India - Test Match', 3, 1, 'Lord''s', '2023-07-10', 'England');

INSERT INTO player_stats (player_id, format, runs, wickets, average, strike_rate) VALUES
(1, 'ODI', 12898, 4, 57.0, 93.5),
(2, 'ODI', 10709, 8, 49.0, 89.4),
(3, 'ODI', 1250, 234, 22.5, 80.0),
(4, 'ODI', 6200, 36, 50.1, 87.0);
""")

conn.commit()
conn.close()

print("✅ SQLite DB 'cricbuzz.db' created with sample data!")
