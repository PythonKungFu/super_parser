import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Uzcotton:
    def __init__(self, parent):
        self.main_page = 'https://uzcotton.ru/'
        self.parent = parent
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

    def parser_category(self):
        r = requests.get(self.main_page + '/catalog/')
        html = BS(r.content, 'html.parser')
        categories = []
        for el in html.select('div.item_block a.dark_link'):
            categories.append({'title': el.text, 'href': el['href'], 'subcategories': []})
        return categories

    async def parser_category_async(self):
        self.parser_category()

    def parser_goods(self, href):
        first_page = self.main_page + href[1:]
        r = requests.get(first_page)
        html = BS(r.content, 'html.parser')
        goods = []
        n = html.find('a', class_='dark_link cv_too')
        if n:
            max_page = int(n.text)
        else:
            max_page = 1
        for i in range(1, max_page + 1):
            print('cтраница %i' % i)
            r = requests.get(first_page + '?PAGEN_1=' + str(i))
            html = BS(r.content, 'html.parser')

            for el in html.find_all('div', class_='item_info'):
                text_container = el.find('a', class_='dark_link option-font-bold font_sm')
                title = text_container.find('span').text
                # product_number = el.select('.product-number')[0]['title']
                goods.append({'title': title, 'href': text_container['href'], 'vendor code': ''})
        return goods

    def parser_good(self, page):
        try:
            self.driver.get(page)
            html = BS(self.driver.page_source, 'html.parser')
            title = html.find_all('a', class_='breadcrumbs__link')[-1]
            section = title.find('span', itemprop='name').text.strip()
            name = html.find('h1', id='pagetitle').text.strip()
            amount_of_sizes = {}
            all_sizes = html.find('div', class_='list-offers')
            if all_sizes:
                all_sizes = all_sizes.find_all('div', class_='table-view__item')
                for line in all_sizes:
                    size = self.parent.get_size(line.find('div', class_='item-title').text.strip())
                    amount = line.find('span', class_='value font_sxs').text
                    amount = amount.replace('В наличии: ', '').replace(' шт.', '').strip()
                    amount_of_sizes[size] = amount
            else:
                amount_of_sizes[self.parent.get_size('Склад')] = ''
            price = html.find('meta', itemprop='price')['content']
            if price:
                price = float(''.join(price.strip().split()))
            else:
                price = '-'
            color = html.find('div', class_='properties__value darken properties__item--inline')
            if color:
                color = color.text.strip()
            else:
                color = ''
            materials = ''
            for el in html.find_all('tr', itemprop='additionalProperty'):
                if el.find('span', itemprop='name').text.strip() == 'Материал':
                    materials = el.find('span', itemprop='value').text.strip()
                    break
            description = html.find('div', itemprop='description')
            if description:
                description = description.text.strip()
            else:
                description = ''
            return {'name': name, 'price': [price], 'section': section, 'marks': [''] * len([page]),
                    'color': [color], 'page': [page], 'materials': materials, 'descriptions': [description],
                    'sizes': [amount_of_sizes], 'vendor_code': [''] * len([page])}
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    s = Uzcotton()
    # print(s.parser_category())
    # print(s.parser_goods('/catalog/futbolki/'))
    print(s.parser_good('https://uzcotton.ru/catalog/vetrovka_classic_belaya/'))
