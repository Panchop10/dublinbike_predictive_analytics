import pandas as pd

#Dublin Bike dataset
bike_dataset = pd.read_csv (r'../datasets/filtered_dublinbikes_2019.csv')

bike_dataset['YEAR'] = pd.to_datetime(bike_dataset['TIME']).apply(lambda x: x.strftime('%Y'))
bike_dataset['MONTH'] = pd.to_datetime(bike_dataset['TIME']).apply(lambda x: x.strftime('%m'))
bike_dataset['DAY'] = pd.to_datetime(bike_dataset['TIME']).apply(lambda x: x.strftime('%d'))
bike_dataset['HOUR'] = pd.to_datetime(bike_dataset['TIME']).apply(lambda x: x.strftime('%H'))
bike_dataset['MINUTES'] = pd.to_datetime(bike_dataset['TIME']).apply(lambda x: x.strftime('%M'))
#add day of the week to the dataset 
bike_dataset['DAY OF THE WEEK'] = pd.to_datetime(bike_dataset['TIME']).dt.dayofweek

#Weather dataset
weather_dataset = pd.read_csv (r'../datasets/dublinweather_20190101_20200101.csv')

weather_dataset['YEAR'] = pd.to_datetime(weather_dataset['dt_iso']).apply(lambda x: x.strftime('%Y'))
weather_dataset['MONTH'] = pd.to_datetime(weather_dataset['dt_iso']).apply(lambda x: x.strftime('%m'))
weather_dataset['DAY'] = pd.to_datetime(weather_dataset['dt_iso']).apply(lambda x: x.strftime('%d'))
weather_dataset['HOUR'] = pd.to_datetime(weather_dataset['dt_iso']).apply(lambda x: x.strftime('%H'))
weather_dataset['MINUTES'] = pd.to_datetime(weather_dataset['dt_iso']).apply(lambda x: x.strftime('%M'))

raw_joined_dataset = pd.merge(bike_dataset, weather_dataset, on=['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTES'])

raw_joined_dataset.to_csv(r'../datasets/joined_dataset.csv', index = False)