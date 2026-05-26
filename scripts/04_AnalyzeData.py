import pandas as pd

df_cleaned = pd.read_csv("../data/clean/Cleaned_Data.csv")

df_cleaned.head()

# Revenue Analysis

total_revenue = df_cleaned['revenue'].sum()
total_revenue

total_revenue_per_region = df_cleaned.groupby('region')['revenue'].sum().sort_values(ascending=False)
total_revenue_per_region

total_revenue_per_category = df_cleaned.groupby('category')['revenue'].sum()
total_revenue_per_category

average_order_value = df_cleaned['revenue'].mean()
average_order_value

average_order_value2 = df_cleaned['revenue'].median()
average_order_value2

expensive_order = df_cleaned.nlargest(1, 'revenue')[['order_id', 'customer_name', 'product', 'revenue']]
expensive_order


# Customer Analysis

top_5_customers_by_revenue = df_cleaned.groupby('customer_name')['revenue'].sum().nlargest(5)
top_5_customers_by_revenue

count_of_orders_by_each_customer = df_cleaned.groupby('customer_name')['order_id'].count().sort_values(ascending=False)
count_of_orders_by_each_customer

Cust_avg_order_value = df_cleaned.groupby('customer_name')['revenue'].mean().sort_values(ascending=False)
Cust_avg_order_value

customer_statuses = df_cleaned.groupby('customer_name')['status'].unique()

both_statuses = customer_statuses[customer_statuses.apply(lambda x: 'completed' in x and 'pending' in x)]

both_statuses

# Time Analysis

revenue_per_month = df_cleaned.groupby('month')['revenue'].sum().reset_index()
revenue_per_month

monthly_orders_count = df_cleaned.groupby('month')['order_id'].count().idxmax()
monthly_orders_count

# -------------------------  Month to Month growth %
monthly_growth = df_cleaned.groupby('month')['revenue'].sum().reset_index()
monthly_growth['mom_growth'] = monthly_growth['revenue'].pct_change() * 100
monthly_growth['mom_growth'] = monthly_growth['mom_growth'].round(2)
monthly_growth

# ------------------------- 2 month rolling average
rolling_2month_avg = monthly_growth['revenue'].rolling(2).mean()
rolling_2month_avg


# Product Analysis


most_units_sold= df_cleaned.groupby('product')['units_sold'].sum().sort_values(ascending=False).reset_index()
most_units_sold

avg_unit_price = df_cleaned.groupby('product')['unit_price'].mean().sort_values(ascending=False).round(2).reset_index()
avg_unit_price

Each_product_cost = df_cleaned[['product','unit_price']].drop_duplicates().sort_values('unit_price',ascending=False).reset_index()
Each_product_cost







