import os 
import requests


API_KEY = os.getenv("API_KEY")



def get_data(place, forecast_days, kind):
    """Gets data from API"""
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    content = response.json()
    filtered_data = content["list"]
    
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    
    if kind == "Temperature":
        filtered_temperatures = [dict["main"]["temp"] for dict in filtered_data ]
        date_points = [dict["dt_txt"] for dict in filtered_data]
        response_dict = {date: temperature for date, temperature in zip(date_points, filtered_temperatures)}
    if kind == "Sky":
        filtered_sky = [dict["weather"][0]["main"] for dict in filtered_data]
        date_points = [dict["dt_txt"] for dict in filtered_data]
        response_dict = {date: sky for date, sky in zip(date_points, filtered_sky)}
    return response_dict


if __name__ == "__main__":
    print(get_data("tokyo", forecast_days=3, kind="Temperature"))