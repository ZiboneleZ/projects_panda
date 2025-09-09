import pandas as pd


from regiment_raw_data import raw_data

regiment = pd.DataFrame(raw_data)
print(regiment)

#The mean preTestScore from the regiment Nighthawks
mean_nighthawks = regiment[regiment['regiment'] == 'Nighthawks'].groupby('regiment')['preTestScore'].mean()
#Repository code looks incorrect or not working, did not specify preTestScore
print("\n=== Printing Mean preTestScore From The Regiment Nighthawks ===")
print(mean_nighthawks)

#Present general statistics by company
general_stats = regiment.groupby('company').describe()
print("\n=== Printing General Statistics By Company ===")
print(general_stats)

#The mean of each company's preTestScore
company_mean_preTestScore = regiment.groupby('company')['preTestScore'].mean()
print("\n=== Printing The Mean Of Each Company's preTestScore ===")
print(company_mean_preTestScore)

#Presenting the mean preTestScores grouped by regiment and company
preTestScore_grouped_reg_comp = regiment.groupby(['regiment', 'company']).preTestScore.mean()
print("\n=== Printing Mean preTestScores Grouped by Regiment and Company ===")
print(preTestScore_grouped_reg_comp)

#Presenting the mean preTestScores grouped by regiment and company without heirarchical indexing
preTestScore_without_heirarchical_indexing = regiment.groupby(['regiment', 'company'])['preTestScore'].mean().unstack()
print("\n=== Printing Mean preTestScores Grouped by Regiment and Company w/out Heirarchical Indexing ===")
print(preTestScore_without_heirarchical_indexing)

#Group the entire dataframe by regiment and company
grouped_by_reg_comp = regiment.groupby(['regiment', 'company'])[['preTestScore', 'postTestScore']].mean()
print("\n=== Grouped The Entire DataFrame by Regiment and Company ===")
print(grouped_by_reg_comp)

#The Number Of Observations In Each Regiment and Company
observations_regiment_company = regiment.groupby(['regiment', 'company']).size()
print("\n=== Printing The Number of Observations In Each Regiment and Company ===")
print(observations_regiment_company)

#Iterating over a group and print the name and the whole data from the regiment

#Group dataframe by regiment, and for each regiment
print("\n=== Printing The DataFrame By Regiment, and For Each Regiment ===")
for name, group in regiment.groupby('regiment'):
    #Printing the name of the regiment
    print(name)
    #Printing the data of that regiment
    print(group)
