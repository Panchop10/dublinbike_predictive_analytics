import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import cov
from scipy.stats import pearsonr
from scipy.stats import spearmanr



# Load dataset
df = pd.read_csv (r'../datasets/raw_final_dataset.csv')

# create a figure and axis
fig, ax = plt.subplots()

# # BIKES AVAILABLE VS MONTH
# # scatter the month against the available_bikes
# ax.scatter(df['month'], df['available_bikes'])
# # set a title and labels
# ax.set_title('Bikes available per month')
# ax.set_xlabel('month')
# ax.set_ylabel('available bikes')

# # BIKES AVAILABLE VS MONTH
# fig, ax = plt.subplots()
# ax.scatter(df['day'], df['available_bikes'])
# ax.set_title('Bikes available per day')
# ax.set_xlabel('day')
# ax.set_ylabel('available bikes')

# # BIKES AVAILABLE VS HOUR
# fig, ax = plt.subplots()
# ax.scatter(df['hour'], df['available_bikes'])
# ax.set_title('Bikes available per hour')
# ax.set_xlabel('hour')
# ax.set_ylabel('available bikes')

# # BIKES AVAILABLE VS DAY OF THE WEEK
# fig, ax = plt.subplots()
# ax.scatter(df['day_of_the_week'], df['available_bikes'])
# ax.set_title('Bikes available per day of the week')
# ax.set_xlabel('day of the week 0: Monday - 6: Sunday')
# ax.set_ylabel('available bikes')

# BIKES AVAILABLE VS TEMPERATURE
# fig, ax = plt.subplots()
# ax.scatter(df['temp'], df['available_bikes'])
# ax.set_title('Bikes available per temperature')
# ax.set_xlabel('temperature')
# ax.set_ylabel('available bikes')

# # BIKES AVAILABLE VS FEELS LIKE
# fig, ax = plt.subplots()
# ax.scatter(df['feels_like'], df['available_bikes'])
# ax.set_title('Bikes available per feels like temperature')
# ax.set_xlabel('feels like temperature')
# ax.set_ylabel('available bikes')

# # BIKES AVAILABLE VS PRESSURE
# fig, ax = plt.subplots()
# ax.scatter(df['pressure'], df['available_bikes'])
# ax.set_title('Bikes available per pressure')
# ax.set_xlabel('pressure')
# ax.set_ylabel('available bikes')

# # BIKES AVAILABLE VS HUMIDITY
# fig, ax = plt.subplots()
# ax.scatter(df['humidity'], df['available_bikes'])
# ax.set_title('Bikes available per humidity')
# ax.set_xlabel('humidity')
# ax.set_ylabel('available bikes')

# # BIKES AVAILABLE VS WIND SPEED
# fig, ax = plt.subplots()
# ax.scatter(df['wind_speed'], df['available_bikes'])
# ax.set_title('Bikes available per Wind speed')
# ax.set_xlabel('wind_speed')
# ax.set_ylabel('available bikes')

# # BIKES AVAILABLE VS WIND DIRECTION
# fig, ax = plt.subplots()
# ax.scatter(df['wind_deg'], df['available_bikes'])
# ax.set_title('Bikes available per Wind direction')
# ax.set_xlabel('wind direction')
# ax.set_ylabel('available bikes')

# # BIKES AVAILABLE VS RAIN VOLUME DURING LAST HOUR
# fig, ax = plt.subplots()
# ax.scatter(df['rain_last_hour'], df['available_bikes'])
# ax.set_title('Bikes available per Rain volume during the last hour')
# ax.set_xlabel('rain volume in mm')
# ax.set_ylabel('available bikes')

# # BIKES AVAILABLE VS CLOUDS
# fig, ax = plt.subplots()
# ax.scatter(df['clouds_all'], df['available_bikes'])
# ax.set_title('Bikes available per Clouds')
# ax.set_xlabel('clouds in the sky')
# ax.set_ylabel('available bikes')

# # BIKES AVAILABLE VS CLOUDS
# fig, ax = plt.subplots()
# ax.scatter(df['weather_main'], df['available_bikes'])
# ax.set_title('Bikes available per Weather')
# ax.set_xlabel('type of weather')
# ax.set_ylabel('available bikes')

# sns.boxplot('weather_main', 'available_bikes', data=df)

#sns.boxplot('clouds_all', 'available_bikes', data=df)
#sns.boxplot('rain_last_hour', 'available_bikes', data=df)

# sns.boxplot('month', 'available_bikes', data=df)

# # calculate covariance matrix
# Variables can be related by a linear relationship. This is a relationship that is consistently additive across the two data samples.
# covariance = cov(df['weather_main'], df['available_bikes'])

# print(covariance)

# The sign of the covariance can be interpreted as whether the two variables change in the same direction (positive) or change in different directions (negative). 
# The magnitude of the covariance is not easily interpreted. A covariance value of zero indicates that both variables are completely independent.



# calculate Pearson's correlation
# The Pearson correlation coefficient (named for Karl Pearson) can be used to summarize the strength of the linear relationship between two data samples.
# corr, _ = pearsonr(df['month'], df['available_bikes'])

# print('Pearsons correlation: %.3f' % corr)

# The coefficient returns a value between -1 and 1 that represents the limits of correlation from a full negative correlation to a full positive correlation. 
# A value of 0 means no correlation. The value must be interpreted, where often a value below -0.5 or above 0.5 indicates a notable correlation, and values 
# below those values suggests a less notable correlation.




# Two variables may be related by a nonlinear relationship, such that the relationship is stronger or weaker across the distribution of the variables.

# calculate spearman's correlation

corr, _ = spearmanr(df['clouds_all'], df['available_bikes'])
print('Spearmans correlation: %.3f' % corr)

#As with the Pearson correlation coefficient, the scores are between -1 and 1 for perfectly negatively correlated variables and perfectly 
# positively correlated respectively.

plt.show(block=True)
