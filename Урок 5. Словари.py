# Одно значение в словаре
# a = {
    # 'молоко': 65,
# }
# print(a['молоко'])


# Несколько значений в словаре
# a = {
    # 'молоко': 65,
    # 'кефир': 70
# }
# print(a['кефир'])


# Отдельное значение предмета из словаря
# a = {
    # 'молоко': 65,
    # 'кефир': 70,
    # 'список': [12,242,231,5]
# }
# s = []
# print(a['список'][1])


# Мини-переводчик
# english_dict = {
    # 'яблоко': 'apple',
    # 'молоко': 'milk',
    # 'кот': 'cat'
# }
 # word = input('Введите слово на русском языке')
 # if word in english_dict:
     # print(word + ' на английском языке будет: ' + english_dict[word])
 # else:
     # print('такого слова нет в словаре')
     # где word - ключ к значению


# Вытаскивание главного актёра из списка фильмов
# films_dict = {
    # 'Начало': ' Леонардо Ди Каприо',
    # 'Человек паук': 'Том холанд',
    # 'Терминатор': 'Арнольд Шварцнеггер',
    # 'Драйв': 'Райан Гослинг'
# }
# favorite_actor = 'Райан Гослинг'
# film = input('Введите фильм, который хотите посмотреть: ')
# if film in films_dict:
    # actor = films_dict[film]
  # if actor == favorite_actor:
       # print('Этот фильм точно стоит посмотреть! ')
  # else:
       # print('Я бы не смотрел')
   # else:
# print('Такого фильма в списке нет!')


# Опросник
# questions = [
   # {
        # 'question':'Кто играл человека-паука?',
        # 'answer': ['Тоби Магуайер','Том Холанд'],
        # 'right_answer': 1
    # },
# answer = [
# {
#     'question':'Какого цвета костюм у человека-паука?',
# 'answer': ['Красного','Синего','Чёрного'],
# 'right_answer': 2
# }]
# for question in questions:
    # print(question['question'])
    # answer_number = 0
# for answer in question ['answer']:
    # answer_number = answer_number + 1
    # print(answer_number, answer)
    # user_answer = int(input('Введите ваш ответ: '))
   # if user_answer == question['right_answer']:
        #print('Верно')
    # else:
        # print('Неверно')


#Счётчик длительности треков
#violator_songs = {
    #'Close eyes': 4.86,
    #'Phonky town': 4.43,
    #'Personal Jesus': 4.56,
    #'Halo': 4.9,
    #'Jajoja': 6.07,
    #'Enjoy the Silence': 4.20,
    #'This Feeling': 4.76,
    #'Blue Dress': 4.29,
    #'Clean': 5.83
#}
#count = int(input('Сколько песен выбрать? '))
#all_time = 0.0
#for i in range(count):
    #query = f'Название {i + 1} песни: '
    #song_name = input(query)
    #all_time += violator_songs.get(song_name, 0)
#print(f'Общее время звучания песен: {round(all_time, 2)} минут')



#Счётчик стоимости предметов в магазине
#goods = {
    #'Лампа': '12345',
    #'Стол': '23456',
    #'Диван': '34567',
    #'Стул': '45678',
#}
#store = {
    #'12345': [
        #{'quantity': 27, 'price': 42},
    #],
    #'23456': [
       # {'quantity': 22, 'price': 510},
        #{'quantity': 32, 'price': 520},
    #],
    #'34567': [
       # {'quantity': 2, 'price': 1200},
        #{'quantity': 1, 'price': 1150},
    #],
    #'45678': [
      # {'quantity': 50, 'price': 100},
       # {'quantity': 12, 'price': 95},
       # {'quantity': 43, 'price': 97},
    #],
#}
#for product_name, product_code in goods.items():
   # item_t_q = 0
    #item_t_c = 0
    #for product in store[product_code]:
        #item_q = product['quantity']
        #item_cost = product['price']
        #item_t_c += item_q * item_cost
        #item_t_q += item_q
    #print('{0} - {1} шт, общая стоимость {2} рублей'.format(product_name, item_t_q, item_t_c))



