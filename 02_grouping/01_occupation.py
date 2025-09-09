import pandas as pd

#Read and assign data to variable 'users'
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'

users = pd.read_csv(url, sep='|', index_col='user_id')

print(users.head())

#Mean age per occupation
mean_ages = users.groupby('occupation').age.mean().sort_values(ascending=False)
print("\n=== Mean Ages Per Occupation ===")
print(mean_ages)

#Discover the male ratio per occupation - sorted from most to least

#Creating a function to numerise gender - Return 0 for female and 1 for male
def gender_to_numeric(x):
    if x == 'F':
        return 0
    if x == 'M':
        return 1

#Applying the function to the gender column and creating a new column
users['gender_n'] = users.gender.apply(gender_to_numeric)
#print(users.gender_n.head()) #Debug Line

male_ratio = users.groupby('occupation').gender_n.sum() / users.occupation.value_counts() * 100

#Sorting form most to least
sorted_male_ratio = male_ratio.sort_values(ascending=False)

print("\n=== Male Ratio Per Occupation ===")
print(sorted_male_ratio)

#Printing the min and max value for each occupation
min_max = users.groupby('occupation').age.agg(['min', 'max'])

print("\n=== Min and Max Ages For Each Occupation ===")
print(min_max)

#Calculating the mean age for each combination of occupation and gender
mean_age_occupation_gender = users.groupby(['occupation', 'gender']).age.mean()
print("\n=== Mean Age Per Combination Of Occupation and Gender ===")
print(mean_age_occupation_gender)

#Printing the percentage of women and men for each occupation

#Creating a dataframe and apply count to gender
gender_occupation = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})

#Creating a database and applying count to occupation
occupation_count = users.groupby('occupation').agg('count')

#Divide the gender_occupation per the occupation_count multiply by 100
occupation_gender = gender_occupation.div(occupation_count, level = 'occupation') * 100

#Present all rows from the gender column
occupation_gender_display = occupation_gender.loc[: , 'gender']
print("\n=== Displaying All Rows From The Gender Column ===")
print(occupation_gender_display)
