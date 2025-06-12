import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
def afisha_mus_theatre(url):
    page = 1
    data_items = []
    while True:
        url = f'https://www.bileter.ru/afisha/bilety-v-teatr/muzykalnyj-spekatkl?page={page}'
        reg = requests.get(url).text
        soup = BeautifulSoup(reg, 'lxml')
        items = soup.find_all('div', class_='afishe-item')
        if len(items) == 0: #Признак остановки
            break
        # Находим все элементы <div> с классом afishe-item
        for item in items:
            # В каждом элементе <div> ищем элемент <div> с классом "name", "date","place","price"
            div_name = item.find('div', class_='name')
            performance = div_name.find('a').text
            div_date = item.find('div', class_='date')
            date = div_date.text
            div_place = item.find('div', class_='place')
            place = div_place.text
            div_price = item.find('div', class_='price')
            price = div_price.find('a').text
            data_items.append({'название':performance,'дата':date,'театральная площадка':place, 'цена': price})

        page += 1

    return data_items
price_performance = afisha_mus_theatre(url = f'https://www.bileter.ru/afisha/bilety-v-teatr/muzykalnyj-spekatkl?page=1')

df = pd.DataFrame(price_performance)
df.to_excel('price_performance.xlsx')