import os

from dotenv import load_dotenv
import requests


load_dotenv()

TOKEN = os.environ['TOKEN']

def main():
    headers = {
        'Authorization': f'Bearer {TOKEN}',
    }

    url = 'https://api-ssl.bitly.com/v4/user'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(response.json())



if __name__ == '__main__':
    main()
