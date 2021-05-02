import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

HEADERS = {'user-agent': 'Opera/9.97 (X11; Linux i686; en-US) Presto/2.12.288 Version/11.00'}


MAIN_URL = 'https://www.citilink.ru'

def get_html(url, params=None):
    """
    Sending request to the site. Successful connection to the site is 200.
    Header uses here.
    :param url:
    :param params:
    :return:
    """
    return requests.get(url, headers=HEADERS, params=params)

def parsing(url):
    """
    Parsing site, using BeautifulSoup. Studied the structure of the site and brought out the element I needed.
    :param url:
    :return:
    """
    soup = bs(url, "lxml")
    elements = soup.find_all('div', class_="product_data__gtm-js product_data__pageevents-js ProductCardHorizontal js--ProductCardInListing js--ProductCardInWishlist")
    data = []

    for element in  elements:
        name_list = element.find('div', class_="ProductCardHorizontal__header-block").find('a').get_text(strip=True)
        try:
            price = int(element.find('span', class_="ProductPrice__price ProductCardHorizontal__price__price").get_text(strip=True).replace('₽','').replace(' ',''))
            kz_p = price * 6
        except AttributeError:
            price = None
            kz_p = None

        try:
            feed = float(element.find(class_="ProductCardHorizontal__count IconWithCount__count js--IconWithCount__count").get_text(strip=True))
        except AttributeError:
            feed = None
        try:
            rr = []
            exist = element.find('div', class_="ProductDeliveryInfo__stock-info").find_all('a')
            for i in exist:
                rr.append(i.get_text().strip())
                break
        except AttributeError:
            rr = ['']

        data.append({
            'Name' : name_list.replace('Ноутбук ','').replace('Смартфон ','').replace('Компьютер ','').replace('Планшет ','').replace('Моноблок ','').replace('Ультрабук ','').split(',')[0],
            'Colour' : name_list.replace('Ноутбук ','').split(',')[-1].strip(),
            'Price in Rouble' : price,
            'Price in Tenge' : kz_p,
            'Evaluation' : feed,
            'In stock': ''.join(rr),
            'Url' : MAIN_URL + element.find('div', class_="ProductCardHorizontal__header-block").find('a').get('href')

        })

    return data

def pagination(url):
    """
    Function for counting pages in catalog
    :param url:
    :return:
    """
    soup = bs(url, "lxml")
    pages = soup.find('a', class_="PaginationWidget__page js--PaginationWidget__page PaginationWidget__page_last PaginationWidget__page-link")
    if pages:
        return int(pages.get_text(strip=True))
    else:
        return 1



def start_parser(web):
    """
    Main function.
    Here, I combined all the function for parsing content from the site
    :param web:
    :return:
    """
    html = get_html(web)

    if html.status_code==200:
        data = []
        for i in range(1, pagination(html.text)+1):
            url = f'{web}' + f'?p={i}'
            data.extend(parsing(get_html(url).text))

        return data
    else:
        return print(html.status_code, ' NONE')


main_urls = ['https://www.citilink.ru/catalog/noutbuki/', 'https://www.citilink.ru/catalog/kompyutery/', 'https://www.citilink.ru/catalog/monobloki/',
             'https://www.citilink.ru/catalog/ultrabuki/', 'https://www.citilink.ru/catalog/smartfony/', 'https://www.citilink.ru/catalog/planshety/']


#for url in main_urls:
    #df = pd.DataFrame(start_parser(url))
    #name = url.replace('https://www.citilink.ru/catalog/','').replace('/','') + '.csv'
    #print(name)
    #df.to_csv(name)


#df_comp = pd.DataFrame(start_parser('https://www.citilink.ru/catalog/kompyutery/'))
# Меняешь ссылку и имя csv файла
#df_comp.to_csv('kompyutery.csv')
#print(df_comp)

#df_nout = pd.DataFrame(start_parser('https://www.citilink.ru/catalog/noutbuki/'))
# Меняешь ссылку и имя csv файла
#df_nout.to_csv('noutbuki.csv')
#print(df_nout)

#df_mono = pd.DataFrame(start_parser('https://www.citilink.ru/catalog/monobloki/'))
# Меняешь ссылку и имя csv файла
#df_mono.to_csv('monobloki.csv')
#print(df_mono)

#df_ultra = pd.DataFrame(start_parser('https://www.citilink.ru/catalog/ultrabuki/'))
# Меняешь ссылку и имя csv файла
#df_ultra.to_csv('ultrabuki.csv')
#print(df_ultra)

#df_phone = pd.DataFrame(start_parser('https://www.citilink.ru/catalog/smartfony/'))
# Меняешь ссылку и имя csv файла
#df_phone.to_csv('smartfony.csv')
#print(df_phone)

df_plan = pd.DataFrame(start_parser('https://www.citilink.ru/catalog/planshety/'))
# Меняешь ссылку и имя csv файла
df_plan.to_csv('planshety.csv')
print(df_plan)
