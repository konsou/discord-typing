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
    user_ids_to_watch = settings['user-ids-to-watch']
    token = getenv('TOKEN')
    bot = discum.Client(token=token)

    @bot.gateway.command
    def hello_world(response):

        if response.event.typing:
            parsed = response.parsed.auto()
            user_id = parsed['user_id']
            channel_id = parsed['channel_id']
            if user_id in user_ids_to_watch:
                bot.typingAction(channel_id)

        if response.event.ready_supplemental:
            user = bot.gateway.session.user
            print(f'Logged in as {user["username"]}#{user["discriminator"]}')

    bot.gateway.run(auto_reconnect=True)


if __name__ == '__main__':
    main()
