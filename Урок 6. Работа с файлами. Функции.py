#Создание в файле + написание в нём
#w - write
# file = open('result.txt','w')
# file.write('Cool thing!')


#Зачитать файл
#w - write
#r - read
# file = open('result.txt','r')
# s = file.read()
# print(s)


#Зачитать файл по отдельности
#w - write
#r - read
# file = open('result.txt','r')
# for line in file.readlines():
#  print(line)

#Опросник с записью значений
#w - write
#r - read
#a - add
# questions = [
#     {
#         'question': 'Кто из героев Киновселенной Marvel начал знакомство с Землёй, попав под грузовик?',
#         'answers': ['Фил Колсон', 'Халк', 'Капитан Америка', 'Правильного ответа нет'],
#         'right_answer': 4
#     },
#     {
#         'question': 'Как звучит полное имя младшего брата Тора?',
#         'answers': ['Локи Одинсон', 'Локи Эриксон', 'Локи Лафейсон', 'Правильного ответа нет'],
#         'right_answer': 3
#     },
#     {
#         'question': 'Какой суперзлодей отличился тем, что за очень короткое время собрал в ангаре сотни управляемых дронов для армии США?',
#         'answers': ['Иван Ванко', 'Альтрон', 'Танос', 'Правильного ответа нет'],
#         'right_answer': 1
#      }
# ]
# s = 0
# name = input('Введите ваше имя: ')
# for question in questions:
#     print(question.get('question'))
#     answer_number = 0
#     for answer in question.get('answers'):
#         answer_number += 1
#         print(answer_number, '. ', answer)
#     user_answer = int(input('Ваш ответ: '))
#     if user_answer == question.get('right_answer'):
#         print('Верно!')
#         s= s + 1
#     else:
#         print('Неверно!')
#
#
#     file = open('result.txt', 'a')
#     file.write(name + ': ' + str(s) + '\n')
#     file.close()
#
#     fileR = open('result.txt', 'r')
#     print(fileR.read())

# ФУНКЦИИ
#'Тостер'
# def summ(a):
#     # summ это просто переменная, а 'a' это тоже обычное значение
#     return a + 5
# print(summ(4))

#Калькулятор
# def calculator(a, b, operand):
#     if operand == '+':
#         result = a + b
#     elif operand == '-':
#         result = a - b
#     elif operand == '*':
#         result = a * b
#     elif operand == ':':
#         result = a / b
#     return  result
#
# num_1 = int(input('Введите число: '))
# num_2 = int(input('Введите число: '))
# op = input('Введите операцию (+/-/*/:): ')
# print(calculator(num_1, num_2, op))


# Сумма
# def summa_n(N):
#     s = 0
#     for i in range(1, N + 1):
#         s += i
#     print(f'\n Я знаю, что сумма чисел от 1 до {N} равна {s}')
# N = int(input('Введите число: '))
# summa_n(N)

# Робот на входе в отель
# def greeting():
#  for i in range(1):
#   a = input('Зайдёте? Да/Нет: ')
#  if a == 'Да':
#              print('Привет!')
#              print('Добро пожаловать!')
#  else:
#   print('Следующий.')
# print('Следующий.\n')
# greeting()