import pandas as pd

#Assigning to varible called "users" and use the user_id as index
users = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user", sep="|", index_col='user_id')

print(users.head(10))

print(users.tail(10))

#Number of observations in the dataset
print(f"\nObservations shape: {users.shape[0]}")

#Number of columns in the dataset
print(f"\nColumns shape: {users.shape[1]}\n")

#Print the name of all columns
print(users.columns)

#How the data is indexed
print(users.index)

#Print datatype of each columns
print(users.dtypes)

#Print only the occupation column
print(users.occupation) #Or users['occupation']

#Number of different occupations in the dataset
print(f"\nNumber of different occupations: {users.occupation.nunique()}\n") #Or by using value_counts() - users.occupation.value_counts().count()

#The most frequent occupation
print(f"Most Frequent Occupation: {users.occupation.value_counts().head(1).index[0]}")

#Top five occupations
print("\nTop Five Occupations:")
print(users.occupation.value_counts().head())

#Summarizing the DataFrame
print(users.describe())

#Summarizing all columns
print(users.describe(include = "all"))

#Summarize only the occupation column
print(users.occupation.describe())

#Print Mean Age Of Users
print(f"\nThe mean age of users is: {round(users.age.mean())}")

#Printing age with least occurence
print("\nAges with the least occurence: \n")
print(users.age.value_counts().tail())