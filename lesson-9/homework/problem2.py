import csv
from collections import defaultdict

def read_grades(file_name):
    grades = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Grade"] = int(row["Grade"])
            grades.append(row)
    return grades

def calculate_average_grades(grades):
    subject_totals = defaultdict(list)
    for entry in grades:
        subject_totals[entry["Subject"]].append(entry["Grade"])
    
    averages = {subject: sum(grades) / len(grades) for subject, grades in subject_totals.items()}
    return averages

def write_average_grades(file_name, averages):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 2)])

# Example Usage
grades = read_grades("grades.csv")
averages = calculate_average_grades(grades)
write_average_grades("average_grades.csv", averages)
print("Average grades calculated and saved to average_grades.csv.")
