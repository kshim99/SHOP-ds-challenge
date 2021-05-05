import pandas as pd 
import numpy as np

##########
# a) Think about what could be going wrong with our calculation. Think about a better way to evaluate 
# this data. 
# From quickly sorting the dataset, we can see that there are some orders for 2000 shoes which result 
# in 704000 of `order_amount` per order, and this skews the average order amount to be abnormally large. 
# Note that `total_items` is different for each order. That is, each order may contain more than 1 pair of
# sneakers of the same type. 
 
dataset = pd.read_excel("2019 Winter Data Science Intern Challenge Data Set.xlsx")
print(np.mean(dataset['order_amount'])) # result in AOV of $3145.128 
print(dataset.sort_values(by=['order_amount', 'total_items']))

# I would divide the `order_amount` by `total_items` which is equal to price per a pair of shoes in the order, 
# then take the average of this per shoe price for each order. Note that each order can only have 1 type of 
# shoes, and there is usually no need for one customer to order the exact same shoes in more than 1 quantity.
# It is reasonable to assume that any customer ordering more than 1 unit is ordering for multiple people or 
# for retail purposes, so the `true average order value per final customer` would be better reflected with 
# above metric. 
 
########## 

##########
# b) What metric would you report for this dataset?
# I would report average of `order_amount/total_items = price of 1 pair of shoes in the order`. 
# As mentioned above, this metric better reflects the average order value per final customer. 
##########

##########
# c) What is its value?
per_item = dataset['order_amount']/dataset['total_items']
dataset['item_val'] = per_item

print(dataset)
print(np.mean(dataset['item_val']))
# A better way to evaluate AOV is to find the average of the price of 1 pair of shoes per order which 
# reflects the average order value per final customer. The value of this metrics is: 387.7428
########## 