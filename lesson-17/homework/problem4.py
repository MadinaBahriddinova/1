import pandas as pd

# ========== 1. Pipeline on Titanic ==========
titanic_df = pd.read_excel("titanic.xlsx")

def filter_survivors(df):
    return df[df["Survived"] == 1]

def fill_missing_age(df):
    df["Age"].fillna(df["Age"].mean(), inplace=True)
    return df

def add_fare_per_age(df):
    df["Fare_Per_Age"] = df["Fare"] / df["Age"]
    return df

titanic_pipeline = (titanic_df.pipe(filter_survivors)
                    .pipe(fill_missing_age)
                    .pipe(add_fare_per_age))

print("Titanic Pipeline Result:\n", titanic_pipeline.head())
print("\n" + "="*50 + "\n")


# ========== 2. Pipeline on Flights ==========
flights_df = pd.read_parquet("flights.parquet")

def filter_delayed_flights(df):
    return df[df["DepDelay"] > 30]
def add_delay_per_hour(df):
    df["Delay_Per_Hour"] = df["DepDelay"] / df["AirTime"]
    return df

flights_pipeline = (flights_df.pipe(filter_delayed_flights)
                    .pipe(add_delay_per_hour))

print("Flights Pipeline Result:\n", flights_pipeline.head())
print("\n" + "="*50 + "\n")
