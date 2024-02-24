# Columbia AI Module 5 Challenge

## Requirements

### Combine and Clean the Data (15 points)
- [ ] The two DataFrames have been combined on the rows using an inner join and the index has been reset. (10 points)

- [ ] The "invoice_date" column has been converted to a datetime data type. (5 points)

### Determine which Region Sold the Most Products (15 points)
- [ ] A groupby or pivot_table function has been used to create a multi-index DataFrame with the "region", "state", and "city" columns. (10 points)

- [ ] The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)

- [ ] The results are sorted in ascending order to show the top five regions, including the state and city that sold the most products. (4 points)

### Determine which Region had the Most Sales (15 points)
- [ ] A groupby or pivot_table function has been used to create a multi-index DataFrame with the "region", "state", and "city" columns. (10 points)

- [ ] The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)

- [ ] The results are sorted in ascending order to show the top five regions, including the state and city that generated the most sales. (4 points)

### Determine which Retailer had the Most Sales (15 points)
- [ ] A groupby or pivot_table function has been used to create a multi-index DataFrame with the "retailer", "region", "state", and "city" columns. (10 points)

- [ ] The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)

- [ ] The results are sorted in ascending order to show the top five retailers along with their region, state, and city that generated the most sales. (4 points)

### Determine which Retailer Sold the Most Women's Athletic Footwear (20 points)
- [ ] A filtered DataFrame is created that shows only women's athletic footwear sales data. (8 points)

- [ ] A groupby or pivot_table function has been used to create a multi-index DataFrame with the "retailer", "region", "state", and "city" columns. (7 points)

- [ ] The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)

- [ ] The results are sorted in ascending order to show the top five retailers along with their region, state, and city that had the most women's athletic footwear sales. (4 points)

### Determine the Day with the Most Women's Athletic Footwear Sales (15 points)
- [ ] A pivot table is created that has the "invoice_date" column as the index and the "total_sales" column assigned to the values parameter. (10 points)

- [ ] The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)

- [ ] The resample function is used on the pivot table, the data is placed into daily bins, and the total sales for each day is calculated. (2 points)

- [ ] The results are sorted in ascending order to show the days that generated the most women's athletic footwear sales. (2 points)

### Determine the Week with the Most Women's Athletic Footwear Sales (5 points)
- [ ] The resample function is used on the pivot table, the data is placed into weekly bins, and the total sales for each week is calculated. (3 points)

- [ ] The results are sorted in ascending order to show the weeks that generated the most women's athletic footwear sales. (2 points)
