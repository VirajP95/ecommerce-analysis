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


# ---------------------(This provided info that there are 2 prices for laptop)
avg_unit_price = df_cleaned.groupby('product')['unit_price'].mean().sort_values(ascending=False).round(2).reset_index()
avg_unit_price


Each_product_cost = df_cleaned[['product','unit_price']].drop_duplicates().sort_values('unit_price',ascending=False).reset_index()
Each_product_cost

category__rev_perc = df_cleaned.groupby('category')['revenue'].sum()
perc = (category__rev_perc/category__rev_perc.sum() * 100).round(1)
perc

# Advanced Analysis

customer_rank = df_cleaned.groupby('customer_name')['revenue'].sum().reset_index()
customer_rank['rank'] = customer_rank['revenue'].rank(method='dense', ascending=False).astype(int)
customer_rank = customer_rank.sort_values('rank').reset_index(drop=True)
customer_rank

region_rev = df_cleaned.groupby(['region','product'])['revenue'].sum().reset_index()
top_per_region = (region_rev
                  .sort_values('revenue', ascending=False)
                  .groupby('region')
                  .first()
                  .reset_index()
                  )
top_per_region

completion_rate = (df_cleaned.groupby('region')['is_completed']
              .mean() * 100).round(1).reset_index()
completion_rate.columns = ['region','completion_rate %']
completion_rate['completion_rate %'] = completion_rate['completion_rate %'].apply(lambda x: f"{x:.1f}%")
completion_rate

avg_spenders = df_cleaned.groupby('customer_name')['revenue'].sum().mean()
high_spenders = df_cleaned.groupby('customer_name')['revenue'].sum()

spenders_result = high_spenders[high_spenders > avg_spenders].sort_values(ascending=False).reset_index()
spenders_result

#----------------------























