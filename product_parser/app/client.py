import requests

from settings import PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS


class Client:
    def __init__(self, use_proxy: bool = False):
        self.session = requests.Session()
        self.session.headers = self.set_headers(check_mobile=False)

        if use_proxy:
            self.session.proxies = self.set_proxy()

    def __str__(self):
        return f'Объект класса {self.__class__.__name__}'

    @staticmethod
    def set_proxy():
        if PROXY_USER:
            proxies = {
                "http": f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}/",
                "https": f"https://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}/"
            }
        else:
            proxies = {
                "http": f"http://{PROXY_HOST}:{PROXY_PORT}/",
                "https": f"https://{PROXY_HOST}:{PROXY_PORT}/"
            }

        return proxies

    @staticmethod
    def set_headers(check_mobile: bool = False):
        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
        headers = {'user-agent': user_agent, }

        return headers
