# Shopify Data Science Intern Challenge 

## Question 1

### a) Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 

### b) What metric would you report for this dataset?

### c) What is its value? 


## Question 2

### a) How many orders were shipped by Speedy Express in total?

```sql
SELECT Count(orderid)
FROM   orders
WHERE  shipperid = (SELECT shipperid
                    FROM   shippers
                    WHERE  shippername = 'Speedy Express') 
```
> Speedy Express shipped 54 orders in total.

### b) What is the last name of the employee with the most orders?

```sql
SELECT lastname,
       Max(mycount)
FROM   (SELECT lastname,
               Count(orderid) mycount
        FROM   orders
               INNER JOIN employees
                       ON orders.employeeid = employees.employeeid
        GROUP  BY lastname) 
```

> Employee with last name Peacock has the most orders with 40 orders. 

### c) What product was ordered the most by customers in Germany? 

```sql
SELECT productname,
       Max(myquant)
FROM   (SELECT productname,
               Sum(quantity) myquant
        FROM   orders
               INNER JOIN orderdetails
                       ON orders.orderid = orderdetails.orderid
               INNER JOIN customers
                       ON orders.customerid = customers.customerid
               INNER JOIN products
                       ON orderdetails.productid = products.productid
        WHERE  country = 'Germany'
        GROUP  BY productname) 
```

> Customers in Germany ordered Boston Crab Meat the most, withe total quantity ordered of 160 units.