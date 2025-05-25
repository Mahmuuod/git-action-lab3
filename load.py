import pandas as pd
import logging
from transform import data

logging.basicConfig(filename='logs.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    df = pd.DataFrame(data)
    df.to_csv("avg_weather.csv", index=False)
    logging.info("✅ Average weather data saved to avg_weather.csv")
except Exception as e:
    logging.error(f"❌ Failed to save data to CSV: {e}")
