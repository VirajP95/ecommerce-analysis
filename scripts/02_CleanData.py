import pandas as pd

df_raw = pd.read_csv("../data/raw/E-commerce raw data.csv", sep='\t')


#----------------Create a copy of raw data and clean on copied data
df_clean = df_raw.copy()

df_clean.head(5)

#----------------------Fix column names

df_clean.columns = df_clean.columns.str.lower().str.replace(' ', '_').str.strip()

print(df_clean.columns)

#----------------Change to correct data types

df_clean['unit_price'] = df_clean['unit_price'].str.replace(',','').str.replace('$','').astype(float)

df_clean['unit_price']

df_clean['order_id'] = df_clean['order_id'].astype(int)
df_clean['order_id'].dtype



#--------------------Fix date column
def fix_date(date_str):
    if pd.isnull(date_str):
        return pd.NaT
    if '/' in str(date_str):
        return pd.to_datetime(date_str, format='%d/%m/%Y')  
    else:
        return pd.to_datetime(date_str, format='%Y-%m-%d')  
    
df_clean['order_date'] = df_clean['order_date'].apply(fix_date)

df_clean['order_date']

df_clean['order_date'].isnull().sum()



#--------------------Fix text inconsistencies (Standardisation)

df_clean['customer_name'] = df_clean['customer_name'].str.strip().str.title()
df_clean['customer_name']

df_clean['region'] = df_clean['region'].str.strip().str.title()
df_clean['region']

df_clean['status'] = df_clean['status'].str.strip().str.lower()
df_clean['status']

#----------------------------Handle duplicates

df_clean = df_clean.drop_duplicates()

df_clean.duplicated().sum()

#----duplicate order_id only → same order with different values could mean system error or update
print(df_clean.duplicated(subset=['order_id']).sum()) 



#----------------------------Handle missing values

df_clean.isnull().sum()

df_clean[df_clean['unit_price'].isnull()] # this gives the entire row similar to WHERE clause in SQL


# Filling the missing unit_price of product with mean of the same category
df_clean['unit_price'] = df_clean.groupby('category')['unit_price'].transform(lambda x: x.fillna(x.median()))
df_clean['unit_price']

df_clean['region'] = df_clean['region'].fillna('unknown')

df_clean['email'] = df_clean['email'].fillna('no_email@unknown.com')
df_clean['email']

#---------------------------- Verify all the cleaning 

df_clean.isnull().sum()

df_clean.duplicated().sum()

df_clean.dtypes

df_clean.shape

























