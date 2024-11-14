from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime
import time

url = "https://oilprice.com/"

while True:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        oil_prices = []

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        rows = soup.find_all("tr", class_="link_oilprice_row")
        
        for row in rows:
            oil_type = row.get("data-spread")
            price_tag = row.find("td", class_="value")
            price = price_tag.text.strip() if price_tag else None
            
            if oil_type and price:
                oil_prices.append({
                    "type": oil_type,
                    "price": price,
                    "datetime": current_datetime
                })

        with open("oil_prices.json", "a") as json_file:
            json.dump(oil_prices, json_file, indent=4)
            json_file.write(",\n")

        print(f"Data harga minyak berhasil disimpan pada {current_datetime}")
    
    else:
        print("Gagal mengambil data dari situs web.")
    
    time.sleep(60)