from bs4 import BeautifulSoup

# Task 1: Scrape Weather Information
def scrape_weather():
    with open("weather.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    data = []
    rows = soup.find("table").find("tbody").find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        day, temp, condition = cols[0].text, int(cols[1].text[:-2]), cols[2].text
        data.append({"day": day, "temperature": temp, "condition": condition})
    
    highest_temp = max(data, key=lambda x: x["temperature"])
    sunny_days = [d["day"] for d in data if d["condition"] == "Sunny"]
    avg_temp = sum(d["temperature"] for d in data) / len(data)
    
    print("Weather Data:", data)
    print("Hottest Day:", highest_temp)
    print("Sunny Days:", sunny_days)
    print("Average Temperature:", avg_temp)

# Run Task
scrape_weather()