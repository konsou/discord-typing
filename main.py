import json
from os import getenv

import discum
from dotenv import load_dotenv

load_dotenv()


def load_settings(settings_filename: str) -> dict:
    with open(settings_filename, encoding='utf-8') as f:
        return json.load(f)


def main():
    settings = load_settings('settings.json')
    print(settings)
    token = getenv('TOKEN')
    print(token)
    bot = discum.Client(token=token)

    pass


if __name__ == '__main__':
    main()
