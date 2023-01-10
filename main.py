import streamlit as st
import plotly.express as px
from backend import get_data


st.set_page_config(
    page_title="Weather forecast",
    page_icon="☀️"
)


st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")

slider = st.slider(
    "Number of days",
    min_value=1, max_value=5,
    help="Select numer of forecasted days"
) 
option = st.selectbox("Sekect data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for next {slider} days in {place} ")

data = get_data(place, slider, option)

dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
temperatures = [10, 11, 15]
temperatures = [slider * i for i in temperatures]
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)