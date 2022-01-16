import csv
import sqlite3
from itertools import zip_longest
from multiprocessing import Pool
from time import sleep

import pandas as pd
from bs4 import BeautifulSoup

from client import *
from settings import *

URL = 'адрес для парсинга'
COUNT_PROCESS = 40


def multithreading(function, all_links):
    with Pool(COUNT_PROCESS) as p:
        p.map(function, all_links)


def chunks(lst, count):
    n = len(lst) // count
    return list(x for x in zip_longest(*[iter(lst)] * n))


class CSV:
    """
    Class quick save csv-file.
    """

    def __init__(self, file_name):
        self.file_name = PATH_CSV + file_name

    def write_list_to_string(self, list_data):
        with open(self.file_name, 'a', encoding='utf8', newline='') as f:
            writer = csv.writer(f, delimiter='\n')
            writer.writerow(list_data)

    def write_new_list_to_string(self, list_data):
        with open(self.file_name, 'w', encoding='utf8', newline='') as f:
            writer = csv.writer(f, delimiter='\n')
            writer.writerow(list_data)

    def read_string(self):
        with open(self.file_name, newline='') as f:
            reader = csv.reader(f)
            list_data = list(reader)
        list_string = []
        for string in list_data:
            list_string.append(string[0])
        return list_string

    def write_data(self, data):
        order = sorted(list(data.keys()))
        with open(self.file_name, 'a', encoding='utf8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=order, delimiter=';')
            writer.writerow((data))


class ManageSave:
    def __init__(self, data: dict):
        """
        Class for saving data
        :param data: dictionary with data
        """
        self.file_name = FILE_NAME
        self.data = data
        self.df = None

    def manage_save(self):
        """
        Control writing data
        :return: None
        """
        self.set_pandas_dat()
        self.write_csv()
        self.write_db()

    def set_pandas_dat(self):
        """
        Creating DataFrame with pandas
        :return: None
        """
        columns = sorted(list(self.data.keys()))
        self.df = pd.DataFrame(self.data, columns=columns)

    def write_db(self):
        """
        Create and save *.db file sqlite
        :return: None
        """
        file_name = self.file_name + '.db'
        columns = sorted(list(self.data.keys()))
        conn = sqlite3.connect(file_name)
        c = conn.cursor()
        command = f"CREATE TABLE IF NOT EXISTS {TABLE_DB} ({','.join(columns)})"
        c.execute(command)
        conn.commit()
        self.df.to_sql(TABLE_DB, conn, if_exists='append', index=False)

    def write_csv(self):
        """
        Save csv-file
        :return: None
        """
        file_name = self.file_name + '.csv'
        if os.path.exists(file_name):
            check_head = False
        else:
            check_head = True
        self.df.to_csv(file_name, index=False, header=check_head, mode='a')


class Scrapper:
    """
    Class parsing data.
    """

    def __init__(self, client):
        self.client = client

    def get_list_category(self, url: str, file_name: str):
        """
        Getting category product.
        :param url: parsing address
        :param file_name: file name for saving
        :return:
        """
        response = self.client.session.get(url=url, params={})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            uls = soup.select('ul.product-category-list')
            category_urls = []
            for ul in uls:
                lis = ul.select('li.product-category-list-item')
                for li in lis:
                    link = URL + li.select_one('a').get('href')
                    category_urls.append(link)
            csv_ = CSV(file_name=file_name)
            csv_.write_list_to_string(list_data=category_urls)

    def get_total_page(self, url: str):
        """
        Getting the total number of pages
        :param url:
        :return:
        """
        response = self.client.session.get(url=url, params={})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            try:
                ul = soup.select_one('ul.pagination')
            except Exception as e:
                return 1

            try:
                li = ul.select('li')[-1]
            except Exception as e:
                return 1

            try:
                total_page = li.text.strip()
                return total_page
            except Exception as e:
                return 1

    def get_items_urls(self, file_category: str, file_items: str):
        """
        Getting the address of the product card
        :param file_category:
        :param file_items:
        :return:
        """
        file_category_ = CSV(file_name=file_category)
        category_urls = file_category_.read_string()
        for i, url in enumerate(category_urls):
            log.info(f'Get items from url #{i + 1} by {len(category_urls)}')
            total_page = int(self.get_total_page(url=url))
            items_urls = []
            for page in range(1, total_page + 1):
                log.debug(f'Read page #{page} by {total_page}')
                params = {
                    'pageAjaxRequest': 'true',
                    'page': page,
                }
                response = self.client.session.get(url=url, params=params)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'lxml')
                    aa = soup.select('a.lightweight-item-desc')
                    for a in aa:
                        link = URL + a.get('href')
                        items_urls.append(link)
            file_items_ = CSV(file_name=file_items)
            file_items_.write_list_to_string(list_data=items_urls)
            sleep(3)

    def get_items_urls_1(self, url: str):
        """
        Getting the address of the product card
        :param url:
        :return:
        """
        total_page = int(self.get_total_page(url=url))
        log.debug(f'Get {total_page} pages by {url}')
        items_urls = []
        for page in range(1, total_page + 1):
            params = {
                'pageAjaxRequest': 'true',
                'page': page,
            }
            response = self.client.session.get(url=url, params=params)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                aa = soup.select('a.lightweight-item-desc')
                for a in aa:
                    link = URL + a.get('href')
                    items_urls.append(link)
        file_items_ = CSV(file_name='02_items_urls.csv')
        file_items_.write_list_to_string(list_data=items_urls)
        sleep(3)

    def get_items(self, url):
        """
        Getting information about a product
        :param url:
        :return:
        """
        log.debug(f'Get data from page {url}')
        keys = {'name', 'link', 'origin_number', 'brand', 'price', 'delivery'}
        data = {}
        for key in keys:
            data[key] = []

        response = self.client.session.get(url=url, params={})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            items = soup.select('div.snippet-card.fx-box')
            for i, item in enumerate(items):
                try:
                    name = item.select_one('meta[itemprop=name]').get('content')
                except Exception as e:
                    name = ''

                try:
                    a = item.select_one('a.lightweight-item-desc')
                except Exception as e:
                    a = None

                try:
                    link = URL + a.get('href')
                except Exception as e:
                    link = ''

                try:
                    origin_number = a.select_one(
                        'span[data-action=orig-number]') \
                        .get('data-number')
                except Exception as e:
                    origin_number = ''

                try:
                    brand = a.select_one(
                        'span.desc-item--link__brand').text.strip()
                except Exception as e:
                    brand = ''

                try:
                    price = item.select_one('span.price_num').text.strip()
                except Exception as e:
                    price = ''

                try:
                    delivery = item.select_one(
                        'div.lightweight-snippet-card').text.strip()
                    delivery = delivery
                    delivery = delivery.replace('\t', '')
                except Exception as e:
                    delivery = ''

                if link:
                    data['name'].append(name)
                    data['link'].append(link)
                    data['origin_number'].append(origin_number)
                    data['brand'].append(brand)
                    data['price'].append(price)
                    data['delivery'].append(delivery)

        saver = ManageSave(data)
        saver.manage_save()

    def get_big_data(self, url: str):
        """
        Running multiple processes to get information
        :param url:
        :return:
        """
        try:
            total_page = int(self.get_total_page(url=url))
        except Exception as e:
            total_page = 1

        log.debug(f'Get {total_page} pages by {url}')

        urls = []
        for page in range(1, total_page + 1):
            urls.append(f'{url}/?page={page}&pageAjaxRequest=true')

        multithreading(self.get_items, urls)

    def get_pagination_urls(self, url):
        """
        Getting pagination page addresses
        :param url:
        :return:
        """
        try:
            total_page = int(self.get_total_page(url=url))
        except Exception as e:
            total_page = 1

        log.debug(f'Get {total_page} pages by {url}')

        urls = []
        for page in range(1, total_page + 1):
            urls.append(f'{url}?page={page}&pageAjaxRequest=true')

        csv_ = CSV(file_name='01_category_urls_pagination.csv')
        csv_.write_list_to_string(list_data=urls)

    def get_data(self, url: str):
        """
        Getting all data
        :param url:
        :return:
        """
        keys = {'name', 'link', 'origin_number', 'brand', 'price', 'price_old',
                'delivery'}

        try:
            total_page = int(self.get_total_page(url=url))
        except Exception as e:
            total_page = 1

        log.debug(f'Get {total_page} pages by {url}')

        data = {}
        for key in keys:
            data[key] = []

        for page in range(1, total_page + 1):
            log.debug(f'Read page #{page} by {len(total_page)}')
            params = {
                'pageAjaxRequest': 'true',
                'page': page,
            }
            response = self.client.session.get(url=url, params=params)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                items = soup.select('div.snippet-card.fx-box')
                for i, item in enumerate(items):
                    try:
                        name = item.select_one('meta[itemprop=name]').get(
                            'content')
                    except Exception as e:
                        name = ''

                    try:
                        a = item.select_one(
                            'a.lightweight-item-desc.desc-item--link')
                    except Exception as e:
                        a = None

                    try:
                        link = URL + a.get('href')
                    except Exception as e:
                        link = ''

                    try:
                        origin_number = a.select_one(
                            'span[data-driveback-action=copy-orig-number]').get(
                            'data-orig-number')
                    except Exception as e:
                        origin_number = ''

                    try:
                        brand = a.select_one(
                            'span.desc-item--link__brand').text.strip()
                    except Exception as e:
                        brand = ''

                    try:
                        price = item.select_one(
                            'span.price_num_real').text.strip()
                    except Exception as e:
                        price = ''

                    try:
                        delivery = item.select_one(
                            'div.lightweight-snippet-card__price_remote_deliv') \
                            .text.strip()
                        delivery = delivery
                        delivery = delivery.replace('\t', '')
                    except Exception as e:
                        delivery = ''

                    if link:
                        data['name'].append(name)
                        data['link'].append(link)
                        data['origin_number'].append(origin_number)
                        data['brand'].append(brand)
                        data['price'].append(price)
                        data['delivery'].append(delivery)

        saver = ManageSave(data)
        saver.manage_save()


def main():
    client = Client(use_proxy=True)
    scrapper = Scrapper(client=client)
    scrapper.get_list_category(url=f'{URL}/url_part/',
                               file_name='01_category_urls.csv')
    scrapper.get_items_urls(file_category='01_category_urls.csv',
                            file_items='02_items_urls.csv')

    file_category_ = CSV(file_name='01_category_urls.csv')
    category_urls = file_category_.read_string()
    urls = chunks(lst=category_urls, count=200)

    for i, url_tuple in enumerate(urls):
        log.info(f'Connection #{i + 1} by {len(urls)}')
        if url_tuple:
            client = Client(use_proxy=True)
            scrapper = Scrapper(client=client)
            multithreading(scrapper.get_pagination_urls, url_tuple)
        log.warning('Sleep')
        sleep(1)

    file_category_ = CSV(file_name='01_category_urls_pagination.csv')
    category_urls = file_category_.read_string()
    urls = chunks(lst=category_urls, count=2800)

    for i, url_tuple in enumerate(urls):
        log.info(f'Connection #{i + 1} by {len(urls)}')
        if url_tuple:
            client = Client(use_proxy=True)
            scrapper = Scrapper(client=client)
            multithreading(scrapper.get_items, url_tuple)
        for url in url_tuple:
            category_urls.remove(url)
        file_category_ = CSV(
            file_name='01_category_urls_pagination_cleared.csv')
        file_category_.write_new_list_to_string(category_urls)
        log.warning('Sleep')

        if i % 50 == 0:
            sleep(30)
        else:
            sleep(1)


if __name__ == '__main__':
    main()
