import os
from urllib.parse import urlparse

from dotenv import load_dotenv
import requests


load_dotenv()


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


def main():
    token = os.environ['TOKEN']
    long_url = input('Введите ссылку ')
    
    try:
        short_link = shorten_link(token, long_url)
    except requests.exceptions.HTTPError as error:
        print(error)
    else:
        print('Битлинк', short_link)


if __name__ == '__main__':
    main()
