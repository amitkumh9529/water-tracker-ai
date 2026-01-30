import streamlit as st
import pandas as pd
from datetime import datetime
from src.agent import WaterIntakeAgent
from src.database import get_intake_history, log_intake


if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

#Welcome section

if not st.session_state.tracker_started:
    st.title("💧 AI-Powered Water Intake Tracker")
    st.markdown("""

    Track your daily water hydration intake with AI assistant. 
    log your intake, get smart feedback and stay healthy and hydrated
    
    """)

    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.rerun()

else:
    st.title("💧 AI Water Intake Tracker Dashboard")

    #sidebar for user ID input
    st.sidebar.header("Log your water Intake")
    user_id = st.sidebar.text_input("User ID", value="user_012")
    intake_ml = st.sidebar.number_input("Water Intake (ml)", min_value=0, step=100)

    if st.sidebar.button("Submit"):
        if user_id and intake_ml:
            log_intake(user_id, intake_ml)
            st.sidebar.success(f"Logged {intake_ml} ml for {user_id}!")

            agent = WaterIntakeAgent()
            feedback = agent.analyze_intake(intake_ml)
            st.sidebar.info(f"AI Feedback: {feedback}")

    #Divider
    st.markdown("---")


    #histrory section
    st.header("📊 Your Water Intake History")


    if user_id:
        history = get_intake_history(user_id)
        if history:
            dates = [datetime.strptime(row[1], "%Y-%m-%d") for row in history]
            values = [row[0] for row in history]

            df = pd.DataFrame({
                "Date": dates,
                "Water Intake (ml)": values
            })

            st.dataframe(df)
            st.line_chart(df, x="Date", y="Water Intake (ml)")
        else:
            st.warning("No intake history found. Please log your water intake.")