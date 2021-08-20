import os
from urllib.parse import urlparse

from dotenv import load_dotenv
import requests


load_dotenv()


def count_clicks(bitlink, token, **kwargs):

    unit = kwargs.pop('unit', 'day')
    units = kwargs.pop('units', -1)

    if kwargs:  # фактические параметры всё-таки остались
        raise TypeError(f'Неподдерживаемые параметры: {list(kwargs)}')

    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = (
        ('unit', unit),
        ('units', units),

    )

    short_link = get_striped(bitlink)
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{short_link}/clicks/summary'
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']

    return clicks_count


def shorten_link(token, long_url):
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    url = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {
        'long_url': f'{long_url}'
    }
    
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    link = response.json()['link']
    short_link = get_striped(link)

    return short_link


def get_striped(url):
    """Формирует URL без SCHEME-части."""

    parsed = urlparse(url)
    scheme = f'{parsed.scheme}://'
    url_without_scheme_path = parsed.geturl().replace(scheme, '', 1)

    return url_without_scheme_path


def get_shortened_bitlink():
    token = os.environ['TOKEN']
    prompt = 'Введите ссылку '
    long_url = input(prompt)
    
    try:
        short_link = shorten_link(token, long_url)
    except requests.exceptions.HTTPError as error:
        print(error)
    else:
        print('Битлинк', short_link)


def get_clicks_count():
    token = os.environ['TOKEN']
    prompt = 'Введите ссылку '
    bitlink = input(prompt)
    
    try:
        clicks_count = count_clicks(bitlink, token)
    except requests.exceptions.HTTPError as error:
        print(error)
    else:
        clicks_count_msg = f'По вашей ссылке прошли: {clicks_count} раз(а)'
        print(clicks_count_msg)


if __name__ == '__main__':
    get_clicks_count()
