import telegram


def error_handler(text, tg_token, master_id):
    bot = telegram.Bot(token=tg_token)
    bot.send_message(text=text, chat_id=master_id)
