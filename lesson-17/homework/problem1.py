import pandas as pd
import sqlite3

# ========== 1. Inner Join on Chinook Database ==========
conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql("SELECT * FROM customers", conn)
invoices_df = pd.read_sql("SELECT * FROM invoices", conn)
conn.close()
merged_df = customers_df.merge(invoices_df, on="CustomerId", how="inner")

# Count total invoices per customer
invoice_counts = merged_df.groupby(["CustomerId", "FirstName", "LastName"]).size().reset_index(name="TotalInvoices")
print("Total invoices per customer:\n", invoice_counts.head())

print("\n" + "="*50 + "\n")

# ========== 2. Outer Join on Movie Data ==========
movie_df = pd.read_csv("movie.csv")
df1 = movie_df[["director_name", "color"]].drop_duplicates()
df2 = movie_df[["director_name", "num_critic_for_reviews"]].drop_duplicates()

left_join_df = df1.merge(df2, on="director_name", how="left")
print("Rows after Left Join:", len(left_join_df))

outer_join_df = df1.merge(df2, on="director_name", how="outer")
print("Rows after Full Outer Join:", len(outer_join_df))

print("\n" + "="*50 + "\n")
