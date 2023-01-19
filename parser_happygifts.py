from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests


class HappyGifts:
    def __init__(self, parent):
        self.main_page = 'https://happygifts.ru/'
        self.parent = parent

    def parser_category(self):
        r = requests.get(self.main_page)
        html = BS(r.content, 'html.parser')
        categories = []
        for el in html.find('div', class_='catalog-menu-inner').find_all('li', class_='level1-item'):
            link = el.select('.level1-title')[0]
            list_item = el.find('ul', class_='level2-list')
            subcategories = []
            if list_item:
                for item in list_item.find_all('li', class_='level2-item')[1:]:
                    c = item.select('a')[0]
                    subcategories.append({'title': c.text, 'href': c['href']})
            categories.append({'title': link.text.strip(), 'href': link['href'], 'subcategories': subcategories})
        return categories

    async def parser_category_async(self):
        self.parser_category()

    def parser_goods(self, href):
        first_page = self.main_page + href[1:]
        r = requests.get(first_page)
        html = BS(r.content, 'html.parser')
        goods = []
        navigation = html.select('.catalog-pagination.modern-page-navigation')
        max_page = navigation[0].select('a')
        if max_page:
            max_page = int(max_page[-2].text)
        else:
            max_page = 1
        for i in range(1, max_page + 1):
            print('cтраница %i' % i)
            r = requests.get(first_page + '?PAGEN_1=' + str(i))
            html = BS(r.content, 'html.parser')

            for el in html.select('.catalog-item-container'):
                text_container = el.select('.text-container')
                if text_container:
                    title = text_container[0].select('.product-title')
                    product_number = el.select('.product-number')[0]['title']
                    goods.append({'title': title[0].text, 'href': title[0]['href'], 'vendor code': product_number})
        return goods

    def parser_good(self, page):
        r = requests.get(page)
        html = BS(r.content, 'html.parser')
        url = page
        main_good = self.pars_good_main(page)

        item_other_colors_box = html.find_all('li', class_='color-item')
        if len(item_other_colors_box) > 1:
            other_colors = item_other_colors_box[1:]
            for item in other_colors:
                url = self.main_page + item['data-url'][1:]
                good_color = self.pars_good_main(url)
                if good_color is not None:
                    main_good['price'].extend(good_color['price'])
                    main_good['page'].extend(good_color['page'])
                    main_good['color'].extend(good_color['color'])
                    main_good['marks'].extend(good_color['marks'])
                    main_good['vendor_code'].extend(good_color['vendor_code'])
                    main_good['descriptions'].extend(good_color['descriptions'])
                    main_good['sizes'].extend(good_color['sizes'])
        return main_good

    def pars_good_main(self, page):
        try:
            r = requests.get(page)
            html = BS(r.content, 'html.parser')
            section = html.find('li', class_='breadcrumb-item link-parent').text.strip()
            name = html.find('li', class_='breadcrumb-item current').text.strip()
            product_number = html.select('.articul')[0].text.strip()
            color = html.find_all('li', class_='color-item')[0]['data-color']
            mark = html.find('span', class_='md_newico')
            if mark:
                mark = mark.text.strip()
            else:
                mark = ''
            price = html.find('span', class_='price').text.strip()[:-2].strip()
            amount_of_sizes = {}
            items = html.find('div', class_='avilability-table avilability-table-sizes')
            if items is not None:
                items = items.find_all('ul')[:2]
                for item in range(1, len(items[0].find_all('li'))):
                    size = items[0].find_all('li')[item]
                    amount = items[1].find_all('li')[item]
                    amount_of_sizes[self.parent.get_size(size.text.strip())] = amount.text.split('/')[0].strip()
            else:
                items = html.find('div', class_='avilability-table avilability-table-nosizes').find_all('ul')[1]
                amount_of_sizes[self.parent.get_size('Склад')] = items.find('span', class_='number-all').text.strip()
            descriptions = html.find('div', class_='detail-text')
            descriptions = descriptions.text.strip() if descriptions else ''
            materials = ''
            for item in html.find('div', class_='col-md-4').find_all('p'):
                if 'Материал' in item.text.strip():
                    materials = item.text.strip().replace('Материал', '')
                    break

            return {'section': section, 'name': name, 'page': [page], 'marks': [mark], 'price': [price],
                    'descriptions': [descriptions], 'vendor_code': [product_number],
                    'materials': materials, 'sizes': [amount_of_sizes], 'color': [color]}
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    s = HappyGifts()
    for i in s.parser_category():
        print(i)
    # print(s.parser_good('https://happygifts.ru/catalog_new/promo_odezhda/polo/muzhskie_1087/fruit_of_the_loom_1090/polo_muzhskoe_premium_polo_170_articul_632180/color_glubokiy_temno-siniy/'))
    # print(s.parser_good('https://happygifts.ru/catalog_new/nagrady/medali/medal_glory_v_podarochnoy_upakovke_70kh66kh5_mm_akril_articul_34709u/color_prozrachnyy/'))
