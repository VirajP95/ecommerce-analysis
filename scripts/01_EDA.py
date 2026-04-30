import pandas as pd

# -------------- Understand Data Structure

df_raw = pd.read_csv("../data/raw/E-commerce raw data.csv", sep='\t')

df_raw.head(5)

df_raw.shape

df_raw.columns.to_list

df_raw.dtypes

df_raw.describe()

# ------------------ Understand Data Quality

df_raw.isnull().sum()
df_raw.isnull().sum()/len(df_raw) * 100

df_raw.duplicated().sum()
df_raw.duplicated(subset=["order_id"]).sum() # 2 duplicate orders were found

unique_regions = df_raw['region'].unique()
unique_regions

status_counts = df_raw['status'].value_counts()
status_counts

df_raw['unit_price'].astype

df_raw['customer_name'].nunique()

#------------Understand Data distribution (Do this in EDA2 after data is cleaned)

orders_per_region = df_raw['region'].value_counts()
orders_per_region

orders_per_category = df_raw['category'].value_counts()
orders_per_category

df_raw['order_date']






