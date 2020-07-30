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

col_one_list = df['available_bikes'].tolist()

#remove first value
col_one_list.pop(0)

#remove last row in dataframe
df.drop(df.tail(1).index,inplace=True)

#add new column with prediction in 1 hour
df['available_bikes_1h'] = col_one_list

#convert weather main to numeric
df.loc[df['weather_main'] == 'Clouds', 'weather_main'] = 1
df.loc[df['weather_main'] == 'Rain', 'weather_main'] = 2
df.loc[df['weather_main'] == 'Drizzle', 'weather_main'] = 3
df.loc[df['weather_main'] == 'Mist', 'weather_main'] = 4
df.loc[df['weather_main'] == 'Clear', 'weather_main'] = 5
df.loc[df['weather_main'] == 'Fog', 'weather_main'] = 6
df.loc[df['weather_main'] == 'Snow', 'weather_main'] = 7
df.loc[df['weather_main'] == 'Haze', 'weather_main'] = 8
df.loc[df['weather_main'] == 'Smoke', 'weather_main'] = 9
df.loc[df['weather_main'] == 'Thunderstorm', 'weather_main'] = 10

df.to_csv(r'../datasets/raw_final_dataset.csv', index = False)

