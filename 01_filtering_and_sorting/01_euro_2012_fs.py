import pandas as pd

#Fetch the data and give it a variable

euro_2012 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv", sep=',')
print(euro_2012.head())

#Selecting the goal column only
print("\n=== Goals Column Only ===\n")
print(euro_2012.Goals)

#Total Number of Teams That Participated
total_teams = euro_2012.shape[0]
print("\n=== Teams Participated Total ===\n")
print(total_teams)

#The number of columns in the dataset
print("\n=== Number of Columns ===\n")
print(euro_2012.info())

#Assign columns Teams, Yellow Cards,and Red Cards to dataframe "discipline"
discipline = euro_2012[['Team', 'Yellow Cards', 'Red Cards']]
print("\n=== Discipline ===\n")
print(discipline)

#Sort the teams by Red Cards, Then by Yellow Cards
sorted_by_reds = discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)
print("\n=== Sorted by Red Cards and Yellow Cards ===\n")
print(sorted_by_reds)

#Calculating the mean Yellow Cards given per team
yellows_given_per_team = round(discipline['Yellow Cards'].mean())
print("\n=== Yellow Cards Mean Given Per Team ===\n")
print(yellows_given_per_team)

#Filter only teams than scored more than 5 goals
more_than_five_goals = euro_2012[euro_2012.Goals > 5]
print("\n=== Teams that scored than 5 goals ===\n")
print(more_than_five_goals)

#Selecting teams that start with "C"
starts_with_c = euro_2012[euro_2012.Team.str.startswith('C')]
print("\n=== Teams that start with letter 'C' ===\n")
print(starts_with_c)

#Selecting the first five columns
first_five_columns = euro_2012.iloc[:, 0:5]
print("\n=== First Five Columns ===\n")
print(first_five_columns)

#Selecting all columns except the last 4
exclude_last_four = euro_2012.iloc[:, :-4]
print("\n=== All columns except the last 4 ===\n")
print(exclude_last_four)

#Presenting only the Shooting Accuracy of only Italy, Croatia, and England
shooting_acc = euro_2012.loc[euro_2012.Team.isin(['Italy', 'Croatia', 'England']), ['Team', 'Shooting Accuracy']]
print("\n=== Shooting Accuracy For The 3 Teams - Croatia, England, and Italy ===\n")
print(shooting_acc)

