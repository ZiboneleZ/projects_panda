import pandas as pd
import numpy as np

#Fetching the data

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url, sep='\t')

print(chipo.head(10))

#Number of observations in the dataset
print(f"\nNumber of observations: {chipo.shape[0]}\n")
print(chipo.info())

#Number of columns in the dataset
print(f"\nNumber of columns: {chipo.shape[1]}")

#Printing the names of all columns
print(f"\nColumn names:\n{chipo.columns}")

#How the dataset is indexed
print(f"\n{chipo.index}\n")

#The most ordered item
c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
print(c.head(1))

#The most ordered item in the choice_description column
c = chipo.groupby('choice_description').sum()
c = c.sort_values(['quantity'], ascending=False)
print(c.head(1))

#Total number of ordered items
total_number_ordered = chipo.quantity.sum()
print(f"\nTotal Items Ordered: {total_number_ordered}\n")

#---Converting item price into float---
#Check the item price type
print(f"Item price datatype is: {chipo.item_price.dtype}")

#Creating a lambda function to convert price into float
from time import sleep
print("=== Converting Item Price Datatype ===")
dollarizer = lambda x: float(x[1: -1])
chipo.item_price = chipo.item_price.apply(dollarizer)
sleep(2)

#Confirm the item price changes into float
print(f"\nItem price data type is now: {chipo.item_price.dtype}")

#Calculating the total revenue for the period in the dataset
revenue = (chipo.quantity * chipo.item_price).sum()
#print(f"\nTotal Revenue: {revenue}")
print('\nRevenue was $' + str(np.round(revenue,2)))

#Calculating orders made in that period
orders = chipo.order_id.value_counts().count()
print(f"\nOrders made: {orders}")

'''
#Calculating average revenue amount per order - Solution 1 - !Working
chipo['revenue'] = chipo['quantity'] * chipo['item_price']
order_grouped = chipo.groupby(by=['order_id']).sum()
order_grouped = order_grouped.mean()['revenue']
print(f"\nAverage Revenue Per Order: {order_grouped}")


#Calculating average revenue - Solution 2 - Also !working - Will Sort It Myself
order_group = chipo.groupby(by=['order_id']).sum().mean()['revenue']
print(order_group)
'''

#Number of different items sold
diff_items_sold = chipo.item_name.value_counts().count()
print(f"\nDifferent items sold: {diff_items_sold}")
