from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, template_folder="./templates")

def get_station_data(station, is_parse_dates=True):
    return pd.read_csv(f"006-your-weather-api\data_small\TG_STAID{str(station).zfill(6)}.txt", skiprows=20,  parse_dates=["    DATE"] if is_parse_dates else None)

@app.route("/")
def home():
    return render_template("home.html", data=pd.read_csv("006-your-weather-api\data_small\stations.txt", skiprows=17).to_html())

@app.route("/api/v1/<station>")
def all_data(station):
    df = get_station_data(station)
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/year/<station>/<year>")
def year(station, year):
    df = get_station_data(station, False)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result

@app.route("/api/v1/day/<station>/<date>")
def day(station, date):
    df = get_station_data(station)
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station, "date": date, "temperature": temperature}

if __name__ == "__main__":
    app.run(debug=True)