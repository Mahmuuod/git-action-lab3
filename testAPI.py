import requests
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def api_check() -> bool:
    url = "https://api.open-meteo.com/v1/forecast"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info("✅ API check successful.")
            return True
        else:
            logging.warning(f"⚠️ API check failed with status code {response.status_code}.")
            raise
    except Exception as e:
        logging.error(f"❌ API check failed with exception: {e}")
        raise

api_check()