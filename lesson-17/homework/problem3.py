import pandas as pd

# ========== 1. Classify Titanic Passengers as Child or Adult ==========
titanic_df = pd.read_excel("titanic.xlsx")

def classify_age(age):
    return "Child" if age < 18 else "Adult"

titanic_df["Age_Group"] = titanic_df["Age"].apply(classify_age)
print("Titanic Age Groups:\n", titanic_df[["Age", "Age_Group"]].head())
print("\n" + "="*50 + "\n")


# ========== 2. Normalize Employee Salaries ==========
employee_df = pd.read_csv("employee.csv")

employee_df["Normalized_Salary"] = employee_df.groupby("Department")["Salary"].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)

print("Normalized Employee Salaries:\n", employee_df.head())
print("\n" + "="*50 + "\n")


# ========== 3. Classify Movies by Duration ==========
movie_df = pd.read_csv("movie.csv")
def classify_movie_length(duration):
    if duration < 60:
        return "Short"
    elif 60 <= duration <= 120:
        return "Medium"
    else:
        return "Long"

movie_df["Movie_Length"] = movie_df["duration"].apply(classify_movie_length)
print("Movie Length Classification:\n", movie_df[["title", "duration", "Movie_Length"]].head())
print("\n" + "="*50 + "\n")
