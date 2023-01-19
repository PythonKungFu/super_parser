import requests
from bs4 import BeautifulSoup as BS
import json
import traceback
from pprint import pp


class Modernit:
    def __init__(self, parent):
        self.main_page = 'https://www.modern-it.ru/'
        self.parent = parent

    def parser_category(self):
        r = requests.get(self.main_page)
        html = BS(r.content, 'html.parser')
        categories = []
        for el in html.find('div', class_='menu-catalog flex-block').find_all('a', class_='box-category')[:-5]:
            if 'С принтом' not in el.text.strip():
                categories.append({'title': el.text.strip(), 'href': el['href'], 'subcategories': []})
        return categories

    def parser_goods(self, href):
        first_page = self.main_page + href[1:]
        r = requests.get(first_page.strip())
        html = BS(r.content, 'html.parser')
        goods = []
        for el in html.find_all('div', class_='_product'):
            text_container = el.select('a')[1]
            title = text_container.text.strip()

            url_products = self.main_page + text_container['href'][1:]
            response = requests.get(url_products)
            soup = BS(response.content, 'html.parser')
            product = soup.select('div._product')[0]
            title = product.select_one('p.name').text.strip()
            url_product = product.select_one('a')['href']
            goods.append({'title': title, 'href': url_product, 'vendor code': ''})

            # goods.append({'title': title, 'href': text_container['href'], 'vendor code': ''})
        pp(goods)
        return goods

    def parser_good(self, page):
        try:
            r = requests.get(page)
            html = BS(r.content, 'html.parser')
            title = html.find('div', class_='breadcrumbs')
            section = title.find_all('a')[-2].text.strip()
            name = title.find_all('a')[-1].text.strip()
            colors = []
            vendor_codes = []
            prices = []
            amount_of_sizes = []
            data = html.find('button', class_='calc btn send spm-button')
            if data:
                data = json.loads(data['data-base'])
                sizes = data[0][1:]
                for color, *items in data[1:]:
                    if len(items) != 0:
                        colors.append(color)
                        vendor_codes.append(items[0]['article'])
                        prices.append(float(items[0]['price']))
                        size_dict = {}
                        for i in range(len(sizes)):
                            size_dict[self.parent.get_size(sizes[i])] = items[i]['qty']
                        amount_of_sizes.append(size_dict)
                count = len(colors)
            else:
                count = 0
                for el in html.find_all('div', class_='palitra-list-item'):
                    if 'Арт' in el.find_all('div')[2].text:
                        vendor_codes.append(el.find_all('div')[2].text.strip().replace('Арт.', ''))
                    else:
                        colors.append(el.find_all('div')[2].text.strip())
                    count += 1
                count = 1 if count == 0 else count
                if len(colors) == 0:
                    colors = [''] * count
                if len(vendor_codes) == 0:
                    vendor_codes = [''] * count
                prices = ['-'] * count
                for el in html.find('div', class_='description1').find_all('div', class_='row'):
                    param = el.find_all('div')
                    if param[0].text.strip() == 'Размеры':
                        amount_of_sizes = [{param[1].text.strip(): '-'}] * count
                        break
            mark = ''
            materials = ''
            for el in html.find('div', class_='description1').find_all('div', class_='row'):
                param = el.find_all('div')
                if param[0].text.strip() == 'Состав':
                    materials += param[1].text.strip() + ' '
                elif param[0].text.strip() == 'Плотность':
                    materials += param[1].text.strip() + ' '
            description = html.find('div', class_='description2')
            if description:
                description = description.text.strip()
            else:
                description = ''
            return {'name': name, 'price': prices, 'section': section, 'marks': [mark] * count,
                    'color': colors, 'page': [page] * count, 'materials': materials,
                    'descriptions': [description] * count, 'sizes': amount_of_sizes, 'vendor_code': vendor_codes}
        except Exception as e:
            print(e)
            traceback.print_exc()
            return


if __name__ == '__main__':
    s = Modernit()
    # for i in s.parser_goods('/futbolki'):
    #     print(i)
    # for key, val in s.parser_good('https://www.modern-it.ru/futbolki/18/promo-futbolki-ekonom-detail').items():
    #     print(key, val)
    for key, val in s.parser_good('https://www.modern-it.ru/panamy-optom/79/panamy-detail').items():
        print(key, val)
    # print(s.parser_good('https://www.modern-it.ru/kollektsii/67/sportivnye-kostyumy-muzhskie-bordo-temno-sinij-detail'))
