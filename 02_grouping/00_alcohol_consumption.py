import pandas as pd

#Reading and displaying data
drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')

print(drinks.head())

#Continent that drinks more wine on average
wine_average = drinks.groupby('continent').wine_servings.mean()
print("\n=== Wine Servings Average By Continent ===")
print(wine_average)

#Printing the statistics for wine consumption for each continent
wine_statistics = drinks.groupby('continent').wine_servings.describe()
print("\n=== Printing Stats For Wine Consumption By Continent ===")
print(wine_statistics)

#Printing the mean alcohol consupmtion per continent for every column
mean_alcohol_consumption = drinks.iloc[:, 1:].groupby('continent').mean() 
#drinks.groupby('continent').mean() didnt work, so I used previous lessons
print("\n=== Printing Average Alcohol Consumption ===")
print(mean_alcohol_consumption)

#Printing the median alcohol consumption per continent for every column
median_alcohol_consumption = drinks.iloc[:, 1:].groupby('continent').median()
print("\n=== Printing Median Alcohol Consumption ===")
print(median_alcohol_consumption)

#Printing Alcohol Consumption In Africa - Not in exercise, was just curious
alcohol_consumption_africa = drinks[drinks['continent'] == 'AF']
print("\n=== Printing The Top 10 Countries In Africa By Beer Serving")
print(alcohol_consumption_africa.sort_values(by = 'beer_servings', ascending=False).head(10))

#Printing mean, min, and max values for spirit consumption
mean_min_max = drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max'])
print("\n=== Printing The Mean, Min, Max Values Of Spirit Consumption ===")
print(mean_min_max)
