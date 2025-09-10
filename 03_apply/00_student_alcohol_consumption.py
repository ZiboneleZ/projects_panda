import pandas as pd
#import numpy as np

#Reading and assigning the dataset to variable called 'df' 
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(url)

print("\n=== Dataset Head ===")
print(df.head())

#Slicing the dataframe from shool to guardian columns
student_alcohol = df.loc[:, 'school':'guardian']
print("\n=== Printing Head - School to Guardian Columns Only ===")
print(student_alcohol.head())

#Creating a lambda function that will capitalise strings
capitaliser = lambda x: x.capitalize()

#Capitalizing both Mjob and Fjob
student_alcohol['Mjob'] = student_alcohol['Mjob'].apply(capitaliser)
student_alcohol['Fjob'] = student_alcohol['Fjob'].apply(capitaliser)

print("\n=== Capitalized Mjob and Fjob Columns ===")
print(student_alcohol.head())

#Printing Dataset Tail
print("\n=== Dataset Tail ===")
print(student_alcohol.tail())

#Creating a function called 'majority' that returns a boolean value to a new column called "legal drinker"
def majority(x):
    if x > 17:
        return True
    else:
        return False

student_alcohol['legal_drinker'] = student_alcohol['age'].apply(majority)

print("\n === Legal Drinkers ===")
print(student_alcohol.head())

#Multiplying every number by 10 in the dataset
def multiplier(x):
    if type(x) is int:
        return x * 10
    return x

multiplied_dataset = student_alcohol.applymap(multiplier)
print("\n=== Dataset With Numbers Multiplied By 10 ===")
print(multiplied_dataset)

