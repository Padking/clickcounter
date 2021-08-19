import os

from dotenv import load_dotenv
import requests


load_dotenv()


def main():
    
    TOKEN = os.environ['TOKEN']
    long_url = 'https://hctraktor.org/team/players/'

    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json',
    }
    url = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {
        'long_url': f'{long_url}'
    }
    
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    print(response.json()['link'])


if __name__ == '__main__':
    main()
