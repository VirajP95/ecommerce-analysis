import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/clean/Cleaned_Data.csv")
df.head()


# 1 ----------------------- Distibution Charts -----------------------------------


# Histogram of revenue distribution. With KDE curve

sns.histplot(data=df, x="revenue", bins=20, kde=True)

plt.title("Revenue Distribution")
plt.show()

 # Box plot showing revenue spread by region
 
sns.boxplot(data=df, x="region", y="revenue")

plt.title("Revenue By Region", fontsize = 14)
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.show()


# Box plot showing revenue by category

sns.boxplot(data=df, x="category", y="revenue")

plt.title("Revenue By Category")
plt.xlabel("category")
plt.ylabel("Revenue")
plt.show()
 

# 2 ----------------------- Comparison Charts -----------------------------------

# Bar chart: total revenue per region (highest to lowest)

df.groupby('region')['revenue'].sum().sort_values(ascending=False).plot.bar()
plt.title("Revenue By Region")
plt.show()

# Bar chart: order count per product category using seaborn

sns.countplot(data=df, x="category", order= df['category'].value_counts().index)

plt.title("Order Count By Category")
plt.show()

# Grouped bar chart: revenue by region AND category using hue

region_cat = df.groupby(['region','category'])['revenue'].sum().reset_index()
sns.barplot(data=region_cat, x='region', y='revenue', hue='category')
plt.show()



# 3 ----------------------- Trend Charts -----------------------------------

# Line chart: monthly revenue trend

monthly = df.groupby('month')['revenue'].sum()
monthly.plot.line(marker='o')
plt.xticks([1, 2, 3, 4])
plt.show()

# Line chart: monthly revenue by region (separate lines per region)

monthly_revenue = df.groupby(['region','month'])['revenue'].sum().reset_index()

sns.lineplot(data=monthly_revenue, x='month', y='revenue', hue='region', marker='o')
plt.show()

# 4 ----------------------- Relationship Charts -----------------------------------

# Scatter plot: units_sold vs revenue. Color by category

sns.scatterplot(data=df, x='units_sold', y='revenue', hue='category', alpha= 0.7)

plt.title("Units Sold Vs Revenue")
plt.show()


# Correlation heatmap for numeric columns

corr = df[['units_sold','unit_price','revenue']].corr()

sns.heatmap(corr, annot= True, cmap='coolwarm', fmt='2f')
plt.show()

# Pair plot for all numeric columns colored by category

sns.pairplot(df[['units_sold','unit_price','revenue','category']], hue='category')
plt.show()

# Pie chat for percentage of total revenue that comes from each product category

pie = df.groupby('category')['revenue'].sum()

plt.pie(pie, labels=pie.index, autopct="%1.1f%%", startangle=90)
plt.title("Revenue Share by Product Category")
plt.show()

#----------------------