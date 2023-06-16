# my_list = [x for x in range(1,1_000_000)]
# print(my_list)

#Генератор
# my_list_2 = (x for x in range(1,1_000_000)) #получим место в памяти - класс генератор
# print(my_list_2)
# print(next(my_list_2)) #проход по генератору, next выводит следующее число

# for i in my_list_2:
#     print(i)

# squares = (n** 2 for n in range(1_000_001))#1
# for square in squares:
#     print(square)
#
# def squares(length):#2
#     for n in range(length):
#         yield n ** 2
# for square in squares(1_000_001):
#     print(square)


# def lazy_func():
#     for item in range(1,11):#2 #7
#         print('до', item)#3
#         yield item #отдал item - заморозка
#         print('после', item)#6
#
# for i in lazy_func():#1 #5
#     print(i)#4




#WITH
import contextlib #библиотека для создания контекстных менеджеров через декоратор или наследования
f = open('churka.txt','w')
f.write('Hello world!')
f.close() #чтобы не возникала ошибка

with open('churka.txt','w') as f:
    f.write('Hello world!')
    #после выхода из файла автоматически выполнится f.close()