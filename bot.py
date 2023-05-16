from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from rivescript import RiveScript
from dotenv import load_dotenv
import os

# Загружаем переменные среды из файла .env
load_dotenv()

# Получаем токен VK API из переменных среды
vk_token = os.getenv('VK_TOKEN')

# Создаем экземпляр RiveScript и загружаем файлы
bot = RiveScript()
bot.load_file('bakery.rive')
bot.sort_replies()

# Авторизуемся в VK
vk_session = VkApi(token=vk_token)
longpoll = VkLongPoll(vk_session)

# Обработчик входящих сообщений
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # Получаем текст сообщения от пользователя
        message = event.text

        # Отвечаем, используя RiveScript
        reply = bot.reply('localuser', message)

        # Отправляем ответ пользователю
        vk_session.method('messages.send', {'user_id': event.user_id, 'message': reply, 'random_id': 0})
