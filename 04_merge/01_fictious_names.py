import pandas as pd

#Data to create dataframes from 
raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

data_one = pd.DataFrame(raw_data_1, columns=['subject_id', 'first_name', 'last_name'])
data_two = pd.DataFrame(raw_data_2, columns=['subject_id', 'first_name', 'last_name'])
data_three = pd.DataFrame(raw_data_3, columns=['subject_id', 'test_id'])

#Printing data_one head
print("\n=== Data One Head ===")
print(data_one.head())
print("\n=== Data Three Head ===")
print(data_three.head())

#Combining data_one and data_two into all_data
all_data = pd.concat([data_one, data_two])  #data_one._append(data_two)
print("\n=== Prnting All Data ===")
print(all_data)

#Joining the two dataframes along columns and assign it to all_data_col
all_data_col = pd.concat([data_one, data_two], axis=1)
print("\n=== Joining The Two DataFrames Along Columns ===")
print(all_data_col)

#Printing data_three
print("\n=== Data Three ===")
print(data_three)

#Merging all_data and data_three along the subject_id value
merged_data = pd.merge(all_data, data_three, on='subject_id')
print("\n=== Merging all_data And data_three On subject_id ===")
print(merged_data)

#Merging only the subject that have the same id in both data_one and data_two
same_sub_id = pd.merge(data_one, data_two, on='subject_id', how='inner')
print("\n=== Subject With The Same ID From data_one And data_two ===")
print(same_sub_id)

#Merging all values from data_one and data_two, with matching records from both sides where available
matching_records = pd.merge(data_one, data_two, on='subject_id', how='outer')
print("\n=== Values From Both Data Sets With Matching Records ===")
print(matching_records)
