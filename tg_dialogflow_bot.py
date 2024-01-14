import logging

from environs import Env
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    CallbackContext

from error_handler import error_handler
from helper import detect_intent_texts

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def dialog_flow(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    answer = detect_intent_texts(
        project_id,
        chat_id,
        update.message.text,
        'ru-RU'
    )
    update.message.reply_text(answer)


def main() -> None:
    updater = Updater(tg_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, dialog_flow))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    env = Env()
    env.read_env()
    tg_token = env.str('TELEGRAM_TOKEN')
    project_id = env.str('PROJECT_ID')
    try:
        main()
    except Exception as e:
        error_handler(e)
