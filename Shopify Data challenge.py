import pandas as pd 
import numpy as np

dataset = pd.read_excel("2019 Winter Data Science Intern Challenge Data Set.xlsx")

##########
# a) Think about what could be going wrong with our calculation. Think about a better way to evaluate 
# this data. 
print(np.mean(dataset['order_amount'])) # result in AOV of $3145.128 

print(dataset.sort_values(by=['order_amount', 'total_items']))
# From quickly sorting the dataset, we can see that there are some orders for 2000 shoes 
# which result in 704000 of order_amount per order, and this skews the average order amount 
# to be abnormally large.
# Note that total_items is different for each order. That is, each order may contain more than 
# 1 pair of sneakers of the same type. I would divide the order_amount by total_items which is 
# equal to price per shoe in the order, and then take the average of this per shoe price for each 
# order.
# Note that each order can only have 1 type of shoes, and there is usually no need for one customer
# to order the exact same shoes in more than 1 quantity. It is reasonable to assume that any customer
# ordering more than 1 unit is ordering for multiple people or for retail purposes, so the true 
# average order value per final customer would be better reflected with above metric. 
########## OUTPUT BELOW
'''
3145.128
      order_id  shop_id  user_id  order_amount  total_items payment_method              created_at
1            2       92      925            90            1           cash 2017-03-03 17:38:51.999
158        159       92      795            90            1    credit_card 2017-03-29 03:07:12.224
228        229       92      757            90            1          debit 2017-03-13 23:57:51.040
322        323       92      783            90            1          debit 2017-03-08 03:49:15.321
590        591       92      967            90            1          debit 2017-03-28 22:56:22.880
...        ...      ...      ...           ...          ...            ...                     ...
3332      3333       42      607        704000         2000    credit_card 2017-03-24 04:00:00.000
4056      4057       42      607        704000         2000    credit_card 2017-03-28 04:00:00.000
4646      4647       42      607        704000         2000    credit_card 2017-03-02 04:00:00.000
4868      4869       42      607        704000         2000    credit_card 2017-03-22 04:00:00.000
4882      4883       42      607        704000         2000    credit_card 2017-03-25 04:00:00.000

[5000 rows x 7 columns]
'''
##########
# b) What metric would you report for this dataset?
# 
# I would report average of order_amount/total_items = price of 1 pair of shoes in the order. 
##########

##########
# c) What is its value?
per_item = []

for i in range(len(dataset)):
    per_item.append(dataset['order_amount'][i]/dataset['total_items'][i])
dataset['item_val'] = per_item

print(dataset)
print(np.mean(dataset['item_val']))
print("A better way to evaluate AOV is to find the average of 1 shoe value per order.")
print("The value of this metrics is: ", np.mean(dataset['item_val']))
########## OUTPUT BELOW
'''  
order_id  shop_id  user_id  order_amount  total_items payment_method                    created_at  item_val
0            1       53      746           224            2           cash 2017-03-13 12:36:56.190     112.0
1            2       92      925            90            1           cash 2017-03-03 17:38:51.999      90.0
2            3       44      861           144            1           cash 2017-03-14 04:23:55.595     144.0
3            4       18      935           156            1    credit_card 2017-03-26 12:43:36.649     156.0
4            5       18      883           156            1    credit_card 2017-03-01 04:35:10.773     156.0
...        ...      ...      ...           ...          ...            ...                     ...       ...
4995      4996       73      993           330            2          debit 2017-03-30 13:47:16.597     165.0
4996      4997       48      789           234            2           cash 2017-03-16 20:36:16.389     117.0
4997      4998       56      867           351            3           cash 2017-03-19 05:42:42.228     117.0
4998      4999       60      825           354            2    credit_card 2017-03-16 14:51:18.188     177.0
4999      5000       44      734           288            2          debit 2017-03-18 15:48:18.205     144.0

[5000 rows x 8 columns]
387.7428
A better way to evaluate AOV is to find the average of 1 shoe value per order.
The value of this metrics is:  387.7428
'''