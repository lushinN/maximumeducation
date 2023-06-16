# VK_BOT
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import get_course

token = 'vk1.a.eDWLhAAXEBiGiR_-n0xeOHNm1vsA3fqarClpMg6Ndj9n01r01kzD1kY6K-_g6r6r2x6f9a8K0SU9p7domXpt8DFcrApCj0hnTcW5CuTUoMF54UtV5XgIXKfpWyGO4MeTvzBC_eiMffXjmkgPzfEkYga8PdbLnx-h2LlgzpoRi1-c5fInu0aPGxbROYup5IbSuQv7QMuB8ZC5LRTo-jPx1g'

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api() #это чтобы всегда метод не писать

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
       msg = event.text
       user_id = event.user_id
       msg_id = event.message_id
       if msg.lower() == 'привет':
           vk.messages.send(user_id = user_id, random_id = msg_id, message = 'Покумарить пора!')
       elif msg.lower() == 'курс доллар':
           response = f'{get_course("R01235")} рублей за 1 доллар'
           vk.messages.send(user_id=user_id, random_id=msg_id, message=response)
       elif msg.lower() == 'курс евро':
           response = f'{get_course("R01239")} рублей за 1 евро'
           vk.messages.send(user_id=user_id, random_id=msg_id, message=response)
       elif msg.lower() == 'курс юань':
           response = f'{get_course("R01375")} рублей за 1 юаней'
           vk.messages.send(user_id=user_id, random_id=msg_id, message=response)
       else:
           vk.messages.send(user_id = user_id, random_id = msg_id, message = 'Жидкий ле, нефор биля!')



