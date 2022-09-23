import re
import string
import time

from bs4 import BeautifulSoup, PageElement
from selenium import webdriver
from utils import generate_vendor_code

MAX_PRICE = 100000
excluded_values = ('0', 0, None, '1', 1)


def make_request(driver, page) -> BeautifulSoup:
    url = f'https://www.avito.ru/rossiya/zapchasti_i_aksessuary/zapchasti/dlya_spetstehniki-ASgBAgICAkQKJKwJjGQ?p={page}'
    driver.get(url)
    if page == 1:
        time.sleep(5)
    r = driver.page_source
    soup = BeautifulSoup(r, features='html.parser')
    result = soup.find('div', class_='items-items-kAJAg')
    return result


def parse_description(text: str) -> str:
    replace_filter = {
        '\n': ' ',
        '"': '',
        ' назадНаписатьПоказать телефон': '',
        '\\': r'\\',
        ' минут назад': '',
        'отзывовРеквизиты проверены': '',
        ' часа назад': '',
        ' отзывовНаписатьПоказать телефон': '',
        ' часа': '',
        ' минут': '',
        'VIP-объявления': '',
        ' часов': '',
        ' назад': '',
        'час назад': '',
        'НаписатьПоказать телефон': '',
        ' завершённых объявленийРеквизиты проверены': '',
        ' завершённых объявленияРеквизиты проверены': '',
        '1 час': ''
    }

    for k, v in replace_filter.items():
        text = text.replace(k, v)
    text = re.sub(r'Ещё \d* похожих объявлений продавца\S*', '', text)
    text = re.sub(r'На Авито с \w* \d*', '', text)
    text = re.sub(r'\d* отзыва\s?\w*\s?\w*', '', text)
    for i in range(len(text)):
        if text[i] in string.digits and i in (len(text), len(text)-1):
            text = text.replace(text[i], '')

    return text


def parse_html_post(post: PageElement) -> dict:
    price = post.find(itemprop='price').get('content')
    try:
        image = post.find('ul').find('li').get('data-marker')[19:]
    except:
        image = None
    title = post.find('h3').string
    description = parse_description(post.text)
    try:
        vendor_code = post.find('div',
                                class_='iva-item-text-Ge6dR iva-item-noaccent-_yEU8 text-text-LurtD '
                                       'text-size-s-BxGpL').string
    except:
        vendor_code = generate_vendor_code()
    return {
                    'price': price,
                    'title': title,
                    'description': description,
                    'image': image,
                    'vendor_code': vendor_code
                }


def is_valid_post(parsed_post: dict) -> bool:
    return parsed_post['price'] not in excluded_values and int(parsed_post['price']) < MAX_PRICE and parsed_post['image']


def parse_avito() -> list:
    driver = webdriver.Firefox()
    posts = []
    page = 0
    while len(posts) < 1000:
        page += 1
        all_posts = make_request(driver, page)
        if not all_posts:
            driver.close()
            return posts
        for post in all_posts:
            parsed_post = parse_html_post(post)
            if is_valid_post(parsed_post):
                posts.append(parsed_post)
    driver.close()
    write_to_file(posts)
    return posts
