import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pandas as pd


def link():
    url = 'https://kugoo-samokat.ru/elektrosamokat-kugoo-s3#!/tab/333312074-2'
    res = requests.get(url, headers={'User-Agent': UserAgent().chrome})
    html = res.content
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('h1', attrs={'class': 'js-product-name'}).text

    d = {
        'Категория': 'Электросамокаты',
        'Цвет': 'черный',
        'Бренд': 'Kugoo',
        'Пол': '',
        'Название': soup.find('h1', attrs={'class': 'js-product-name'}).text,
        'Артикул товара': '0001',
        'Баркод товара': '0001',
        'Цена': soup.find('div', attrs={'class': 't762__price-value'}).text,
        'Состав': '',
        'Описание': '',
        'Гарантийный срок': '1 год',
        'Время зарядки': soup.find('div', attrs={'field': 'tn_text_1610137288297'}).text,
        'Максимальная скорость': soup.find('div', attrs={'field': 'tn_text_1610130533629'}).text,
        'Питание': 'от аккумулятора'
    }
    z = pd.DataFrame(d, index=[0])
    z.to_excel('name.xlsx')


if __name__ == "__main__":
    link()
