from bs4 import BeautifulSoup as BS
import requests
import traceback


class Oasiscatalog:
    def __init__(self, parent):
        self.main_page = 'https://www.oasiscatalog.com/'
        self.parent = parent

    def parser_category(self):
        cat_link = "https://www.oasiscatalog.com/rubricator"

        r = requests.get(cat_link)
        html = BS(r.content, 'html.parser')
        categories = []

        for el in html.find_all(class_='rubricator-list__item'):
            title = el.find_all(class_="rubricator-list__link-text")[0].text
            href = el.find_all(class_="rubricator-list__link")[0]['href']

            sub_els = el.find_all(class_="rubricator-list__l2-item")
            subcategories = []
            for sub_el in sub_els:
                sub_title = sub_el.text.strip()
                sub_href = sub_el.select_one('a')['href']
                subcategories.append({'title': sub_title, 'href': sub_href})
            categories.append({'title': title, 'href': href, 'subcategories': subcategories})
        return categories

    def parser_goods(self, href):
        first_page = self.main_page + href[1:]
        goods = []
        i = 1
        while True:
            print('cтраница %i' % i)
            r = requests.get(first_page + '?page=' + str(i))
            html = BS(r.content, 'html.parser')
            for el in html.select('.new-catalog-product'):
                title = el.find('a', class_='new-catalog-product__title')
                if title is not None:
                    product_number = el.find('p', class_='new-catalog-product__text').text
                    goods.append({'title': title.text.strip(),
                                  'href': title['href'],
                                  'vendor code': product_number})
            if not html.select('.pagination__item'):
                break
            check_page = html.select('.pagination__item')[-2].select('a')[0].text
            if str(i) == check_page:
                break
            else:
                i += 1
        return goods

    def parser_good(self, page):
        r = requests.get(page)
        html = BS(r.content, 'html.parser')
        main_good = self.pars_good_main(page)
        item_other_colors_box = html.find_all('a', class_='product-preview__colors-link')
        if item_other_colors_box:
            for item in item_other_colors_box[1:]:
                url = self.main_page + item['href'][1:]
                good_color = self.pars_good_main(url)
                if good_color is not None:
                    main_good['price'].extend(good_color['price'])
                    main_good['page'].extend(good_color['page'])
                    main_good['color'].extend(good_color['color'])
                    main_good['descriptions'].extend(good_color['descriptions'])
                    main_good['sizes'].extend(good_color['sizes'])
                    main_good['marks'].extend(good_color['marks'])
                    main_good['vendor_code'].extend(good_color['vendor_code'])
        return main_good

    def pars_good_main(self, page):
        try:
            r = requests.get(page)
            html = BS(r.content, 'html.parser')
            title = html.find_all('li', class_='breadcrumbs__item')[-2:]
            section = title[0].select('span')[0].text.strip()
            name_box = html.find_all('div', class_='product-heading__section')
            # name = name_box[0].text.strip()
            name = html.select_one('h1.product-heading__title').text.strip()
            # art = name_box[1].text.strip().split()
            art = html.select('div.product-heading__section')[4].text.strip().split()
            vendor_code = art[1][:-1]
            if len(art) > 2:
                mark = art[2]
                if 'Временно' in mark:
                    mark = 'Временно нет в наличии'
            else:
                mark = ''
            price = float('.'.join(html.find('div', class_='product-price2__price-1').text.strip().split()[:2]))
            amount_of_sizes = {}
            all_sizes = html.find_all('div', 'product-amount-textile__item')
            if all_sizes:
                for line in all_sizes:
                    size = self.parent.get_size(line.find('div', class_='product-amount-textile__item-cell_size').text.strip())
                    amount = line.find('span', class_='product-amount-textile__item-cell-text_dashed').text.strip().split()
                    amount = int(''.join(amount))
                    amount_of_sizes[size] = amount
            else:
                amount = html.find('div', 'product-amount__row-b').text.strip().split()
                if amount[1].isdigit():
                    amount = int(''.join(amount[:2]))
                else:
                    amount = int(''.join(amount[:1]))
                amount_of_sizes[self.parent.get_size('Склад')] = amount
            color = ''
            for el in html.select('.product-params__item'):
                if el.select('.product-params__item-title')[0].text.strip() == 'Цвет товара':
                    color = el.select('.product-params__item-data')[0].text.strip()
                    break
            materials = ''
            for el in html.select('.product-params__item'):
                if el.select('.product-params__item-title')[0].text.strip() == 'Материал товара':
                    materials = el.select('.product-params__item-data')[0].text.strip()
                    break
            description = html.select('.product__description')
            if description:
                description = description[0].text.strip()
            else:
                description = ''
            return {'name': name, 'price': [price], 'section': section, 'marks': [mark],
                    'color': [color], 'page': [page], 'materials': materials, 'descriptions': [description],
                    'sizes': [amount_of_sizes], 'vendor_code': [vendor_code]}
        except Exception as e:
            print(e)
            traceback.print_exc()
            return None


if __name__ == '__main__':
    s = Oasiscatalog('0')
    # for key, val in s.parser_good('https://www.oasiscatalog.com/item/1-000059242').items():
    #     print(key, val)
    for key, val in s.parser_good('https://www.oasiscatalog.com/item/1-000022159').items():
        print(key, val)
    # https://www.oasiscatalog.com/item/1-000064500
    # print(s.parser_goods('/catalog/polo-s-logotipom'))
