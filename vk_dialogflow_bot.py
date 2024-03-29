import random

import vk_api as vk
from environs import Env
from vk_api.longpoll import VkLongPoll, VkEventType

from error_handler import error_handler
from detect_intent import detect_intent_texts


def response(event, vk_api, project_id):
    answer, is_fallback = detect_intent_texts(
        project_id,
        event.user_id,
        event.text,
        'ru-RU'
    )
    if not is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    env = Env()
    env.read_env()
    vk_token = env.str('VK_TOKEN')
    tg_token = env.str('TELEGRAM_TOKEN')
    master_id = env.str('MASTER_ID')
    project_id = env.str('PROJECT_ID')
    try:
        vk_session = vk.VkApi(token=vk_token)
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                response(event, vk_api, project_id)
    except Exception as e:
        error_handler(e, tg_token, master_id)
