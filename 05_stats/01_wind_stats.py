import pandas as pd
import datetime

data_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'

#Assigning data to variable data - and replace the first three columns by a proper datetime index
data = pd.read_csv(data_url, sep = '\s+', parse_dates=[[0, 1, 2]])
print(data.head())
print()

#We do not have year 2061 - this is a function to fix that - problem is that the years are 2061 and so on...
### Function Uses datetime ###
print(data.tail())
print()

def fix_century(x):
    year = x.year - 100 if x.year > 1989 else x.year
    return datetime.date(year, x.month, x.day)

#Applying the function to fix the century
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)

print(data.head())
print(data.info())
print()

data['Yr_Mo_Dy'] = pd.to_datetime(data['Yr_Mo_Dy'])

print(data.info())

data = data.set_index('Yr_Mo_Dy')

print(data.dtypes)

#How many values are missing for each location over the period of time
data_null_count = data.isnull().sum()
print("\n=== Locations Without Values ===")
print(data_null_count)

#How many non-missing values are there in total
data_not_null_count = data.notnull().sum()
print("\n=== Locations With Values ===")
print(data_not_null_count)

#Calculate the mean windspeeds of the windspeeds over all locations and all the times
mean_wind_speeds = data.sum().sum() / data.notna().sum().sum()
print("\n=== The Mean Windspeed For All Windspeeds Over All Locations ===")
print(mean_wind_speeds)

#Create a DataFrame and call it loc_stats and calculate the min, max, and mean windspeeds at each location over all the days
loc_stats = pd.DataFrame()

loc_stats = data.describe(percentiles=[])
print("\n=== === === ===")
print(loc_stats)

"""Creating a DataFrame called day_stats and calculate the min, max, and mean windspeed 
and standard deviations of the windspeeds accross all the locations at each day"""

day_stats = pd.DataFrame()

day_stats['min'] = data.min(axis=1)
day_stats['max'] = data.max(axis=1)
day_stats['mean'] = data.mean(axis=1)
day_stats['std'] = data.std(axis=1)

print("\n=== Day Stats - Min, Max, and Mean ===")
print(day_stats.head())

#Finding the average windspeed in January for each location
average_for_jan = data.loc[data.index.month == 1].mean()
print("\n=== Average Windspeed In January For Each Location ===")
print(average_for_jan)

#Downsampling the record to a yearly frequency for each location
downsample_to_yearly = data.groupby(data.index.to_period('A')).mean()
print("\n=== Printing Downsampled Record To A Yearly Frequency For Each Location ===")
print(downsample_to_yearly)

#Downsampling the record to a monthly frequency for each location
downsample_to_monthly = data.groupby(data.index.to_period('M')).mean()
print("\n=== Printing Downsampled Record To A Monthly Frequency For Each Location ===")
print(downsample_to_monthly)

#Downsampling the record to a weekly frequency for each location
downsample_to_weekly = data.groupby(data.index.to_period('W')).mean()
print("\n=== Printing Downsampled Record To A Weekly Frequency For Each Location ===")
print(downsample_to_weekly)

"""
Calculating the min, max, mean windspeeds and standard deviations of the windspeeds across all locations
for each week (assuming the first week starts on the 2nd of January 1961) for the first 52 weeks
"""
#Resampling data to 'W' week and use the functions
weekly = data.resample('W').agg(['min', 'max', 'mean', 'std'])

#Slicing it for the first 52 weeks and locations
weekly = weekly.loc[weekly.index[1:53], "RPT":"MAL"].head(10)

print("\n=== Printing Min, Max, Mean And Standard Deviations For The First 52 Weeks ===")
print(weekly)
