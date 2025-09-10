import pandas as pd

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'

crime_rates = pd.read_csv(url)

print(crime_rates.head())

print(crime_rates.info())

#Converting the year into datetime64
crime_rates.Year = pd.to_datetime(crime_rates.Year, format='%Y')
print("\n=== Converting Date into datetime64 ===")
from time import sleep
sleep(2)
print(crime_rates.dtypes)

#Setting the Year column as the index of the dataframe
crime_rates = crime_rates.set_index('Year', drop=True)
print("\n=== Setting Year As Index ===")
print(crime_rates.head())

#Deleting the total column
del crime_rates['Total']
print("\n=== Deleting The Total Column ===")
sleep(2)
print("\n=== Total Column Deleted Successfully! === \nHead Preview: \n")
print(crime_rates.head())

#Grouping the year by decades - NOT SURE ABOUT THIS ONE !!!!!!!!!!!!!!

#Using resample to sum each decade - taking note of population
crime_rates = crime_rates.resample('10YS').sum()
#print(crime_rates.head())

#Uses resample to get the max value only for the population column
population = crime_rates['Population'].resample('10YS').max()

crime_rates['Population'] = population

print("\n=== Grouping The Year In Decades ===")
print(crime_rates.head())

#The most dangerous decade in the US
danger_decade = crime_rates.idxmax(0)
print("\n=== The Most Dangerous Decade Per Danger ===")
print(danger_decade)
