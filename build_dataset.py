import pandas as pd
from pathlib import Path

# Input files
MATCHES = Path("matches.csv")
DELIVERIES = Path("deliveries.csv")
OUTPUT = Path("processed_matches.csv")

print("🔄 Loading data...")
matches = pd.read_csv(MATCHES)
deliveries = pd.read_csv(DELIVERIES)

# Keep only 20 overs matches (T20 format)
matches = matches[matches["Season"].str.contains("IPL", na=False)]

# Merge match info into deliveries
df = deliveries.merge(
    matches[["id", "city", "team1", "team2", "winner"]],
    left_on="match_id",
    right_on="id",
    how="left"
)

# Target runs = total runs scored by team1
targets = df.groupby("match_id").agg({"total_runs": "sum"}).reset_index()
targets.rename(columns={"total_runs": "target"}, inplace=True)
df = df.merge(targets, on="match_id", how="left")

# Compute cumulative runs per match, per inning
df["current_score"] = df.groupby(["match_id", "inning"])["total_runs"].cumsum()

# Overs done = (over - 1) + (ball/6)
df["overs"] = df["over"] + (df["ball"] - 1) / 6.0

# Wickets fallen (dismissal_kind not null)
df["wickets_fallen"] = df.groupby(["match_id", "inning"])["player_dismissed"].cumcount()

# Batting/bowling teams
df["batting_team"] = df["batting_team"]
df["bowling_team"] = df["bowling_team"]

# Result: 1 if batting team == winner
df["result"] = (df["batting_team"] == df["winner"]).astype(int)

# Select relevant columns
final = df[[
    "batting_team", "bowling_team", "city",
    "target", "current_score", "overs", "wickets_fallen", "result"
]]

# Drop NaNs
final = final.dropna()

print("✅ Processed dataset shape:", final.shape)
final.to_csv(OUTPUT, index=False)
print(f"💾 Saved processed dataset to {OUTPUT}")
