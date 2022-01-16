import argparse
import csv
import socket
import sys

import requests
import socks
from bs4 import BeautifulSoup

PORT_TOR = 9050
TOR = 'tor'
PROXY = 'proxy'
FILE_PROXY = './proxies.csv'
URL = 'http://checkip.dyndns.org'
SEPARATOR = "*" * 75


def create_parser():
    """
    Parsing command line for get params: proxy, tor
    :return: argparse object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(f'-{TOR[:1]}', f'--{TOR}', action='store_const',
                        const=True)
    parser.add_argument(f'-{PROXY[:1]}', f'--{PROXY}', action='store_const',
                        const=True)

    return parser


class Print:
    """
    Color print.
    """

    @staticmethod
    def red(text):
        """
        :param text: output text
        :return: None
        """
        print("\033[31m {}".format(text))

    @staticmethod
    def yellow(text):
        """
        :param text: output text
        :return: None
        """
        print("\033[33m {}".format(text))


class CheckIP:
    """Class for testing using ip"""

    def __init__(self, param: str = None):
        """
        Initialisation
        :param param: tor, proxy or None
        """
        self.param = param

        if param == TOR:
            socks.set_default_proxy(socks.SOCKS5, "localhost", PORT_TOR)
            socket.socket = socks.socksocket
            print(SEPARATOR)
            print('Tor checking')
            print(SEPARATOR)

        self.host = self.port = self.user = self.password = ""
        self.session = requests.Session()
        if param == PROXY:
            with open(FILE_PROXY, newline='') as f:
                reader = csv.reader(f)
                data = list(reader)

                if len(data) > 1:
                    self.host = data[1][0]
                    self.port = data[1][1]
                    self.user = data[1][2]
                    self.password = data[1][3]
                else:
                    Print.red(f'Error read data in file {FILE_PROXY}')

            print(SEPARATOR)
            print('Proxy checking')
            print(f'User: {self.host}')
            print(f'User: {self.port}')
            print(f'User: {self.user}')
            print(f'User: {self.password}')
            print(SEPARATOR)

            proxies = {
                "http": f"http://{self.user}:{self.password}@{self.host}:{self.port}/",
                "https": f"https://{self.user}:{self.password}@{self.host}:{self.port}/"
            }
            self.session.proxies = proxies

    def check_ip(self):
        """
        Get ip from URL
        :return:
        """
        if self.param == TOR:
            try:
                ip = self.session.get(URL).content
            except Exception as e:
                ip = None
                Print.yellow(
                    f'No connection to the tor network. Check if the installation is correct'
                    f' ($ tor --version), status ($ sudo /etc/init.d/tor status) or '
                    f'port number {PORT_TOR=} ($ netstat -nlp --inet).')
                print(SEPARATOR)
                Print.red(f'Error: {e}')
        elif self.param == PROXY:
            try:
                ip = self.session.get(URL).content
            except Exception as e:
                ip = None
                Print.yellow(
                    f'The {FILE_PROXY} file contains incorrect proxy data.')
                print(SEPARATOR)
                Print.red(f'Error: {e}')

        else:
            ip = self.session.get(URL).content

        if ip:
            soup = BeautifulSoup(ip, 'lxml')
            print(soup.find('body').text)


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    param = ''
    if namespace.tor:
        param = TOR
    elif namespace.proxy:
        param = PROXY

    CheckIP(param=param).check_ip()


if __name__ == '__main__':
    main()
