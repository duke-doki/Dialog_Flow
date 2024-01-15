import logging

from environs import Env
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    CallbackContext

from error_handler import error_handler
from detect_intent import detect_intent_texts


logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def response(update: Update, context: CallbackContext, project_id) -> None:
    chat_id = update.effective_chat.id
    answer, is_fallback = detect_intent_texts(
        project_id,
        chat_id,
        update.message.text,
        'ru-RU'
    )
    update.message.reply_text(answer)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    env = Env()
    env.read_env()
    tg_token = env.str('TELEGRAM_TOKEN')
    master_id = env.str('MASTER_ID')
    project_id = env.str('PROJECT_ID')
    try:
        updater = Updater(tg_token)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))

        dispatcher.add_handler(
            MessageHandler(
                Filters.text & ~Filters.command,
                lambda update, context: response(update, context, project_id)
            )
        )

        updater.start_polling()

        updater.idle()
    except Exception as e:
        error_handler(e, tg_token, master_id)
