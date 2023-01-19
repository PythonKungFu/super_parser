from bs4 import BeautifulSoup
import requests
import traceback


class Gifts:
    def __init__(self, parent):
        self.main_page = 'https://gifts.ru/'
        self.parent = parent

    def parser_category(self):
        r = requests.get(self.main_page)
        soup = BeautifulSoup(r.content, 'lxml')
        categories = []
        for el in soup.find_all('li', class_='m-ctlg-item'):
            category = el.find('a', class_='m-ctlg-root')
            title = category.text
            href = category["href"]
            list_item = el.find_all('a', class_='m-ctlg-link')
            subcategories = []
            if list_item:
                for subcategory in list_item:
                    subcategories.append({'title': subcategory.text, 'href': subcategory["href"]})
            categories.append({'title': title, 'href': href, 'subcategories': subcategories})
        return categories

    def parser_goods(self, href):
        first_page = self.main_page + href[1:]
        r = requests.get(first_page)
        html = BeautifulSoup(r.content, 'lxml')
        goods = []
        navigation = html.find('div', class_='ctlg-pages-count')
        if navigation:
            max_page = int(navigation.find('div', class_='ctlg-pages-count').text.split()[-1])
        else:
            max_page = 1
        for i in range(1, max_page + 1):
            print('cтраница %i' % i)
            r = requests.get(first_page + '/page' + str(i))
            html = BeautifulSoup(r.content, 'lxml')

            articles = []
            for el in html.find_all("li", class_="j_articlecode"):
                article = el.text.replace("Артикул: ", '')
                articles.append(article)
            for el, article in zip(html.find('ul', class_='ctlg-items').children, articles):
                try:
                    title = el.find('div', class_='ctlg-name').text
                    product_number = article
                    check_colors = el.find('div', class_='j_colors')
                    if check_colors is not None:
                        href = check_colors.select('.j_child')[0]['data-hash']
                    else:
                        href = el.find('a', class_='ctlg-link')['href']
                    goods.append({'title': title, 'href': href, 'vendor code': product_number})
                except Exception:
                    traceback.print_exc()
                    continue

        return goods

    def parser_good(self, page):
        r = requests.get(page)
        html = BeautifulSoup(r.content, 'html.parser')
        main_good = self.pars_good_main(page)

        item_other_colors_box = html.select('.itm-clrs')
        if item_other_colors_box:
            other_colors = item_other_colors_box[0].select('a')
            for item in other_colors:
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
            html = BeautifulSoup(r.content, 'html.parser')
            breadcrumbs = html.select('ul', class_='brdc')[0].select('li')[-3:]
            section = breadcrumbs[0].select('span')[0].text.strip()
            vendor_code = breadcrumbs[2].select('span')[0].text.split()[1]
            name = html.find('h1', itemprop="name").text
            print(name)
            price = float(html.find('meta', itemprop='price')['content'])
            amount_of_sizes = {}
            all_sizes = html.find_all('tr', 'j_salearticle')
            for line in all_sizes:
                size = line.find('td', class_='itm-ord-size')
                if size:
                    size = self.parent.get_size(size.text.strip())
                else:
                    size = ' '
                amount = line.find('td', class_='lgnr')
                if amount is not None:
                    amount_of_sizes[size] = int(amount.find('g-number').text)
                else:
                    amount_of_sizes[size] = html.find('input', 'itm-ord-inp')["placeholder"]
            mark = html.select('.btn.itm-lbl.color--danger')
            if mark:
                mark = mark[0].text
            else:
                mark = ''
            name_block = html.find('h1', itemprop='name').text.strip()
            if len(name_block.split(', ')) == 1:
                color = name_block.split(' ')[-1]
            else:
                color = name_block.split(', ')[-1]
            materials = ''
            for item in html.find('ul', class_='itm-opts').find_all('li'):
                if 'Материал' in item.text.strip():
                    materials = item.text.strip().replace('Материал', '')
                    break
            description = html.find('div', itemprop='description')
            if description:
                description = description.text
            else:
                description = ''
            # print(page)
            return {'name': name, 'price': [price], 'section': section, 'marks': [mark],
                    'color': [color], 'page': [page], 'materials': materials, 'descriptions': [description],
                    'sizes': [amount_of_sizes], 'vendor_code': [vendor_code]}
        except Exception as e:
            traceback.print_exc()
            print(e)
            return None


if __name__ == '__main__':
    s = Gifts('0')
    # for key, val in s.parser_good('https://gifts.ru/id/110687').items():
    #     print(key, val)
    # print(s.parser_goods('/catalog/polo-s-logotipom'))

    # first_page = s.main_page + '/catalog/futbolki'[1:]
    # r = requests.get(first_page)
    # html = BeautifulSoup(r.content, 'lxml')
    # goods = []
    # navigation = html.select('.paginator')
    # if navigation:
    #     max_page = int(navigation[0].select('li')[-1].text)
    # else:
    #     max_page = 1
    # for i in range(1, max_page + 1):
    #     print('cтраница %i' % i)
    #     r = requests.get(first_page + '/page' + str(i), headers={'user-agent':
    #                                                                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.1.985 Yowser/2.5 Safari/537.36'})
    #     html = BeautifulSoup(r.content, 'lxml')
    #
    #     articles = []
    #     for el in html.find_all("li", class_="j_articlecode"):
    #         article = el.text.replace("Артикул: ", '')
    #         articles.append(article)
    #     for j in html.find('ul', class_='ctlg-items').children:
            # print(j.find('div', class_='ctlg-name').text)
            # print(j)
    #     for el, article in zip(html.find_all("div", class_='ctlg-item'), articles):
    #         title = el.find('div', class_='ctlg-name').text
    #         product_number = article
    #         check_colors = el.find('div', class_='j_colors')
    #         if check_colors is not None:
    #             href = check_colors.select('.j_child')[0]['data-hash']
    #         else:
    #             href = el.select('.catalog-grid-link')[0]['href']
    #         goods.append({'title': title, 'href': href, 'vendor code': product_number})
    #
    # return goods
