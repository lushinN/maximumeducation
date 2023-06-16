# Полиморфизм

#Динамическая типизация

# class Animal:
#     legs = 4
#     tail = 1
#     def voice(self):
#         print('какой-то звук')
#
# class Cat(Animal):
#     def voice(self):
#         print('мяу-мяу')
#
# class Dog(Animal):
#     def voice(self):
#         print('гав-гав')
#
# animal = Animal()
# cat = Cat()
# dog = Dog()
#
# farm_band = [animal,cat,dog]
#
# for animal in farm_band:
#     if isinstance(animal,Cat): #isinstance - проверяет принадлежность класса
#         animal.voice()
#     elif isinstance(animal, Dog):
#         animal.voice()
#     else:
#         animal.voice




#Статическая типизация

# class  Animal:
#     _legs = 4 #_ - не стоит изменять, но возможно
#     __tail = 1# __ - невозможно изменить и запринтить(только через функцию можно)
#     def voice(self):
#         print('какой-то звук')
#
#     def getter(self):
#         print(self.__tail)
#
# animal = Animal()
#
# animal._legs = 1
# print(animal._legs)
# animal.getter()

#Декоратор

def func_decorator(func):
    def inner():
        print('start')
        func()
        print('end')
    return inner

@func_decorator
def some_func():
    print('Супер важный, но базовый функционал')

some_func()

@message_handler
def bot_send_message():


# f = func_decorator(some_func)
# f()
