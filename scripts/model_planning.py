import pandas as pd

# Load dataset
df = pd.read_csv (r'../datasets/raw_final_dataset.csv')

# columns of interest
cols_of_interest = [
    "available_bikes",
    "month",
    "temp",
    "feels_like",
    "humidity",
    "available_bikes_1h"
    ]

df = df[cols_of_interest]

df.to_csv(r'../datasets/final_dublinbike_dataset.csv', index = False)