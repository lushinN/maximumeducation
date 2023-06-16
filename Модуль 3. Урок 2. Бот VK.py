#VK бот
import vk_api
import course

token = 'vk1.a.eDWLhAAXEBiGiR_-n0xeOHNm1vsA3fqarClpMg6Ndj9n01r01kzD1kY6K-_g6r6r2x6f9a8K0SU9p7domXpt8DFcrApCj0hnTcW5CuTUoMF54UtV5XgIXKfpWyGO4MeTvzBC_eiMffXjmkgPzfEkYga8PdbLnx-h2LlgzpoRi1-c5fInu0aPGxbROYup5IbSuQv7QMuB8ZC5LRTo-jPx1g'


vk = vk_api.VkApi(token=token)

messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})


while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] >= 1:
        print(messages)
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']
        if 'привет' in message_text.lower():
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Вечер в хату'})
        elif 'курс' in message_text.lower():
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': course.get_course('R01235')})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Чурка что ли?'})



# items = [первый диалог, второй диалог, ...]