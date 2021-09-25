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

    @bot.gateway.command
    def hello_world(response):
        if response.event.ready_supplemental:
            user = bot.gateway.session.user
            print(f'Logged in as {user["username"]}#{user["discriminator"]}')

        if response.event.message:
            m = response.parsed.auto()
            guild_id = m['guild_id'] if 'guild_id' in m else None
            channel_id = m['channel_id']
            username = m['author']['username']
            discriminator = m['author']['discriminator']
            content = m['content']
            print(f'> guild {guild_id} channel {channel_id} | {username}#{discriminator}: {content}')

    bot.gateway.run(auto_reconnect=True)


if __name__ == '__main__':
    main()
