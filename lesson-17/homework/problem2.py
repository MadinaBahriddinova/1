import pandas as pd

# ========== 1. Grouped Aggregations on Titanic ==========
titanic_df = pd.read_excel("titanic.xlsx")
grouped_titanic = titanic_df.groupby("Pclass").agg(
    Average_Age=("Age", "mean"),
    Total_Fare=("Fare", "sum"),
    Passenger_Count=("PassengerId", "count")
).reset_index()

print("Titanic Grouped by Pclass:\n", grouped_titanic)
print("\n" + "="*50 + "\n")


# ========== 2. Multi-level Grouping on Movie Data ==========
movie_df = pd.read_csv("movie.csv")

grouped_movies = movie_df.groupby(["color", "director_name"]).agg(
    Total_Critic_Reviews=("num_critic_for_reviews", "sum"),
    Average_Duration=("duration", "mean")
).reset_index()

print("Movies Grouped by Color and Director:\n", grouped_movies.head())
print("\n" + "="*50 + "\n")


# ========== 3. Nested Grouping on Flights ==========
flights_df = pd.read_parquet("flights.parquet")

grouped_flights = flights_df.groupby(["Year", "Month"]).agg(
    Total_Flights=("FlightNum", "count"),
    Avg_Arrival_Delay=("ArrDelay", "mean"),
    Max_Departure_Delay=("DepDelay", "max")
).reset_index()

print("Flights Grouped by Year and Month:\n", grouped_flights.head())
print("\n" + "="*50 + "\n")
