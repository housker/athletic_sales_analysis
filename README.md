# Columbia AI Module 5 Challenge

## Requirements

### Combine and Clean the Data (15 points)
- [X] The two DataFrames have been combined on the rows using an inner join and the index has been reset. (10 points)

- [X] The "invoice_date" column has been converted to a datetime data type. (5 points)

### Determine which Region Sold the Most Products (15 points)
- [X] A groupby or pivot_table function has been used to create a multi-index DataFrame with the "region", "state", and "city" columns. (10 points)

- [X] The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)

- [X] The results are sorted in descending (note: instructions read "ascending", but given [example](https://bootcampspot.instructure.com/courses/4996/assignments/66998#submit:~:text=has%20been%20changed.-,Determine%20which%20Region%20Sold%20the%20Most%20Products,-Use%20either%20the), that appears to be a typo) order to show the top five regions, including the state and city that sold the most products. (4 points)

### Determine which Region had the Most Sales (15 points)
- [X] A groupby or pivot_table function has been used to create a multi-index DataFrame with the "region", "state", and "city" columns. (10 points)

- [X] The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)

- [X] The results are sorted in descending (note: instructions read "ascending", but given [example](https://bootcampspot.instructure.com/courses/4996/assignments/66998#submit:~:text=the%20following%20image%3A-,Determine%20which%20Region%20had%20the%20Most%20Sales,-Use%20either%20the), that appears to be a typo) order to show the top five regions, including the state and city that generated the most sales. (4 points)

### Determine which Retailer had the Most Sales (15 points)
- [X] A groupby or pivot_table function has been used to create a multi-index DataFrame with the "retailer", "region", "state", and "city" columns. (10 points)

- [X] The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)

- [X] The results are sorted in descending (note: instructions read "ascending", but given [example](https://bootcampspot.instructure.com/courses/4996/assignments/66998#submit:~:text=the%20following%20image%3A-,Determine%20which%20Retailer%20had%20the%20Most%20Sales,-Use%20either%20the), that appears to be a typo) order to show the top five retailers along with their region, state, and city that generated the most sales. (4 points)

### Determine which Retailer Sold the Most Women's Athletic Footwear (20 points)
- [X] A filtered DataFrame is created that shows only women's athletic footwear sales data. (8 points)

- [X] A groupby or pivot_table function has been used to create a multi-index DataFrame with the "retailer", "region", "state", and "city" columns. (7 points)

- [X] The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)

- [X] The results are sorted in descending (note: instructions read "ascending", but given [example](https://bootcampspot.instructure.com/courses/4996/assignments/66998#submit:~:text=the%20following%20image%3A-,Determine%20which%20Retailer%20Sold%20the%20Most%20Women%27s%20Athletic%20Footwear,-Filter%20the%20combined), that appears to be a typo) order to show the top five retailers along with their region, state, and city that had the most women's athletic footwear sales. (4 points)

### Determine the Day with the Most Women's Athletic Footwear Sales (15 points)
- [X] A pivot table is created that has the "invoice_date" column as the index and the "total_sales" column assigned to the values parameter. (10 points)

- [X] The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)

- [X] The resample function is used on the pivot table, the data is placed into daily bins, and the total sales for each day is calculated. (2 points)

- [X] The results are sorted in descending (note: instructions read "ascending", but given [example](https://bootcampspot.instructure.com/courses/4996/assignments/66998#submit:~:text=the%20following%20image%3A-,Determine%20the%20Day%20with%20the%20Most%20Women%27s%20Athletic%20Footwear%20Sales,-Create%20a%20pivot), that appears to be a typo) order to show the days that generated the most women's athletic footwear sales. (2 points)

### Determine the Week with the Most Women's Athletic Footwear Sales (5 points)
- [X] The resample function is used on the pivot table, the data is placed into weekly bins, and the total sales for each week is calculated. (3 points)

- [X] The results are sorted in descending (note: instructions read "ascending", but given [example](https://bootcampspot.instructure.com/courses/4996/assignments/66998#submit:~:text=the%20following%20image%3A-,Determine%20the%20Week%20with%20the%20Most%20Women%27s%20Athletic%20Footwear%20Sales,-Apply%20resample%20to), that appears to be a typo) order to show the weeks that generated the most women's athletic footwear sales. (2 points)
