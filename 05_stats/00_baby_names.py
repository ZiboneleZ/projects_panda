import pandas as pd

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'

baby_names = pd.read_csv(url)

print(baby_names.head())

print(baby_names.shape)

print(baby_names.info())

#Printing the first 10 entries
print(baby_names.head(10))

#Deleting the columns 'Unnamed' and 'Id' 
del baby_names['Unnamed: 0']
print("\n=== Deleting 'Unnamed: 0' Colum ===")

from time import sleep
sleep(2)

del baby_names['Id']
print("\n=== Deleting 'Id' Column ===")
sleep(2)

print("\n=== 'Unnamed: 0' and 'Id' Columns Deleted Successfully! ===\n")
print(baby_names.sort_values(by='Count', ascending=False).head())

#Calculating the males vs the females in the dataset
genders = baby_names['Gender'].value_counts()
print("\n=== Calculating The Number Of Each Gender ===")
print(genders)

#Grouping the dataset by 'name' and assign it to variable 'names'
#Delete the column year - not needed

del baby_names['Year']

names = baby_names.groupby("Name").sum()
print("\n=== Baby Names Grouped by Name ===")
print(names.Count.head())

#Printing the sie of the dataset
print("\n=== Size of Dataset ===")
print(names.shape)

#Sorting the dataset from big to small
names = names.sort_values("Count", ascending=0)
print("\n=== Baby Names by Most Used To Least ===")
print(names['Count'].head())
#print(names.info())

#=== How many different names are there in the dataset ===
#Because we have already grouped by names, the names are already unique
#We will get the length of names
unique_names = len(names)
print("\n=== Number of Unique Names In The Dataset ===")
print(unique_names)

#The name with the most occurences
most_used_name = names.Count.idxmax() #names[names.Count == names.Count.max()]
print("\n=== Most Used Name ===")
print(most_used_name)

#The list of names with the least occurences
least_used_names = names[names.Count == names.Count.min()]
print("\n=== Number Of Least Used Names ===")
print(len(least_used_names))

#The median name occurence
median_name_occ = names[names['Count'] == names.Count.median()]
print("\n=== Median Name Occurence ===")
print(median_name_occ['Count'])

#The standard deviation of names
standard_deviation = names.Count.std()
print("\n=== Stadard Deviation Of Names ===")
print(standard_deviation)

#Getting a summary with the mean, min, max and quartiles
summary = names.describe()
print("\n=== Getting Summary with Mean, Min, Max and Quartile ===")
print(summary)
