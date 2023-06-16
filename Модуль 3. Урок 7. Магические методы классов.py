a = 5
b = 1
c = a + b

w = 'Hello' + 'world'



#Метод __add__
# class Item:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#     def __add__(self, other):#сложение #2 #add позволяет спокойно складывать
#         if isinstance(other,Item): # isinstance проверяет класс
#           return  self.weight + other.weight
#         elif isinstance(other,int):
#           return self.weight + other#3
#
#     def __sub__(self, other): #вычитание
#         if isinstance(other,Item):
#             return self.weight - other.weight
#
#     def __mul__(self, other): #умножение
#         if isinstance(other,Item):
#             return self.weight * other.weight
#
#     def __floordiv__(self, other): #целочисленное деление
#         if isinstance(other,Item):
#             return self.weight // other.weight
#
#     def __truediv__(self, other): #деление
#         if isinstance(other, Item):
#             return self.weight / other.weight
#
#
#
#
# ingredient1 = Item('Мука', 200)
# ingredient2 = Item('Яйца', 1000)
#
# print(ingredient1 + ingredient2) #1
# print(ingredient2 - ingredient1)
# print(ingredient1 * ingredient2)
# print(ingredient2 // ingredient1)
# print(ingredient2 / ingredient1)




#Алхимия
from  tkinter import *
import  random
window = Tk()
window.geometry('600x600')

class Fire:
    image = PhotoImage(file='D:\Репет\PyCharm\Работы/free-icon-fire-9509865.png').subsample(10,10)#subsample - уменьшает картинку
    def __add__(self, other):
        if isinstance(other, Earth):
            return  Clay

class Water:
    image = PhotoImage(file='D:\Репет\PyCharm\Работы/free-icon-water-drop-4246703.png').subsample(10,10)


class Earth:
    image = PhotoImage(file='D:\Репет\PyCharm\Работы/ground.png').subsample(10,10)
    def __add__(self, other):
        if isinstance(other, Fire):
            return  Clay


class Wind:
    image = PhotoImage(file='D:\Репет\PyCharm\Работы/wind.png').subsample(10,10)

class Clay:
    image = PhotoImage(file='D:\Репет\PyCharm\Работы/free-icon-pottery-7942410.png').subsample(10, 10)



elements = [Fire(), Earth(), Water(), Wind()]

canvas = Canvas(window, width=600, height=600)
canvas.pack()

for elem in elements:
    img = canvas.create_image(random.randint(50, 550), random.randint(50, 550), image = elem.image)

def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)

    if len(images_id) > 1:
        elem1 = elements[images_id[0]-1]
        elem2 = elements[images_id[1]-1]

        new_element = elem1 + elem2

        if new_element not in elements:
         canvas.create_image(event.x, event.y, image = elem.image)
         elements.append(new_element)


    canvas.coords(images_id, event.x, event.y ) #coords - изменение координатов объектов




window.bind('<B1-Motion>', move)





window.mainloop()




# from tkinter import *
# import random
#
# window = Tk()
# window.geometry('600x600')
# window.resizable(width=False, height=False)
# window.title('ALCHEMY')
#
#
#
# class Fire:
#     image = PhotoImage(file='fire.png').subsample(1, 1) #zoom увелич а subsample уменшьшает а в них коэфициенты
#     coordx = 100
#     coordy = 100
#
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Smoke
#         elif isinstance(other, Earth):
#             return Clay
#         elif isinstance(other, Wind):
#             return Forest_fire
#
#
# class Water:
#     image = PhotoImage(file='water.png')
#     coordx = 500
#     coordy = 100
#
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Smoke
#         elif isinstance(other, Wind):
#             return Ice
#         elif isinstance(other, Earth):
#             return Grass
#
# class Earth:
#     image = PhotoImage(file='earth.png')
#     coordx = 100
#     coordy = 500
#
#     def __add__(self, other):
#         if isinstance(other, Wind):
#             return Stone
#         elif isinstance(other, Fire):
#             return Clay
#         elif isinstance(other, Water):
#             return Grass
#
#
# class Wind:
#     image = PhotoImage(file='wind.png')
#     coordx = 500
#     coordy = 500
#
#     def __add__(self, other):
#         if isinstance(other, Earth):
#             return Stone
#         elif isinstance(other, Water):
#             return Ice
#         elif isinstance(other, Fire):
#             return Forest_fire
#
# class Smoke:
#     image = PhotoImage(file='smoke.png')
#
# class Stone:
#     image = PhotoImage(file='stone.png')
#
# class Ice:
#     image = PhotoImage(file='ice.png')
#
# class Clay:
#     image = PhotoImage(file='clay.png')
#
# class Grass:
#     image = PhotoImage(file='grass.png')
#
# class Forest_fire:
#     image = PhotoImage(file='forest_fire.png')
#
#
#
# elements = [Fire(), Water(), Earth(), Wind()]
#
# canvas = Canvas(window, width=600, height=600)
# canvas.config(bg='#ebebeb')
# canvas.pack()
#
# for elem in elements:
#     img = canvas.create_image(elem.coordx, elem.coordy, image=elem.image)
#
#
#
# def move(event):
#     images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10,)
#     canvas.coords(images_id, event.x, event.y)
#     print(images_id)
#     if event.x >= 600:
#         canvas.coords(images_id, event.x - 50, event.y)
#     elif event.x <= 0:
#         canvas.coords(images_id, event.x + 50, event.y)
#     elif event.y >= 600:
#         canvas.coords(images_id, event.x, event.y - 50)
#     elif event.y <= 0:
#         canvas.coords(images_id, event.x, event.y + 50)
#
#     if len(images_id) == 2:
#         if images_id[-1] < len(elements) + 1:
#             elem1 = elements[images_id[0] - 1]
#             elem2 = elements[images_id[1] - 1]
#
#
#             try:
#                 new_element = elem1 + elem2
#             except:
#                 new_element = None
#             else:
#                 if new_element is not None:
#                     new_element = elem1 + elem2
#                     canvas.delete(images_id[0])
#                     canvas.delete(images_id[1])
#
#
#             if new_element is not None:
#                 canvas.create_image(event.x, event.y, image=new_element.image)
#                 if new_element not in elements:
#                     elements.append(new_element)
#
#         else:
#             return True
#     elif len(images_id) != 2:
#         return True
#
#
#
#
# window.bind('<B1-Motion>', move)
