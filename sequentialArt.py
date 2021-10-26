import requests
from bs4 import BeautifulSoup

url_page = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"


def extract_category_data(url_page):

    reponse = requests.get(url_page)
    soup = BeautifulSoup(reponse.content, 'html.parser')

    extract_category = dict()
    extract_category["url"] = url_page
    title = soup.title.string
    category = soup.find("ul", class_='nav')

    print(extract_category["url"])
    print(title)
    print(category.text)

    return extract_category


data_category = extract_category_data(url_page)


def extract_page_data(url_page):

    reponse = requests.get(url_page)
    soup = BeautifulSoup(reponse.content, 'html.parser')

    extract_page = dict()
    title_page = soup.find("h1")

    for a in soup.find_all('a'):
        if a.img:
            print(a.img['src'])

    '''
   for h3 in soup.find_all('h3'):
       if h3.a:
           print(h3.a['href'])
    '''

    print(title_page.text)

    return extract_page


data_page = extract_page_data(url_page)

../../../scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html
http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html

