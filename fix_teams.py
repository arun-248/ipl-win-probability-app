import joblib
from pathlib import Path

valid_teams = [
    "Sunrisers Hyderabad",
    "Mumbai Indians",
    "Gujarat Titans",
    "Royal Challengers Bangalore",
    "Kolkata Knight Riders",
    "Kings XI Punjab",
    "Chennai Super Kings",
    "Rajasthan Royals",
    "Delhi Capitals"
]

ASSETS_PATH = Path("assets/team.pkl")
ASSETS_PATH.parent.mkdir(exist_ok=True, parents=True)

joblib.dump(sorted(valid_teams), ASSETS_PATH)
print("✅ team.pkl updated with only the 9 valid teams")
