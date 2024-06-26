import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

logger.info("Start data generation...")

# Set random seed for reproducibility
np.random.seed(42)

# Define parameters
start_time = datetime(2023, 6, 1, 0, 0, 0)
end_time = datetime(2023, 8, 31, 23, 59, 0)
locations = ["BikeTown", "CycleHub", "PedalPoint", "SpinScape", "GearGrove", "BikeBreeze", "VelocityVista"]
max_available = 150
min_available = 0
max_delta = 4

# Initialize an empty list to hold the records
data = []

# Generate the timeseries data
for location in locations:

    logger.info(f"Generating data for {location}...")

    current_time = start_time

    while current_time <= end_time:
        # Generate available count
        current_available = np.random.randint(
            max(min_available, data[-1][2] - max_delta),
            min(max_available, data[-1][2] + max_delta)
        ) if data else np.random.randint(min_available, max_available)

        predicted_available = current_available + np.random.randint(-5, 5)

        data.append((current_time, location, current_available, predicted_available))
        
        current_time += timedelta(minutes=1)

# Create a pandas DataFrame from the records
df = pd.DataFrame(data, columns=["timestamp", "location_name", "n_available", "predicted"])

# Further preprocessing
df["timestamp"] = pd.to_datetime(df["timestamp"])  # Convert timestamp to datetime format
df["weekday"] = df["timestamp"].dt.day_of_week
df["weekday_name"] = df["timestamp"].dt.day_name()
df["is_weekend"] = df["weekday"] > 4
df["hour"] = df["timestamp"].dt.hour
df["week"] = df["timestamp"].dt.isocalendar().week

# Save the DataFrame to a CSV file
df.to_csv("./data/availability_dataset.csv", index=False)

logger.info("Data generation complete.")