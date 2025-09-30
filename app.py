# importing the libraries
import streamlit as st
import joblib as pkl
import pandas as pd
import math
from pathlib import Path

# Page config
st.set_page_config(layout="wide")
st.title("🏏 IPL Win Predictor")

# Load model + assets
MODEL_PATH = Path("models/model.pkl")
TEAM_PATH = Path("assets/team.pkl")
CITY_PATH = Path("assets/city.pkl")

if not MODEL_PATH.exists() or not TEAM_PATH.exists() or not CITY_PATH.exists():
    st.error("❌ Model or asset files not found. Please run `train.py` first.")
    st.stop()

model = pkl.load(open(MODEL_PATH, "rb"))
teams = pkl.load(open(TEAM_PATH, "rb"))
cities = pkl.load(open(CITY_PATH, "rb"))

# --- UI Inputs ---
col1, col2, col3 = st.columns(3)
with col1:
    batting_team = st.selectbox("Select the batting team", sorted(teams))
with col2:
    bowling_team = st.selectbox("Select the bowling team", sorted(teams))
with col3:
    selected_city = st.selectbox("Select the host city", sorted(cities))

target = st.number_input("Target Score", min_value=0, max_value=720, step=1)

col4, col5, col6 = st.columns(3)
with col4:
    score = st.number_input("Current Score", min_value=0, max_value=720, step=1)
with col5:
    overs = st.number_input("Overs Done", min_value=0.0, max_value=20.0, step=0.1, format="%.1f")
with col6:
    wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10, step=1)

# --- Prediction ---
if st.button("Predict Probabilities"):
    # Balls bowled from overs (e.g., 8.5 -> 8*6 + 5 = 53)
    whole = int(math.floor(overs))
    frac = round(overs - whole, 1)
    balls_bowled = whole * 6 + int(frac * 10)

    runs_left = target - score
    balls_left = 120 - balls_bowled
    wickets_left = 10 - wickets
    crr = (score / overs) if overs > 0 else 0
    rrr = (runs_left * 6 / balls_left) if balls_left > 0 else 0

    if balls_left <= 0:
        st.error("⚠️ Overs cannot exceed 20. Please adjust.")
    elif runs_left < 0:
        st.error("⚠️ Score cannot exceed target. Please adjust.")
    else:
        input_df = pd.DataFrame({
            "batting_team": [batting_team],
            "bowling_team": [bowling_team],
            "city": [selected_city],
            "runs_left": [runs_left],
            "balls_left": [balls_left],
            "wickets_left": [wickets_left],
            "crr": [crr],
            "rrr": [rrr]
        })

        # Predict
        try:
            result = model.predict_proba(input_df)
            loss = result[0][0]
            win = result[0][1]

            st.subheader(f"{batting_team} win probability: **{round(win*100, 1)}%**")
            st.subheader(f"{bowling_team} win probability: **{round(loss*100, 1)}%**")
            st.progress(int(win * 100))
        except Exception as e:
            st.exception(e)
            st.error("Prediction failed. Please check the model & input features.")
