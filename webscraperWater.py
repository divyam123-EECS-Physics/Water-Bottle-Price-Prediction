import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
baseurl = 'https://beverageuniverse.com/water.html?p=1'

categories = {
        "Name" : '',
        "Brand" : '',
        "Pack Size" : 0,
        "Water Source": '',
        "Falvor": '',
        "Container": '',
        "Price": 0,
        "100% Natural": 0,
        "Anti-Oxidant": 0,
        "Artesian" : 0,
        "BPA Free Plastic": 0,
        "Caffeinated" : 0,
        "Carbonated" : 0,
        "Electrolytes" : 0,
        "Energy Drinks" : 0,
        "Enhanced" : 0,
        "Ethically Sourced" : 0,
        "Fair Trade" : 0,
        "Flavored" : 0,
        "Gluten FREE" : 0,
        "Green Tea" : 0,
        "Kosher" : 0,
        "Low Calorie" : 0,
        "Mineral Water" : 0,
        "No Artifical Flavors" : 0,
        "No Artifical Preservatives" : 0,
        "No Artifical Sweetners" : 0,
        "Non-Alcoholic Wine" : 0,
        "Non GMO" : 0,
        "Non-Sparkling Water" : 0,
        "Nutritional" : 0,
        "Organic" : 0,
        "Organic Cane Sugar" : 0,
        "Preservatice Free" : 0,
        "Purified Water" : 0,
        "Regular Soda" : 0,
        "Sodium-Free" : 0,
        "Soy FREE" : 0,
        "Sparkling Juice" : 0,
        "Sparkling Water" : 0,
        "Spring Water" : 0,
        "Sweetened" : 0,
        "Tea" : 0,
        "Tea" : 0,
        "Twist off Top" : 0,
        "USDA Organic" : 0,
        "Under 100 Calories" : 0,
        "30 Calories": 0,
        "Variety Pack" : 0,
        "Vegan" : 0,
        "Zero Carb" : 0,
        "Zero Calorie" : 0,
        "Zero Sodium" : 0,
        "Zero Calories" : 0,
        "Zero Sugar" : 0,
        "Zero Sweeteners" : 0,
    }
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
df = pd.DataFrame(columns = categories.keys())
productlinks = []
for i in range(1, 19):
    page_url = baseurl[:-1] + str(i)
    r = requests.get(page_url)
    soup = BeautifulSoup(r.content, 'lxml')

    file1 = soup.find_all('div',class_ = 'column')

    for i in file1:
        for l in i.find_all('a', href = True):
            if l['href'] != '#':
                productlinks.append(l['href'])
for product in productlinks:
    r = requests.get(product)#, headers = headers)
    soup = BeautifulSoup(r.content, 'lxml')

    characteristics_categories = {
        "Name" : '',
        "Brand" : '',
        "Pack Size" : 0,
        "Water Source": '',
        "Falvor": '',
        "Container": '',
        "Price": 0,
        "100% Natural": 0,
        "Anti-Oxidant": 0,
        "Artesian" : 0,
        "BPA Free Plastic": 0,
        "Caffeinated" : 0,
        "Carbonated" : 0,
        "Electrolytes" : 0,
        "Energy Drinks" : 0,
        "Enhanced" : 0,
        "Ethically Sourced" : 0,
        "Fair Trade" : 0,
        "Flavored" : 0,
        "Gluten FREE" : 0,
        "Green Tea" : 0,
        "Kosher" : 0,
        "Low Calorie" : 0,
        "Mineral Water" : 0,
        "No Artifical Flavors" : 0,
        "No Artifical Preservatives" : 0,
        "No Artifical Sweetners" : 0,
        "Non-Alcoholic Wine" : 0,
        "Non GMO" : 0,
        "Non-Sparkling Water" : 0,
        "Nutritional" : 0,
        "Organic" : 0,
        "Organic Cane Sugar" : 0,
        "Preservatice Free" : 0,
        "Purified Water" : 0,
        "Regular Soda" : 0,
        "Sodium-Free" : 0,
        "Soy FREE" : 0,
        "Sparkling Juice" : 0,
        "Sparkling Water" : 0,
        "Spring Water" : 0,
        "Sweetened" : 0,
        "Tea" : 0,
        "Tea" : 0,
        "Twist off Top" : 0,
        "USDA Organic" : 0,
        "Under 100 Calories" : 0,
        "30 Calories": 0,
        "Variety Pack" : 0,
        "Vegan" : 0,
        "Zero Carb" : 0,
        "Zero Calorie" : 0,
        "Zero Sodium" : 0,
        "Zero Calories" : 0,
        "Zero Sugar" : 0,
        "Zero Sweeteners" : 0,
    }
    characteristics_categories["Name"] = soup.find('h2',class_ = 'bannerTtl').text
    characteristics_categories["Price"] = float(soup.find('span',class_ = 'price').text[1:])
    
    bev_info = soup.find_all('td')
    for table in bev_info:
        if table.get('data-th') == 'Beverage Characteristics':
            string_of_characteristics = table.text.strip()
            list_of_characteristics = string_of_characteristics.split(', ') 
            for characteristic in list_of_characteristics:
                characteristics_categories[characteristic] = 1
        if table.get('data-th') == 'Calories':
            string_of_characteristics = table.text.strip()
            list_of_characteristics = string_of_characteristics.split(', ') 
            for characteristic in list_of_characteristics:
                characteristics_categories[characteristic] = 1
        if table.get('data-th') == 'Brand':
            characteristics_categories['Brand'] = table.text.strip()

        if table.get('data-th') == 'Pack Size':
            temp = table.text.strip()
            characteristics_categories['Pack Size'] = int(temp[8:])

        if table.get('data-th') == 'Water Source':
            characteristics_categories['Water Source'] = table.text.strip()

        if table.get('data-th') == 'Flavor':
            characteristics_categories['Flavor'] = table.text.strip()

        if table.get('data-th') == 'Container':
            characteristics_categories['Container'] = table.text.strip()
            
        if table.get('data-th') == 'Beverage Size':
            characteristics_categories['Beverage Size'] = float(table.text.strip()[:-2])
    df1  = pd.DataFrame.from_records([characteristics_categories])
    df = df.append(df1)
df.to_csv('/Users/divyamgoel/Desktop/Project/cvete/watter_bottle.csv')
