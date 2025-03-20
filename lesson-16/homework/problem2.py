import pandas as pd

# Load datasets
iris_df = pd.read_json("iris.json")
titanic_df = pd.read_excel("titanic.xlsx")
flights_df = pd.read_parquet("flights.parquet")
movie_df = pd.read_csv("movie.csv")

# ========== 1. Exploring `iris.json` ==========
# Rename columns to lowercase
iris_df.columns = iris_df.columns.str.lower()

# Select only sepal_length and sepal_width columns
iris_selected = iris_df[['sepallength', 'sepalwidth']]
print("Iris Dataset (Sepal Length & Width):")
print(iris_selected.head())
print("\n" + "="*50 + "\n")

# ========== 2. Exploring `titanic.xlsx` ==========
# Filter passengers older than 30
titanic_above_30 = titanic_df[titanic_df["Age"] > 30]
print("Titanic Passengers (Age > 30):")
print(titanic_above_30.head())

# Count number of male and female passengers
gender_counts = titanic_df["Sex"].value_counts()
print("\nGender Count in Titanic Dataset:")
print(gender_counts)
print("\n" + "="*50 + "\n")

# ========== 3. Exploring Flights Parquet File ==========
# Extract only origin, destination, and carrier columns
flights_selected = flights_df[['origin', 'dest', 'carrier']]
print("Flights Dataset (Origin, Destination, Carrier):")
print(flights_selected.head())

# Count unique destinations
unique_destinations = flights_df['dest'].nunique()
print("\nNumber of Unique Destinations:", unique_destinations)
print("\n" + "="*50 + "\n")

# ========== 4. Exploring `movie.csv` ==========
# Filter movies with duration > 120 minutes
long_movies = movie_df[movie_df["duration"] > 120]

# Sort the filtered DataFrame by `director_facebook_likes` in descending order
sorted_movies = long_movies.sort_values(by="director_facebook_likes", ascending=False)

print("Movies Longer than 120 Minutes, Sorted by Director Facebook Likes:")
print(sorted_movies.head())
print("\n" + "="*50 + "\n")
