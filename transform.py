import logging
from extract import get_weather_data

logging.basicConfig(filename='logs.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

locations = {
    "Cairo": (30.0444, 31.2357),
    "Dakahlia": (31.0364, 31.3807),
    "Giza": (30.0131, 31.2089)
}

weather_data = []

for city, (lat, lon) in locations.items():
    try:
        raw = get_weather_data(lat, lon)
        weather = raw["current_weather"]
        temp_C = float(weather["temperature"])
        temp_F = (temp_C * 9/5) + 32

        record = {
            "city": city,
            "temperature_F": round(temp_F, 2),
            "windspeed": weather["windspeed"]
        }

        weather_data.append(record)
        logging.info(f"✅ Transformed weather data for {city}: {record}")

    except Exception as e:
        logging.error(f"❌ Failed to process data for {city}: {e}")

try:
    avg_temperature = round(sum(d["temperature_F"] for d in weather_data) / len(weather_data), 2)
    avg_windspeed = round(sum(d["windspeed"] for d in weather_data) / len(weather_data), 2)

    data = [{
        "average_temperature_F": avg_temperature,
        "average_windspeed": avg_windspeed
    }]
    logging.info(f"📊 Aggregated data: {data[0]}")
except Exception as e:
    logging.error(f"❌ Failed to compute averages: {e}")
    data = []
