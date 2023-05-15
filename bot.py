# bot.py

from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from rivescript import RiveScript

# Создаем экземпляр RiveScript и загружаем файлы
bot = RiveScript()
bot.load_file('bakery.rive')
bot.sort_replies()

# Авторизуемся в VK
vk_session = VkApi(token='vk1.a.PBxP7znrHAaZpqsnZB0Mav4JJRX5jo_eHdZ33Kf0P2_h-m8qGRS2b4jE8KjitVIEFQPLtnCj7Vko94PjNPJ8Mlwpp2DcsWPrs-CviXA1rrlTU-lyK8DwUQQ1xrPJ3NZrn4ZpQ5VokMLI96ATS5IDc2vKflC8tkRMj1kupNMYYjWA010CYEqchh6R6YnuI-4zgHy3ECXC9Jmvz20osUYZwg')
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
