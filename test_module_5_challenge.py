import re

def search_file(file, pattern):
    content = open(file).read()
    if re.search(pattern, content, re.MULTILINE):
        return True
    return False

### Combine and Clean the Data (15 points)
def test_clean():
    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"df = pd\.concat\(\[df_2020, df_2021\], axis=\'rows\', join=\'inner\', ignore_index=True\)") == True, "The two DataFrames have been combined on the rows using an inner join and the index has been reset. (10 points)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"pd\.to_datetime\(df\[\'invoice_date\'\], format=\'%m\/%d\/%y\'\)") == True, "The 'invoice_date' column has been converted to a datetime data type. (5 points)"

### Determine which Region Sold the Most Products (15 points)
def test_region_products():
    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"df\.groupby\(\[\'region\', \'state\', \'city\'\]\)") == True, "A groupby or pivot_table function has been used to create a multi-index DataFrame with the 'region', 'state', and 'city' columns. (10 points)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"\.agg\(Total_Products_Sold=\(\'units_sold\', \'sum\'\)\)") == True, "The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)"

    # assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"\.agg\(\*\*\{{\'Total Products Sold\'\: \(\'units_sold\', \'sum\'\)\}}\)") == True, "The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"grouped_df\.sort_values\(by=\'Total_Products_Sold\', ascending=False, inplace=True\)") == True, "The results are sorted in descending order to show the top five regions, including the state and city that sold the most products. (4 points)"

### Determine which Region had the Most Sales (15 points)
def test_region_sales():
    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"df\.pivot_table\(index=\[\'region\', \'state\', \'city\'\], values=\'total_sales\', aggfunc=\'sum\'\)") == True, "A groupby or pivot_table function has been used to create a multi-index DataFrame with the 'region', 'state', and 'city' columns. (10 points)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"pivot_sales_df\.rename\(columns=\{{ \'total_sales\': \'Total Sales\' \}}, inplace=True\)") == True, "The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"pivot_sales_df\.sort_values\(by=\'Total Sales\', ascending=False, inplace=True\)") == True, "The results are sorted in descending order to show the top five regions, including the state and city that generated the most sales. (4 points)"

### Determine which Retailer had the Most Sales (15 points)
def test_retailer_sales():
    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"df\.groupby\(by=\[\'retailer\', \'region\', \'state\', \'city\'\]\)") == True, "A groupby or pivot_table function has been used to create a multi-index DataFrame with the 'retailer', 'region', 'state', and 'city' columns. (10 points)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf".agg\(\*\*\{{ \'Total Sales\': \(\'total_sales\', \'sum\'\) \}}\)") == True, "The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"retailer_grouped_df\.sort_values\(by=\'Total Sales\', ascending=False, inplace=True\)") == True, "The results are sorted in descending order to show the top five retailers along with their region, state, and city that generated the most sales. (4 points)"

### Determine which Retailer Sold the Most Women's Athletic Footwear (20 points)
def test_retailer_footwear():
    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"df\[df\[\'product\'\] == \\\"Women\'s Athletic Footwear\\\"\]") == True, "A filtered DataFrame is created that shows only women's athletic footwear sales data. (8 points)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"wfoot_df\.pivot_table\(index=\[\'retailer\', \'region\', \'state\', \'city\'\], values=\'units_sold\', aggfunc=\'sum\'\)") == True, "A groupby or pivot_table function has been used to create a multi-index DataFrame with the 'retailer', 'region', 'state', and 'city' columns. (7 points)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"pivot_wfoot_df\.rename\(columns=\{{ \'units_sold\': \'Womens_Footwear_Units_Sold\' \}}, inplace=True\)") == True, "The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"pivot_wfoot_df\.sort_values\(by=\'Womens_Footwear_Units_Sold\', ascending=False, inplace=True\)") == True, "The results are sorted in descending order to show the top five retailers along with their region, state, and city that had the most women's athletic footwear sales. (4 points)"

### Determine the Day with the Most Women's Athletic Footwear Sales (15 points)
def test_day_footwear():
    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"wfoot_df\.pivot_table\(index=\'invoice_date\', values=\'total_sales\', aggfunc=\'sum\'\)") == True, "A pivot table is created that has the 'invoice_date' column as the index and the 'total_sales' column assigned to the values parameter. (10 points)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"pivot_wfoot_sales_df\.rename\(columns=\{{ \'total_sales\': \'Total Sales\' \}}, inplace=True\)") == True, "The aggregated column has been renamed to reflect the aggregation of the data in the column. (1 point)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"pivot_wfoot_sales_df\.resample\(\'D\'\)\.sum\(\)") == True, "The resample function is used on the pivot table, the data is placed into daily bins, and the total sales for each day is calculated. (2 points)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"pivot_wfoot_day_df\.sort_values\(by=\'Total Sales\', ascending=False, inplace=True\)") == True, "The results are sorted in descending order to show the days that generated the most women's athletic footwear sales. (2 points)"

### Determine the Week with the Most Women's Athletic Footwear Sales (5 points)
def test_week_footwear():
    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"pivot_wfoot_sales_df\.resample\(\'W\'\)\.sum\(\)") == True, "The resample function is used on the pivot table, the data is placed into weekly bins, and the total sales for each week is calculated. (3 points)"

    assert search_file("athletic_sales_analysis_starter_code.ipynb", rf"pivot_wfoot_week_df\.sort_values\(by=\'Total Sales\', ascending=False, inplace=True\)") == True, "The results are sorted in ascending order to show the weeks that generated the most women's athletic footwear sales. (2 points)"

