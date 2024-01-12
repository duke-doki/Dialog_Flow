import random

import vk_api as vk
from environs import Env
from vk_api.longpoll import VkLongPoll, VkEventType

from helper import detect_intent_texts

env = Env()
env.read_env()


def dialog_flow(event, vk_api):
    answer = detect_intent_texts(
        project_id,
        event.user_id,
        event.text,
        'ru-RU'
    )
    vk_api.messages.send(
        user_id=event.user_id,
        message=answer,
        random_id=random.randint(1,1000)
    )


def main():
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            dialog_flow(event, vk_api)


if __name__ == "__main__":
    vk_token = env.str('VK_TOKEN')
    project_id = env.str('PROJECT_ID')
    main()