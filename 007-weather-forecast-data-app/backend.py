import requests

API_KEY = "3636dd0c34a5a33398c5db5e93397ba9"

def get_data(place, days_amount = 1, type = "Temperature"):
    url = f"https//api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    req = requests.get(url)
    content = req.json()

    data = content["list"][0:days_amount * 8]
    
    filtered_data = {
        "date": [dict["dt_txt"] for dict in data],
        "temp": [dict["main"]["temp"] for dict in data],
        "sky": [dict["weather"][0]["main"] for dict in data]
    }

    return filtered_data

# if __name__ == "__main__":
#     print(get_data("Tokio"))