import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Climate App", layout="centered")

# ---------- WHITE UI ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #ffffff;
}
body, p, div, span, label {
    color: black !important;
}
h1, h2, h3 {
    color: #003366 !important;
    text-align: center;
}
input {
    background-color: white !important;
    color: black !important;
}
div[data-baseweb="select"] > div {
    background-color: white !important;
    color: black !important;
}
ul[role="listbox"] {
    background-color: white !important;
}
li[role="option"] {
    color: black !important;
}
div[data-baseweb="calendar"] {
    background-color: white !important;
}
.stButton button {
    background-color: #3366cc;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION ----------
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------- PAGE 1 ----------
if st.session_state.page == 1:
    st.title("🌍 Climate Impact Forecasting")

    st.write("Climate means long-term weather patterns. 🌦️")
    st.write("We must protect climate for future generations. 🌱")

    st.markdown("### 🌿 How to Save Climate")
    tips = [
        "🚲 Use public transport",
        "💡 Save electricity",
        "🌳 Plant trees",
        "🚫 Reduce plastic",
        "💧 Save water",
        "♻️ Recycle waste",
        "🌞 Use renewable energy",
        "🌍 Spread awareness"
    ]
    for t in tips:
        st.write(t)

    if st.button("➡️ Next"):
        st.session_state.page = 2


# ---------- PAGE 2 ----------
elif st.session_state.page == 2:
    st.title("🔹 Enter Details")

    city = st.text_input("📍 Enter City")
    country = st.text_input("🌍 Enter Country")

    duration = st.selectbox("📅 Duration", ["7 Days", "30 Days"])
    date = st.date_input("📆 Select Date", datetime.date.today())

    parameter = st.selectbox("🌡️ Parameter", ["Temperature", "Rainfall", "Humidity"])
    purpose = st.selectbox("🧳 Purpose", ["Travel", "Work", "Study"])
    budget = st.radio("💰 Budget", ["Low", "Medium", "High"])
    travel_type = st.selectbox("👨‍👩‍👧 Travel Type", ["Solo", "Family", "Friends"])

    if st.button("➡️ Next"):
        if city.strip() == "" or country.strip() == "":
            st.warning("⚠️ Please fill all fields")
        else:
            st.session_state.city = city
            st.session_state.country = country
            st.session_state.duration = duration
            st.session_state.date = date
            st.session_state.parameter = parameter
            st.session_state.purpose = purpose
            st.session_state.budget = budget
            st.session_state.travel_type = travel_type
            st.session_state.page = 3


# ---------- PAGE 3 ----------
elif st.session_state.page == 3:
    st.title("🔸 Output")

    city = st.session_state.city
    country = st.session_state.country
    duration = st.session_state.duration
    date = st.session_state.date
    parameter = st.session_state.parameter
    purpose = st.session_state.purpose
    budget = st.session_state.budget
    travel_type = st.session_state.travel_type

    # MODEL
    X = np.array([[2020],[2021],[2022],[2023]])
    y = np.array([30,31,32,33])

    model = LinearRegression()
    model.fit(X, y)

    future_year = date.year
    prediction = model.predict([[future_year]])

    st.write(f"📍 {city}, {country}")
    st.write(f"📅 Duration: {duration}")
    st.write(f"📆 Date: {date}")
    st.write(f"🌡️ Parameter: {parameter}")
    st.write(f"🧳 Purpose: {purpose}")
    st.write(f"💰 Budget: {budget}")
    st.write(f"👨‍👩‍👧 Travel: {travel_type}")

    # ---------- SUGGESTIONS ----------
    st.subheader("💡 Suggestions")

    if prediction[0] > 35:
        st.warning("🔥 High temperature! Avoid afternoon travel")

    if purpose == "Travel":
        st.success("🌴 Plan your trip for better experience")

    if budget == "Low":
        st.info("💰 Use budget-friendly transport")

    if travel_type == "Family":
        st.info("👨‍👩‍👧 Choose safe weather conditions")

    if parameter == "Rainfall":
        st.info("🌧️ Carry umbrella")

    st.success(f"📊 Predicted Value: {prediction[0]:.2f}")

    # ---------- 3 GRAPHS ----------
    if st.button("📈 Show Graph"):
        days = 7 if duration == "7 Days" else 30
        x = np.arange(1, days+1)

        temp = prediction[0] + np.sin(x/3)*2
        rain = np.abs(np.sin(x/2))*10
        humidity = 60 + np.cos(x/4)*10

        df = pd.DataFrame({
            "Day": x,
            "Temperature": temp,
            "Rainfall": rain,
            "Humidity": humidity
        })

        # Temperature
        fig1 = px.line(df, x="Day", y="Temperature", title="🌡️ Temperature")
        fig1.update_layout(plot_bgcolor="white", paper_bgcolor="white", font_color="black")
        st.plotly_chart(fig1, use_container_width=True)

        # Rainfall
        fig2 = px.line(df, x="Day", y="Rainfall", title="🌧️ Rainfall")
        fig2.update_layout(plot_bgcolor="white", paper_bgcolor="white", font_color="black")
        st.plotly_chart(fig2, use_container_width=True)

        # Humidity
        fig3 = px.line(df, x="Day", y="Humidity", title="💧 Humidity")
        fig3.update_layout(plot_bgcolor="white", paper_bgcolor="white", font_color="black")
        st.plotly_chart(fig3, use_container_width=True)

    if st.button("🔙 Back"):
        st.session_state.page = 1