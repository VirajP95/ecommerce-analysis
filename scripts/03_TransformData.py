import pandas as pd

df_cleaned = pd.read_csv("../data/clean/Cleaned_Data.csv")

df_cleaned.shape
df_cleaned.columns



# After cleaning, date data type is back to orignal value. Convert it to date_time type again
df_cleaned['order_date'] = pd.to_datetime(df_cleaned['order_date'])
df_cleaned.dtypes




#-----------------------Create new required caluculated columns
df_cleaned['revenue'] = df_cleaned['unit_price'] * df_cleaned['units_sold']
df_cleaned['revenue']

df_cleaned['revenue_tier'] = pd.cut(df_cleaned['revenue'], bins= [0, 1000, 3000, 99999], 
                                    labels= ['Low','Medium','High'])
df_cleaned['revenue_tier']

df_cleaned['is_completed'] = df_cleaned['status'] == 'completed'

df_cleaned.head()



#-----------------------Extract important date parts

# get month number from order_date
df_cleaned['month'] = df_cleaned['order_date'].dt.month
df_cleaned['month']

# get month name from order_date 
df_cleaned['month_name'] = df_cleaned['order_date'].dt.month_name()
df_cleaned['month_name']

# get Quarter from order_date
df_cleaned['quarter'] = 'Q' + df_cleaned['order_date'].dt.quarter.astype(str)
df_cleaned['quarter']

# get day name order was placed on (Was the order placed on weekday?)
df_cleaned['day_of_week'] = df_cleaned['order_date'].dt.day_name()
df_cleaned['day_of_week']




#----------------------------Reshape Data

# Create Pivot table
pivot_table = df_cleaned.pivot_table(values= 'revenue', index= 'region', columns='category', aggfunc='sum', fill_value= 0)
pivot_table

# Melted format of pivot table is converting back to table format like excel
# Useed when feeding data into seaborn charts, Power BI, or SQL — most tools prefer long format.
pivot_table_melted_format = pivot_table.reset_index().melt(id_vars='region', var_name='category', value_name= 'revenue')
pivot_table_melted_format

df_cleaned.head()










