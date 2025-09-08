import pandas as pd

from data_file import raw_data

#Creating a dataframe and assigning to variable: army
army = pd.DataFrame(data=raw_data)

print(army.head())

#Setting the 'origin' column as index
army.set_index('origin', inplace=True)

#Selecting the 'veterans' column only - sorted descending
print("\n=== Veterans From Most ===\n")
print(army.veterans.sort_values(ascending=False))

#Printing 'veterans' and 'deaths' columns
print("\n=== Veterans and Deaths ===\n")
print(army[['veterans', 'deaths']])

#Printing the name of all columns
print("\n=== All Column Names ===\n")
print(army.columns)

#Selecting the 'deaths', 'size', and 'deserters' columns for Maine and Alaska
print("\n=== Deaths, Size, and Deserters - Maine and Alaska ===\n")
deaths_size_deserters_maine_alaska = army.loc[['Maine', 'Alaska'], ['deaths', 'size', 'deserters']]
print(deaths_size_deserters_maine_alaska)

#Selecting rows 3 - 7 and columns 3 - 6
rows_and_columns = army.iloc[2:7, 2:6]
print("\n=== Rows 3 - 7 and Columns 3 - 6 === \n")
print(rows_and_columns)

#Selecting every row after the fourth row, and all columns
print("\n=== Rows After Fourth Row and All Columns ===\n")
print(army.iloc[4:, :])

#Selecting every row up to the fourth row and every column
print("\n=== Rows Up To The 4th, And All Columns ===")
print(army.iloc[:4, :])

#Selecting the 3rd Colmn Up To The 7th
print("\n=== Third Column Up To The Seventh Column ===")
print(army.iloc[:, 2:7])

#Selecting rows where deaths are greater than 50
print("\n=== Rows Where Deaths Are Greater Than 50 ===")
print(army[army.deaths > 50]) #Or army[army["deaths"] > 50]

#Printing rows where deaths are greater than 500 or less than 50
print("\n=== Rows with Deaths greater than 500 or less than 50 ===")
print(army[(army["deaths"] > 500) | (army["deaths"] < 50)])

#Selecting all the rows not named "Dragoons"
not_dragoons = army[army.regiment != "Dragoons"]
print("\n=== All Regiments Except Dragoons ===")
print(not_dragoons)

#Selecting only Texas and Arizona Rows
print("\n=== Texas an Arizona Rows Only ===")
print(army.loc[["Texas", "Arizona"], :])

#Selecting the 3rd cell in the row named "Arizona"
print("\n=== Third Cell In Column 'Arizona' ===")
print(army.loc[["Arizona"]].iloc[:, 2])

#Selecting the third cell down in column named "deaths"
print("\n=== Printing The Cell Down In Column Named Deaths ===")
print(army.loc[:, ["deaths"]].iloc[2])
