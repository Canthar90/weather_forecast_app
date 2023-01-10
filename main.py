import streamlit as st
import plotly.express as px
from backend import get_data


# Cosmetics site title and icon
st.set_page_config(
    page_title="Weather forecast",
    page_icon="☀️"
)

# Menu selectors
st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ", value="Warsaw")

slider = st.slider(
    "Number of days",
    min_value=1, max_value=5,
    help="Select numer of forecasted days"
) 
option = st.selectbox("Sekect data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for next {slider} days in {place} ")
try:
    data = get_data(place, slider, option)

    if option == "Temperature":
        desc = "Temperature (C)"
        
        # Creating temperature plot
        figure = px.line(x=data.keys(), y=data.values(), labels={"x": "Date", "y": f"{desc}"})
        st.plotly_chart(figure)
    else:
        desc = "Sky Condition"
        images = []
        for description in data.values():
            if description.lower() == "rain":
                images.append("images/rain.png")
            elif description.lower() == "clouds":
                images.append("images/cloud.png")
            elif description.lower() == "clear":
                images.append("images/clear.png")
                
        st.image(images, width=115)
except:
    st.error("Given city is invalid. Pliss eneter existing city name")
                
    
