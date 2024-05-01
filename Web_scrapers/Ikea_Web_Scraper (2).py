import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.ikea.lv/lv/products/dzivojama-istaba/kafijas-galdini-un-zurnalgaldini/kafijas-galdini-un-zurnalgaldini'
products = []

while True:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            product_elements = soup.find_all(class_='itemInfo') 
            for m in product_elements:
                products.append(m)
            if soup.find(class_="page-item next") == None:
                break
            new_url = soup.find(class_="page-item next")
            new_url = new_url.find(class_="page-link")
            url = new_url["href"]
        else:
            break

if response.status_code == 200:
        products_info = []
        for product in product_elements:
            products_dick = dict()
            name = product.find(class_='display-7 mr-2') 
            description = product.find(class_='itemFacts')
            price = product.find(class_='display-6')  
            products_dick["Nosaukums"] = name.text.strip()
            products_dick["Apraksts"] = description.text.strip()
            products_dick["Cena"] = price.text.strip()
            products_info.append(products_dick)

        with open('produkti.json', 'w', encoding='utf-8') as f:
            print("is saved")
            json.dump(products_info, f, ensure_ascii=False, indent=4)
        for products in products_info:
            print(f'{products["Nosaukums"]} : {products["Cena"]}')
else:
     print("es gribu nomirt")
