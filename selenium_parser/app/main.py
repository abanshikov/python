import csv
from time import sleep

from selenium.webdriver.common.keys import Keys

from browser_setting import *
from settings import *

URL = 'адрес исследуемого сайта'
SCROLL_PAUSE_TIME = 0.2
BTN_DOWN_PAUSE_TIME = 5


def write_list_to_string(file_name: str, data: list):
    """
    Save data to scv-file
    :param file_name:
    :param data:
    :return:
    """
    file_name = PATH_CSV + file_name
    with open(file_name, 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerow(data)


class Parser:
    """
    Data acquisition control class
    """

    def __init__(self, driver):
        self.driver = driver

    def go_down_and_click(self):
        """
        Imitation of scroll work
        :return:
        """
        for i in range(14):
            body = self.driver.find_element_by_css_selector('body')
            body.send_keys(Keys.PAGE_DOWN)
            sleep(SCROLL_PAUSE_TIME)

        btn = self.driver.find_element_by_css_selector(
            'div.WidthLimiter > '
            'div.WidthLimiter__InnerContent >'
            'div.VerticalLayout__ShowMoreContainer >'
            'button.Button__StyledButton')
        btn.click()
        log.debug('sleep btn down')
        sleep(BTN_DOWN_PAUSE_TIME)

    def get_items(self, url: str):
        """
        Getting data.
        :param url:
        :return:
        """
        self.driver.get(url)
        while True:
            try:
                self.go_down_and_click()
            except Exception as error:
                log.error(error)
                break
        items = self.driver.find_elements_by_css_selector(
            'div.ProductCard__Root')
        aa = [item.find_element_by_css_selector(
            'a.ConditionalLinkWrapper__StyledLink') for item in items]
        links = [a.get_attribute('href') for a in aa]
        write_list_to_string(file_name='01_list_urls_reviews.csv', data=links)
        self.driver.close()


def main():
    driver = get_chromedriver(use_proxy=True, user_agent="")
    parser = Parser(driver=driver)
    parser.get_items(f'{URL}/url_path/')
    sleep(300)


if __name__ == '__main__':
    main()
