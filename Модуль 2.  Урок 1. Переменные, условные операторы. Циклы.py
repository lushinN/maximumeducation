# команда type(переменная) для определения типа переменной

# операция с // - деление без остатка, %-остаток, ** - степень

# срезы!

# проверка ошибки
# try: # Здесь что-то пытаемся делать - то есть проверяет возможную ошибку
#     num_1 = int(input())
#     num_2 = int(input())
#     oper = input()
# except ValueError: # это если ловим ошибку - то выводит принт
#     print('Такого значения я не знаю!')
# else:
#     if oper == '+':
#         print(num_1 + num_2)
#     else: print(num_1 - num_2)

# Калькулятор c функцией
# def calculator():
#     print('Укажите нужную операцию (+/-/*/:): ')
#     operation = input()
#     num_1 = input('Введите первое число:')
#     num_2 = input('Введите второе число:')
#     if operation == '+':
#       try:
#         print(int(num_1) + int(num_2))
#       except ValueError:
#         print('Я такого не знаю!')
#     elif operation == '-':
#       try:
#         print(int(num_1) - int(num_2))
#       except ValueError:
#           print('Я такого не знаю!')
#     elif operation == '*':
#       try:
#         print(int(num_1) * int(num_2))
#       except ValueError:
#           print('Я такого не знаю!')
#     elif operation == ':':
#       try:
#         print(int(num_1) / int(num_2))
#       except ValueError:
#               print('Я такого не знаю!')
#
# calculator()


# Вычислитель корней квадратног уравнения
# import math
# def calculator():
#     print('Эта программа вычилсения дискриминанта! Просто введи a,b и c! ')
#     a = int(input('Введите a:'))
#     b = int(input('Введите b:'))
#     c = int(input('Введите c:'))
#
#     D = b**2 - 4 * a * c
#     print(f'Дискриминант равен: {D}')
#     koren = math.sqrt(D)
#     if D>0:
#         print(f'x1=: {b*-1+koren/2*a}')
#         print(f'x2=: {b*-1-koren/2*a}')
#     elif D==0:
#         print(f'x=: {b*-1/2*a}')
#     else:
#         print('Нет решений')
#
# calculator()
#
#
#
#
