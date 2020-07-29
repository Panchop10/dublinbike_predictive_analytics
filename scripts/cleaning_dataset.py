import pandas as pd

# Reading the dataset joined
df = pd.read_csv (r'../datasets/joined_dataset.csv')

# columns of interest
cols_of_interest = [
    "AVAILABLE BIKES",
    "MONTH",
    "DAY",
    "HOUR",
    "DAY OF THE WEEK",
    "temp",
    "feels_like",
    "pressure",
    "humidity",
    "wind_speed",
    "wind_deg",
    "rain_1h",
    "clouds_all",
    "weather_main"
    ]

df = df[cols_of_interest]

# rename columns to standarize the names
df.columns = [
    "available_bikes",
    "month",
    "day",
    "hour",
    "day_of_the_week",
    "temp",
    "feels_like",
    "pressure",
    "humidity",
    "wind_speed",
    "wind_deg",
    "rain_last_hour",
    "clouds_all",
    "weather_main"
    ]

# replace NaN values with 0 for rain_1h when it didn't rain.
df['rain_last_hour'] = df['rain_last_hour'].fillna(0)

df.to_csv(r'../datasets/raw_final_dataset.csv', index = False)