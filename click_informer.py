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


def is_bitlink(long_url, token):
    
    headers = {
        'Authorization': f'Bearer {token}',
    }
    short_link = get_striped(long_url)
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{short_link}'
    response = requests.get(url, headers=headers)

    return True if response.ok else False


def shorten_link(long_url, token):
    
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


def start_click_informer():
    token = os.environ['TOKEN']
    prompt = 'Введите ссылку '
    long_url = input(prompt)

    bitlink = is_bitlink(long_url, token)
    if bitlink:
        clicks_count = count_clicks(long_url, token)
        clicks_count_msg = f'По вашей ссылке прошли: {clicks_count} раз(а)'
        return clicks_count_msg
    else:
        short_link = shorten_link(long_url, token)
        short_link_msg = f'Битлинк {short_link}'
        return short_link_msg


def main():
    try:
        print(start_click_informer())
    except requests.exceptions.HTTPError as error:
        print(error)


if __name__ == '__main__':
    main()
