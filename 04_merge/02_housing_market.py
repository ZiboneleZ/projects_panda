import pandas as pd
import numpy as np

"""
Creating three different Series, each of length 100 as follows:
1. The first a random number from 1 to 4
2. The second a random number from 1 to 3
3. The third a random number from 10,000 to 30,000
"""

series_one = pd.Series(np.random.randint(1, high=5, size=100, dtype='l'))
series_two = pd.Series(np.random.randint(1, high=4, size=100, dtype='l'))
series_three = pd.Series(np.random.randint(10000, high=30001, size=100, dtype='l'))

#Series One
print("\n=== Series One ===")
print(series_one)

#Series Two
print("\n=== Series Two ===")
print(series_two)

#Series Three
print("\n=== Series Three ===")
print(series_three)

#Creating a dataframe by joining the series by column
house_market = pd.concat([series_one, series_two, series_three], axis=1)
print("\n=== Creating A DataFrame By Joining Series By Column ===")
print(house_market.head())
    
#Changing column names two bedrooms, bathrooms, and price_sqr_meter
house_market.rename(columns = {0 : 'bedrooms', 1 : 'bathrooms', 2 : 'price_sqr_meter'}, inplace=True)
print("\n=== Renaming Column Names ===")
print(house_market.head())

#Creating one column dataframe with the values of three series and assign it to 'bigcolumn'
bigcolumn = pd.concat([series_one, series_two, series_three], axis=0)
print("\n=== Column With All Three ===")
print(bigcolumn)
print("\n=== Data Type To Bigcolumn ===")
print(type(bigcolumn))

#Converting series to dataframe
bigcolumn = bigcolumn.to_frame()
print("\n=== Converting Series To DataFrame ===")
print(type(bigcolumn))

#Re_indexing the dataframe so that it goes form 0 to 299
bigcolumn.reset_index(drop=True, inplace=True)
print("\n=== Resetting Index To Go From 0 to 299 ===")
print(bigcolumn)
