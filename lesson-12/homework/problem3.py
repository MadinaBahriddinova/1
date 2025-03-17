from bs4 import BeautifulSoup
import requests
import json

# Task 3: Scrape Laptop Data
def scrape_laptops():
    url = "https://www.demoblaze.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    laptops = []
    items = soup.find_all("div", class_="card")
    for item in items:
        name = item.find("h4").text.strip()
        price = item.find("h5").text.strip()
        description = item.find("p").text.strip()
        laptops.append({"name": name, "price": price, "description": description})
    
    with open("laptops.json", "w", encoding="utf-8") as f:
        json.dump(laptops, f, indent=4)
    
    print("Laptop data saved to laptops.json.")

# Run Task
scrape_laptops()
