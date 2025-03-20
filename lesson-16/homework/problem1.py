import sqlite3
import pandas as pd

# 1. Read customers table from chinook.db
conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql("SELECT * FROM customers", conn)
conn.close()
print("Customers Table (First 10 Rows):")
print(customers_df.head(10))
print("\n" + "="*50 + "\n")

# 2. Load iris.json into a DataFrame
iris_df = pd.read_json("iris.json")
print("Iris Dataset Shape:", iris_df.shape)
print("Iris Dataset Columns:", iris_df.columns.tolist())
print("\n" + "="*50 + "\n")

# 3. Load titanic.xlsx into a DataFrame
titanic_df = pd.read_excel("titanic.xlsx")
print("Titanic Dataset (First 5 Rows):")
print(titanic_df.head())
print("\n" + "="*50 + "\n")

# 4. Load Flights parquet file into a DataFrame
flights_df = pd.read_parquet("flights.parquet")
print("Flights Dataset Info:")
print(flights_df.info())
print("\n" + "="*50 + "\n")

# 5. Load movie.csv into a DataFrame
movie_df = pd.read_csv("movie.csv")
print("Movie Dataset (Random 10 Rows):")
print(movie_df.sample(10))
print("\n" + "="*50 + "\n")
