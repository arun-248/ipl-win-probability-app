import streamlit as st
import joblib as pkl
import pandas as pd
import math
from pathlib import Path
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="IPL Win Predictor", layout="wide")

# Load model + assets
MODEL_PATH = Path("models/model.pkl")
TEAM_PATH = Path("assets/team.pkl")
CITY_PATH = Path("assets/city.pkl")

model = pkl.load(open(MODEL_PATH, "rb"))
teams = pkl.load(open(TEAM_PATH, "rb"))
cities = pkl.load(open(CITY_PATH, "rb"))

# --- Header ---
st.markdown(
    "<h1 style='text-align: center; color: #00ff88;'>🏏 IPL Win Probability Estimator</h1>",
    unsafe_allow_html=True,
)
st.markdown("---")

# --- Input Section ---
with st.container():
    st.subheader("Match Setup")

    col1, col2, col3 = st.columns(3)
    with col1:
        batting_team = st.selectbox("Batting Team", sorted(teams), index=None, placeholder="Select batting team")
    with col2:
        bowling_team = st.selectbox("Bowling Team", sorted(teams), index=None, placeholder="Select bowling team")
    with col3:
        selected_city = st.selectbox("Host City", sorted(cities), index=None, placeholder="Select host city")

    target = st.text_input("🎯 Target Score", placeholder="Enter target score")

    col4, col5, col6 = st.columns(3)
    with col4:
        score = st.text_input("Current Score", placeholder="Enter current score")
    with col5:
        overs = st.text_input("Overs Done", placeholder="Enter overs (e.g., 12.3)")
    with col6:
        wickets = st.text_input("Wickets Fallen", placeholder="Enter wickets fallen")

# --- Prediction Button ---
if st.button("🔮 Predict Win Probability"):
    try:
        target = int(target) if target.strip() else 0
        score = int(score) if score.strip() else 0
        overs = float(overs) if overs.strip() else 0.0
        wickets = int(wickets) if wickets.strip() else 0

        whole = int(math.floor(overs))
        frac = round(overs - whole, 1)
        balls_bowled = whole * 6 + int(frac * 10)

        runs_left = target - score
        balls_left = 120 - balls_bowled
        wickets_left = 10 - wickets
        crr = (score / overs) if overs > 0 else 0
        rrr = (runs_left * 6 / balls_left) if balls_left > 0 else 0

        if not batting_team or not bowling_team or not selected_city:
            st.error("⚠️ Please select both teams and city.")
        elif balls_left <= 0:
            st.error("⚠️ Overs cannot exceed 20.")
        elif runs_left < 0:
            st.error("⚠️ Score cannot exceed target.")
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

            result = model.predict_proba(input_df)
            loss = result[0][0]
            win = result[0][1]

            # --- Stylish Results ---
            st.markdown("## 📊 Prediction Result")
            colA, colB = st.columns(2)

            with colA:
                st.metric(label=f"{batting_team} Win Chance", value=f"{round(win*100,1)} %")
            with colB:
                st.metric(label=f"{bowling_team} Win Chance", value=f"{round(loss*100,1)} %")

            # --- Cricbuzz-style Chart ---
            fig = go.Figure(data=[
                go.Bar(
                    name=batting_team,
                    x=[batting_team],
                    y=[win*100],
                    marker_color="#00ff88",
                    text=f"{round(win*100,1)}%",
                    textposition="auto"
                ),
                go.Bar(
                    name=bowling_team,
                    x=[bowling_team],
                    y=[loss*100],
                    marker_color="#ff4b4b",
                    text=f"{round(loss*100,1)}%",
                    textposition="auto"
                )
            ])

            fig.update_layout(
                barmode="group",
                yaxis=dict(title="Win Probability (%)", range=[0,100], color="#fafafa"),
                xaxis=dict(color="#fafafa"),
                title="Cricbuzz-style Win Predictor",
                template="plotly_dark",
                plot_bgcolor="#0e1117",
                paper_bgcolor="#0e1117",
                font=dict(color="#fafafa")
            )
            st.plotly_chart(fig, use_container_width=True)

            # --- Match Summary with color cards ---
            st.markdown("## 📋 Match Summary")
            colS1, colS2, colS3, colS4, colS5 = st.columns(5)

            def colored_card(label, value, color):
                st.markdown(
                    f"""
                    <div style="
                        background-color:{color};
                        padding:15px;
                        border-radius:10px;
                        text-align:center;
                        font-size:18px;
                        font-weight:bold;
                        color:white;">
                        {label}<br><span style="font-size:22px;">{value}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with colS1:
                colored_card("Runs Left", runs_left, "#f4a261")  # orange
            with colS2:
                colored_card("Balls Left", balls_left, "#2a9d8f")  # teal
            with colS3:
                colored_card("Wickets Left", wickets_left, "#e9c46a")  # yellow
            with colS4:
                colored_card("CRR", round(crr, 2), "#457b9d")  # blue
            with colS5:
                colored_card("RRR", round(rrr, 2), "#e63946")  # red

    except Exception as e:
        st.error(f"⚠️ Invalid input: {e}")
