import pandas as pd

#First Quarter
df_q1 = pd.read_csv (r'../datasets/dublinbikes_20190101_20190401.csv')
df_q1_filtered = df_q1.loc[df_q1['STATION ID'] == 80]
df_q1_filtered.to_csv(r'../datasets/filtered_dublinbikes_2019.csv', index = False)

#Second Quarter
df_q2 = pd.read_csv (r'../datasets/dublinbikes_20190401_20190701.csv')
df_q2_filtered = df_q2.loc[df_q2['STATION ID'] == 80]
df_q2_filtered.to_csv(r'../datasets/filtered_dublinbikes_2019.csv', mode='a', index = False, header = False)

#Third Quarter
df_q3 = pd.read_csv (r'../datasets/dublinbikes_20190701_20191001.csv')
df_q3_filtered = df_q3.loc[df_q3['STATION ID'] == 80]
df_q3_filtered.to_csv(r'../datasets/filtered_dublinbikes_2019.csv', mode='a', index = False, header = False)

#Fourth Quarter
df_q4 = pd.read_csv (r'../datasets/dublinbikes_20191001_20200101.csv')
df_q4_filtered = df_q4.loc[df_q4['STATION ID'] == 80]
df_q4_filtered.to_csv(r'../datasets/filtered_dublinbikes_2019.csv', mode='a', index = False, header = False)
