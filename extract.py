import requests
import logging

logging.basicConfig(filename='logs.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_weather_data(latitude, longitude):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f"✅ Successfully fetched weather data for lat={latitude}, lon={longitude}")
        return response.json()
    except requests.RequestException as e:
        logging.error(f"❌ Failed to fetch weather data for lat={latitude}, lon={longitude} — {e}")
        raise
