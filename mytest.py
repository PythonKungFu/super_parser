from bs4 import BeautifulSoup
import requests


def pars_good_main(page):
    try:
        r = requests.get(page)
        html = BeautifulSoup(r.content, 'html.parser')
        breadcrumbs = html.select('ul', class_='brdc')[0].select('li')[-3:]
        section = breadcrumbs[0].select('span')[0].text.strip()
        vendor_code = breadcrumbs[2].select('span')[0].text.split()[1]
        name = html.find('h1', itemprop="name").text
        price = float(html.find('meta', itemprop='price')['content'])
        amount_of_sizes = {}
        all_sizes = html.find_all('tr', 'j_salearticle')
        for line in all_sizes:
            size = line.find('td', class_='itm-ord-size')
            if size:
                size = "self.parent.get_size(size.text.strip())"
            else:
                size = ''
            amount = line.find('td', class_='lgnr')
            try:
                if amount is not None:
                    amount_of_sizes[size] = int(amount.find('g-number').text)
                else:
                    amount_of_sizes[size] = line.find('input')["placeholder"]
            except:
                amount_of_sizes[size] = 1
        mark = html.select('.btn.itm-lbl.color--danger')
        if mark:
            mark = mark[0].text
        else:
            mark = ''
        name_block = html.find('h1', itemprop='name').text.strip()
        print(name_block)
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
        return {'name': name, 'price': [price], 'section': section, 'marks': [mark],
                'color': [color], 'page': [page], 'materials': materials, 'descriptions': [description],
                'sizes': [amount_of_sizes], 'vendor_code': [vendor_code]}
    except Exception as e:
        print(e, 'OK')
        return None

def parser_good(page):
    r = requests.get(page)
    html = BeautifulSoup(r.content, 'html.parser')
    main_good = pars_good_main(page)

    item_other_colors_box = html.select('.itm-clrs')
    if item_other_colors_box:
        other_colors = item_other_colors_box[0].select('a')
        for item in other_colors:
            url = 'https://gifts.ru/' + item['href'][1:]
            good_color = pars_good_main(url)
            if good_color is not None:
                main_good['price'].extend(good_color['price'])
                main_good['page'].extend(good_color['page'])
                main_good['color'].extend(good_color['color'])
                main_good['descriptions'].extend(good_color['descriptions'])
                main_good['sizes'].extend(good_color['sizes'])
                main_good['marks'].extend(good_color['marks'])
                main_good['vendor_code'].extend(good_color['vendor_code'])
    return main_good


print(parser_good('https://gifts.ru/id/41417'))
