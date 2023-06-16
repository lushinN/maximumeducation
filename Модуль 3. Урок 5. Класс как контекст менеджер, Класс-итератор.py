# #Создание файла и запись в него инфы
# with open('file.txt', 'w') as f:
#     f.write('123')
#     f.close #ОБЯЗАТЕЛЬНО!
import random
import time


#Работа WITH №1
# class Context:
#     def __enter__(self):
#       print('start')
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#
#
# with Context():
#     print('Какой-то обёрнутый код')
#
# print('А это уже после менеджера')


#Работа WITH №2
# class RunningCodeJudge:
#     def __init__(self):
#         self.start = None
#
#
#     def __enter__(self):
#         print('start')
#         self.start = time.time()
#
#
#     def __exit__(self, exc_type, exc_val, exc_tb): #с помощью этих атрибутов можно понять ошибку
#         t = time.time()
#         print(f'Время выполнения кода {t - self.start} секунд')
#         print('exit')
#
#         if exc_type is TypeError: #is то же самое, что и ==
#             return True
#
#
# with RunningCodeJudge():
#     my_list = [x for x in range(1, 100_000_000)]
#     my_list -= 's' #здесь ошибка, но код все равно сработает


#Итерация и итератор
# my_list = [1,2,3,4,5]
#
# list_iterator = iter(my_list)
#
# print(next(list_iterator)) #next - перебирает следующий элемент после начала



class RandomIter:
    def __init__(self, limit):
        self.limit = limit
        self.__reload = limit

    def __iter__(self):   #обнуление итерации
        self.limit = self.__reload
        return self



    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        self.limit -= 1
        return random.randint(0,100)


rand_iter = RandomIter(5)
print(next(rand_iter))
print(next(rand_iter))
print(next(rand_iter))
print(next(rand_iter))
print(next(rand_iter))

iter(rand_iter) #начало новой итерации
print(next(rand_iter))
print(next(rand_iter))
for rand_int in rand_iter:
    print(rand_int)

#Бесконечный итератор
int() #int без значения возвращает 0
a = iter(int, 1)
next(a)
next(a)
next(a)
for i in a:
    print(a)
