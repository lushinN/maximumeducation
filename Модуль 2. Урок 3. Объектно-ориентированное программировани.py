# Холст с фигурами
# from tkinter import *
# window = Tk()
# window.geometry('800x600')
#
# canvas = Canvas(window, width=800, height=600, bg='white') #Canvas - Холст
# canvas.pack() #pack - для существования холста

# canvas.create_rectangle(10,10,30,30, fill= 'green', outline='black') #rectange для прямоугольных фигур
# canvas.create_rectangle(40,40,80,80, fill= 'yellow', outline='cyan') #первая цифра из двух - x, вторая - y
# canvas.create_rectangle(90,90,150,150,fill='red', outline='blue')

# canvas.create_polygon(10,260,60,200,110,260, fill='black', outline='') #polygon - для других фигур
# canvas.create_rectangle(20,260,100,320,fill='red', outline='blue')
#
#
# window.mainloop()



# # Игра с уроном
# class Unit: #Unit - каждый игрок
#     def __init__(self, name, health):  #__init__ - инициализация игрока, self - текущего игрока
#         self.name = name
#         self.health = health
#
#     def sayHello(self):
#         print('Hi! My nickname is', self.name)
#
#     def pistol(self, other): #other - обращение к другим
#         damage = 15
#         print(self.name, 'did pew-pew')
#         other.health = other.health - damage
#
# unit_1 = Unit('s1mple', 100)
# unit_2 = Unit('Zywoo', 88)
#
# # unit_1.sayHello()
# # unit_2.sayHello()
#
# print(unit_2.health) #Здоровье зайву до выстрела
# unit_1.pistol(unit_2) #Симпл стреляет в зайву
# print(unit_2.health) #Здоровье зайву после выстрела
#
# #unit_2.pistol()
#
# # print(unit_1.health)
# # print(unit_2.health)

# Игра в рыцарей
# import random
# class Warrior:
#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health
#
#     def attack(self, other):
#         if type(self) == type(other):
#          other.health -= 20
#         else:
#             raise TypeError #этот вид ошибки сам отыскал, очень удобен здесь
#
# warriors = [Warrior('Воин_1'),Warrior('Воин_2')]
# while True: #True идет вместе с TypeError
#  k = input('Введите 7, чтобы началась атака одного из войнов, нажмите 5 для конца месива: ')
#  if k == '7':
#      r = random.randint(0,1)
#      attacker, defender = warriors[r],warriors[r-1]
#      attacker.attack(defender)
#      print(attacker.name, 'атаковал', defender.name)
#      print('у', defender.name, 'осталось здоровья', defender.health)
#      if defender.health <= 0:
#          print(attacker.name, 'разнес 1 на 1!')
#          break
#      elif k == '5':
#          break
#      else:
#          print('Ты ввёл что то не то!')