import pandas as pd
import sqlite3

# ─────────────────────────────────────
# Load data and create SQLite database
# ─────────────────────────────────────

df = pd.read_csv("../data/clean/Cleaned_Data.csv")

# Create SQLite database
conn = sqlite3.connect("../data/clean/ecommerce.db")

# Load DataFrame into SQL table called 'orders'
df.to_sql('orders', conn, if_exists='replace', index=False)
print("Database ready")

 # All orders from North region 
 
query1 = """
    SELECT * 
    FROM orders 
    WHERE region = 'North'
        """
result1 = pd.read_sql(query1, conn)
print(result1)

 # Total number of orders per region
 
query2 = """
    SELECT region, COUNT(*) as orders_count 
    FROM orders 
    GROUP BY region
    ORDER BY orders_count DESC
"""
result2 = pd.read_sql(query2, conn)
print(result2)

 #  Total revenue per category
 
query3 = """
    SELECT category, sum(revenue) as Total_Revenue 
    from orders
    GROUP BY category 
"""
result3 = pd.read_sql(query3, conn)
print(result3)
 
 
# All completed orders with revenue > 1000

query4 = """
    SELECT * from orders
    WHERE status = 'completed' AND revenue > 1000
    ORDER BY revenue desc
"""

result4 = pd.read_sql(query4, conn)
print(result4)

# Top 5 orders by Revenue

query5 = """
    SELECT order_id, customer_name, product, revenue 
    From orders
    ORDER BY revenue desc
    LIMIT 5
"""
result5 = pd.read_sql(query5, conn)
print(result5)


# Total revenue and order count per customer. Show only customers with revenue > 2000

query6 = """
    SELECT customer_name, SUM(revenue), COUNT(*) as order_count
    FROM orders
    GROUP BY customer_name
    HAVING revenue > 2000


"""
result6 = pd.read_sql(query6, conn)
print(result6)

#  Each customer's revenue as a % of total revenue

query7 = """
    SELECT customer_name, 
    SUM(revenue) as rev, 
    ROUND(SUM(revenue)* 100.0 /(SELECT SUM(revenue) from orders), 1) as pct 
    FROM orders
    GROUP BY customer_name
    ORDER BY rev desc
"""

result7 = pd.read_sql(query7, conn)
print(result7)

#  Monthly revenue trend

query8 = """
    SELECT strftime('%m',order_date) as month, 
    SUM(revenue) as monthly_revenue
    FROM orders
    GROUP BY month
    ORDER BY month
"""

result8 = pd.read_sql(query8, conn)
print(result8)

#  Products that have never been cancelled

query9 = """
    SELECT DISTINCT product
    FROM orders
    WHERE product NOT IN (SELECT DISTINCT product from orders where status = 'cancelled')
"""

result9 = pd.read_sql(query9, conn)
print(result9)

#  Customers by total revenue using DENSE_RANK

query10 = """
    WITH totals AS (SELECT customer_name, SUM(revenue) AS tot_rev
                    from orders
                    GROUP BY customer_name 
                    )
    SELECT customer_name, tot_rev, DENSE_RANK() over(ORDER BY tot_rev DESC) as Rank
    from totals
"""

result10 = pd.read_sql(query10, conn)
print(result10)

# For each region rank products by revenue — show rank within region

query11 = """
    WITH totals AS (
        SELECT region, product, SUM(revenue) AS total_rev
        from orders
        GROUP BY region, product
    )
    
    SELECT region, product, total_rev, DENSE_RANK() OVER(PARTITION BY region ORDER BY total_rev DESC) as Rank
    from totals
    ORDER BY region, Rank
"""

result11 = pd.read_sql(query11, conn)
print(result11)

# Running total of revenue ordered by date

query12 = """
    SELECT order_date, revenue, SUM(revenue) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED
    preceding and current row) as running_totals from orders

"""

result12 = pd.read_sql(query12, conn)
print(result12)


#  Each customer's most recent order date

query13 = """
    SELECT DISTINCT customer_name, MAX(order_date) OVER(PARTITION BY customer_name) as Last_Order
    from orders
"""

result13 = pd.read_sql(query13, conn)
print(result13)

#----------------------












