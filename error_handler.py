import telegram
from environs import Env


env = Env()
env.read_env()


def error_handler(text):
    tg_token = env.str('TELEGRAM_TOKEN')
    master_id = env.str('MASTER_ID')
    bot = telegram.Bot(token=tg_token)
    bot.send_message(text=text, chat_id=master_id)
