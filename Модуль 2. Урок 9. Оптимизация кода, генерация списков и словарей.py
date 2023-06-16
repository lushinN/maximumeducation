#Все кратные 5 элементы от 0 до 99
div_5_list = []
for x in range(100):
    if x % 5 == 0:
        div_5_list.append(x)
print(div_5_list)

div_5_list = [x**3 if x>50 else x for x in range(100) if x % 5 == 0]
print(div_5_list)

list = [x for x in range(251) if x % 30 == 0 or x % 31 == 0]
print(list)

#Генератор ключей
# some_dict = {'red': 3,}

# words = ['red', 'orange', 'green', 'purple']
# some_dict = {x: len(x) for x in words}
# print(some_dict)

#Коорды параболы
# def y(x):
#     return x**2 + 1
# some_list=[2313,6456,123,7567]
# some_dict = {x: y(x) for x in some_list}
# print(some_dict)

#Кортежи-tuple

# some_tuple = (1,2,3,4)
# print(some_tuple)

# some_dict = {(1,2,3): 'value'}
# print(some_dict)

#Превращение кортежа в список и обратно
# some_tuple = (1,2,3,4)
# print(some_tuple)
# some_list = list(some_tuple)
# print(some_list)
# some_list.append(15)
# print(some_list)
# some_tuple = tuple(some_list)
# print(some_tuple)

# some_tuple = tuple(x for x in range(100))
# print(some_tuple)

#*args *kwargs
# def func(a,b,*args, **kwargs):
#     print(a+b)
#     print(args)#*args - забирает на себя числа, которые не забрали на себя переменные
#     print(kwargs['one'])#**kwargs - принимает только именованные значения
#
# func(2,3,5, one=1,two=2)
