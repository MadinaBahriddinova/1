import pandas as pd

# Load datasets
iris_df = pd.read_json("iris.json")
titanic_df = pd.read_excel("titanic.xlsx")
flights_df = pd.read_parquet("flights.parquet")
movie_df = pd.read_csv("movie.csv")

# ========== 1. Statistics for `iris.json` ==========
# Compute mean, median, and standard deviation for each numerical column
iris_stats = iris_df.describe().loc[['mean', '50%', 'std']]
print("Iris Dataset - Mean, Median, and Standard Deviation:")
print(iris_stats)
print("\n" + "="*50 + "\n")

# ========== 2. Statistics for `titanic.xlsx` ==========
# Compute min, max, and sum of passenger ages
age_stats = {
    "Min Age": titanic_df["Age"].min(),
    "Max Age": titanic_df["Age"].max(),
    "Sum of Ages": titanic_df["Age"].sum()
}
print("Titanic Dataset - Age Statistics:")
print(age_stats)
print("\n" + "="*50 + "\n")

# ========== 3. Analysis for `movie.csv` ==========
# Director with highest total `director_facebook_likes`
top_director = movie_df.groupby("director_name")["director_facebook_likes"].sum().idxmax()
print("Director with the Highest Total Facebook Likes:", top_director)

# Find the 5 longest movies and their respective directors
top_5_longest_movies = movie_df.nlargest(5, "duration")[["title", "director_name", "duration"]]
print("\nTop 5 Longest Movies and Their Directors:")
print(top_5_longest_movies)
print("\n" + "="*50 + "\n")

# ========== 4. Missing Value Handling in `Flights.parquet` ==========
# Check for missing values
missing_values = flights_df.isnull().sum()
print("Missing Values in Flights Dataset:")
print(missing_values)

# Fill missing values in a numerical column (e.g., 'flight_duration') with the mean
if "flight_duration" in flights_df.columns:
    flights_df["flight_duration"].fillna(flights_df["flight_duration"].mean(), inplace=True)
    print("\nMissing values in 'flight_duration' filled with column mean.")
else:
    print("\nColumn 'flight_duration' not found in Flights dataset.")

print("\n" + "="*50 + "\n")
