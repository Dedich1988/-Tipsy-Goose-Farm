from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType

import os
from dotenv import load_dotenv

load_dotenv()

vk_token = os.getenv('VK_TOKEN')

# Авторизуемся как сообщество
vk_session = VkApi(token=vk_token)

# Инициализируем работу с longpoll
longpoll = VkLongPoll(vk_session)

# Основной цикл
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # Сообщение от пользователя пришло, отправим его обратно
        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Hello, world!', 'random_id': 0})
