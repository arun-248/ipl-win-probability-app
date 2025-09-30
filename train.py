import math
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# Paths
DATA = Path("processed_matches.csv")
  # use your matches.csv dataset
MODELS_DIR = Path("models")
ASSETS_DIR = Path("assets")
MODELS_DIR.mkdir(exist_ok=True, parents=True)
ASSETS_DIR.mkdir(exist_ok=True, parents=True)

# ---------------- 1. Load dataset ----------------
df = pd.read_csv(DATA)

# Required columns
required_cols = [
    "batting_team", "bowling_team", "city",
    "target", "current_score", "overs", "wickets_fallen",
    "result"
]
for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Dataset is missing required column: {col}")

# ---------------- 2. Feature engineering ----------------
def overs_to_balls(x):
    """Convert overs like 8.5 -> 53 balls"""
    whole = int(x)
    frac = round(x - whole, 1)
    balls = whole * 6 + int(frac * 10)
    return balls

balls_bowled = df["overs"].apply(overs_to_balls)
balls_left = 120 - balls_bowled
runs_left = df["target"] - df["current_score"]
wickets_left = 10 - df["wickets_fallen"]

crr = df["current_score"] / df["overs"].replace(0, np.nan)
rrr = np.where(balls_left > 0, (runs_left * 6) / balls_left, 0)

X = pd.DataFrame({
    "batting_team": df["batting_team"],
    "bowling_team": df["bowling_team"],
    "city": df["city"],
    "runs_left": runs_left,
    "balls_left": balls_left,
    "wickets_left": wickets_left,
    "crr": crr,
    "rrr": rrr
})
y = df["result"]

# Drop invalid rows
mask = (
    (X["balls_left"] > 0) &
    (X["runs_left"] >= 0) &
    (X["wickets_left"] >= 0) &
    np.isfinite(X["crr"]) &
    np.isfinite(X["rrr"])
)
X = X[mask]
y = y[mask]

# ---------------- 3. Build pipeline ----------------
cat_cols = ["batting_team", "bowling_team", "city"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore", drop="first", sparse_output=False), cat_cols)
    ],
    remainder="passthrough"
)

model = Pipeline([
    ("pre", preprocessor),
    ("clf", LogisticRegression(max_iter=1000))
])

model.fit(X, y)

# ---------------- 4. Save artifacts ----------------
joblib.dump(model, MODELS_DIR / "model.pkl")
joblib.dump(sorted(df["batting_team"].unique()), ASSETS_DIR / "team.pkl")
joblib.dump(sorted(df["city"].unique()), ASSETS_DIR / "city.pkl")

print("✅ Training complete!")
print(f"Saved model.pkl → {MODELS_DIR}")
print(f"Saved team.pkl, city.pkl → {ASSETS_DIR}")
