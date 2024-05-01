import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

base_url = 'https://www.ss.com'
start_url = 'https://www.ss.com/lv/transport/cars/land-rover/filter/'
car_urls = []

# Collect URLs of individual car listings
while True:
    response = requests.get(start_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        listing_elements = soup.find_all('td', class_='msg2')
        for element in listing_elements:
            link = element.find('a', class_='am')  # Adjust class name if necessary
            if link:
                car_urls.append(urljoin(base_url, link.get('href')))
        # Handle pagination if exists
        next_page = soup.find(class_="d1").find(class_="navi")  # Adjust class name if necessary
        if next_page:
            relative_url = next_page.get("href")
            start_url = urljoin(base_url, relative_url)
        else:
            break
    else:
        break

car_model_counts = {}
products_info = []
for url in car_urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        product_dick = dict()

        # Extract information
        make_model = soup.find(id='tdo_31')
        release_year = soup.find(id='tdo_18')
        engine_volume = soup.find(id='tdo_15')
        gearbox = soup.find(id='tdo_35')
        mileage = soup.find(id='tdo_16')
        color = soup.find(id='tdo_17')
        technical_inspection_deadline = soup.find(id='tdo_223')

        # Check if engine_volume contains "dīzelis"
        if engine_volume and "dīzelis" in engine_volume.text.lower():
            product_dick["Modelis"] = make_model.text.strip() if make_model else None
            product_dick["Izlaiduma gads"] = release_year.text.strip() if release_year else None
            product_dick["Motora tilpums"] = engine_volume.text.strip()
            product_dick["Ātrumkārbas veids"] = gearbox.text.strip() if gearbox else None
            product_dick["Nobraukums"] = mileage.text.strip() if mileage else None
            product_dick["Krāsa"] = color.text.strip() if color else None
            product_dick["Tehniskās apskates termiņš"] = technical_inspection_deadline.text.strip() if technical_inspection_deadline else None

            products_info.append(product_dick)

            if make_model:
                model_key = make_model.text.strip()
                if model_key in car_model_counts:
                    car_model_counts[model_key] += 1
                else:
                    car_model_counts[model_key] = 1

# Save and print the data
if products_info:
    with open('land_rover.json', 'w', encoding='utf-8') as f:
        json.dump(products_info, f, ensure_ascii=False, indent=4)
    print("Data saved")
    for model, count in car_model_counts.items():
        print(f"{model} : {count}")
else:
    print("No data to save")
