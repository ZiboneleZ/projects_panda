import pandas as pd
import numpy as np

cars_one = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv')

cars_two = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv')

print(cars_one.head())

print()
    
print(cars_two.head())

#Getting rid of the unnamed blank columns
cars_one = cars_one.loc[:, 'mpg':'car']
print("\n=== Data Without The Unnamed Blank Columns ===")
print(cars_one.head())

#Getting the shape of both datasets
print("\n=== Shapes ===")
print(cars_one.shape, cars_two.shape)

#Joining cars_one and cars_two together into a single DataFrame called cars
cars = cars_one._append(cars_two)
print("\n=== Joining Cars into One DataFrame ===")
print(cars)

#Create a column called owners and fill it with random numbers from 15000 to 73000
cars['owners'] = np.random.randint(15000, high=73001, size=398, dtype='l')
print('\n=== Creating Column Called "owners" And Filled It With Data ===')
print(cars.head())
