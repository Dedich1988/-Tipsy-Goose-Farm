from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from rivescript import RiveScript

import os
from dotenv import load_dotenv

load_dotenv()

vk_token = os.getenv('VK_TOKEN')

# Авторизуемся как сообщество
vk_session = VkApi(token=vk_token)

# Инициализируем работу с longpoll
longpoll = VkLongPoll(vk_session)

# Создаем экземпляр RiveScript и загружаем файлы
bot = RiveScript(utf8=True, debug=False)
bot.load_directory(".")
bot.sort_replies()

# Функция для обработки сообщений от пользователя
def bot_reply(text):
    reply = bot.reply("user", text)
    reply_text = reply.strip()
    return reply_text

# Основной цикл
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # Получаем текст сообщения от пользователя
        message = event.text

        # Отвечаем, используя RiveScript
        reply = bot_reply(message)

        # Отправляем ответ пользователю
        vk_session.method('messages.send', {'user_id': event.user_id, 'message': reply, 'random_id': 0})
