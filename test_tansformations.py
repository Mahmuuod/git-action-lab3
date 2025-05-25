from math import isclose
import logging

# Setup logging to write to logs.log
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_transformation_on_valid_sample():
    logging.info("🔍 Starting transformation test on valid sample...")

    # Sample API-like data
    sample = {
        "current_weather": {
            "temperature": 25.0,
            "windspeed": 11.0,
            "winddirection": 150,
            "weathercode": 1,
            "is_day": 1,
            "time": "2025-05-25T12:00"
        }
    }

    city = "TestCity"
    temp_C = float(sample["current_weather"]["temperature"])
    temp_F = (temp_C * 9/5) + 32
    windspeed = sample["current_weather"]["windspeed"]

    expected_temp_F = 77.0
    expected_windspeed = 11.0

    # Log computed values
    logging.info(f"Computed temperature_F: {temp_F}, Expected: {expected_temp_F}")
    logging.info(f"Computed windspeed: {windspeed}, Expected: {expected_windspeed}")

    # Assertions
    assert isclose(temp_F, expected_temp_F, rel_tol=1e-2), "❌ Temperature conversion incorrect"
    assert windspeed == expected_windspeed, "❌ Windspeed mismatch"

    logging.info("✅ Transformation test passed.")
test_transformation_on_valid_sample()