from bs4 import BeautifulSoup
import requests
import sqlite3

# Task 2: Scrape and Store Job Listings
def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    job_entries = []
    jobs = soup.find_all("div", class_="card-content")
    for job in jobs:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="content").text.strip()
        link = job.find("a")["href"]
        job_entries.append((title, company, location, description, link))
    
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            link TEXT,
            UNIQUE(title, company, location)
        )
    """)
    
    for entry in job_entries:
        cursor.execute("""
            INSERT OR IGNORE INTO jobs (title, company, location, description, link) VALUES (?, ?, ?, ?, ?)
        """, entry)
    
    conn.commit()
    conn.close()
    print("Jobs saved to database.")

# Run Task
scrape_jobs()