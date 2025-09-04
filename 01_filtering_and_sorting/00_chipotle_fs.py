import pandas as pd

#Assigning dataset to variable called "chipo"
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"

chipo = pd.read_csv(url, sep='\t')

print(chipo.head())

#=== How many products cost more than $10.00 ===
#Cleaning the item price column and converting it into a float
prices = [float(value[1:-1]) for value in chipo.item_price]

#Reassigning columns with cleaned prices
chipo.item_price = prices

#Deleting duplicates in item_name and quantity
chipo_filtered = chipo.drop_duplicates(['item_name', 'quantity', 'choice_description'])
print(chipo_filtered)
#Just visually comparing the two tails - I'm hoping they will be different, so I can quickly assume correctness
print(chipo.tail())

#Selecting only the products with quantity equals to 1
chipo_one_product = chipo_filtered[(chipo_filtered.quantity == 1) & (chipo_filtered.item_price > 10)] #Had to improvise here - Solution code was populating incorrectly
print(chipo_one_product)

#chipos = chipo_one_product[chipo_one_product['item_price'] > 10].item_name.nunique()
#chipos = chipo_one_product[chipo_one_product['item_price']>10]
#print(chipos)

#chipos = chipo.query('item_price > 10.00').item_name.nunique() #In the execise solutions it says 'price_per_item'
#print(chipos)

#=== 5. What is the price of each item? ===
#Delete the duplicates in item_name and quantity

#chipo_filtered = chipo.drop_duplicates(['item_name', 'quantity'])
chipo_filtered = chipo[(chipo['item_name'] == 'Chicken Bowl') & (chipo['quantity'] == 1)]
print(chipo_filtered)

#Sorting by name of the item
print("\n === Values Sorted By Item Name ===\n")
by_item = chipo.item_name.sort_values() #Or chipo.sort_values(by = 'item_name')
print(by_item)

#Quantity of the most expensive item ordered
expensive_item_quantity = chipo.sort_values(by = 'item_price', ascending=False).head(1)
print("\n=== Quantity of the most expensive item ordered ===\n")
print(expensive_item_quantity)

#How many times was the Chicken Salad Bowl ordered?
chicken_salad_bowl = chipo[chipo.item_name == 'Chicken Salad Bowl']
print("\n=== Chicken Bowl Salad Ordered Amount ===\n")
print(len(chicken_salad_bowl))

#How many times was the Canned Soda ordered more than once at a time
canned_soda_over_one = chipo[(chipo.item_name == 'Canned Soda') & (chipo.quantity > 1)]
print("\n=== Canned Soda Ordered More Than Once By Customer ===\n")
print(len(canned_soda_over_one))