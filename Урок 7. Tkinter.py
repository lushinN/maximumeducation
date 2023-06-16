#Опросник в окне
# from tkinter import* #эта команда для того, чтобы не повторять tkinter несколько раз
#
# window = Tk() #window - переменная, Tk обязательно с большой
# window.geometry('700x500') #700x500 это разрешение создаваемого окна
# window.title('Самый сложный тест по вселенной Марвел') #title - для озаглавления окна
#
# facts = [
#     {'text': 'Человеческое имя Халка - Брюс Беннет', 'right:': 1},
#     {'text': 'ХАХАХААХАХАХ', 'right:': 0},
#     {'text': 'ЛОЛОЛОЛОЛОЛОЛОЛ', 'right:': 1},
#     {'text': 'ЛАЛАЛАЛАЛАЛ', 'right:': 0},
# ]
#
# cur_q = 0
# points = 0
# def check():
#     global cur_q, points #global - это возможность обратиться к функции
#     answer = var.get()
#     if bool(answer) == facts[cur_q]['right:']:
#         points += 1
#         if cur_q < len(facts)-1:
#             cur_q += 1
#             fact['text'] = facts[cur_q]['text']
#         else:
#             points_label = Label(text = 'Вы набрали' + str(points) + 'очка',
#                                  font = ('Arial, 34'), fg = 'red', bg = 'white')
#
#
# label_title = Label(text = 'Тестирование по вселенной Марвел', font=('Arial, 24'),fg='white', bg = 'red') #label_title - переменная, Label-Текст в файле, fg - цвет текста, bg - фон текста
# label_title.place(width=700, height=50, x=0, y=0) #place - место текста в файле, все значения в пикселях, width - ширина текста, height - высота текста, x и y - это смещение текста
#
# fact = Message(text = facts[cur_q]['text'], font=('Arial', 14), #Message - как и Label
#                width=680, borderwidth=0) #borderwidth - ширина обводки сообщения
# fact.place(x = 10, y = 70)
#
# var = IntVar()
# true = Radiobutton(text = 'Верно', variable=var, value = 1) # value - значение выполнения, varibale - запишет значения value в переменную var
# true.place (x=10, y = 120)
#
# false = Radiobutton(text = 'Ложь', variable=var, value = 0)
# false.place (x=10, y = 170)
#
# b = Button(text = 'Ответить', font = ('Arial', 24), fg = 'black', command=check)
# b.place(x = 200, y = 130)
#
# window.mainloop() #mainloop - чтобы окно не закрылось сразу


# Кликер
# from tkinter import *
# import random
#
# window = Tk()
# window.geometry('700x500')
# window.title('Кликер')
#
#
# points = 0
#
# def check():
#     global points
#     b.place(x=random.randint(1,550),y=random.randint(1,350))
#     points +=1
#     label['text'] = points
#
#
#
# b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check)
# b.place(x=200,y=130)
# label = Label(text = points, font=('Arial',15), fg='black')
# label.place(x=10,y=10)
#
# window.mainloop()



# Исправленная первая программа
# from tkinter import *
#
# window = Tk()
# window.geometry('700x500')
# window.title('Самый сложный тест по вселенной Marvel')
#
# facts = [
#     {'text': 'Человеческое имя Халка - Брюс Беннет', 'right': 1},
#     {'text': 'Уолт Дисней является создателем вселенной Marvel', 'right': 0},
#     {'text': 'До появления костюма супергероя, человек муравей занимался воровством ', 'right': 1},
#     {'text': 'Выдуманный город Дженоша является родиной Черной пантеры', 'right': 0}
# ]
# cur_q = 0
# points = 0
#
#
# def check():
#     global cur_q, points
#     answer = var.get()
#     if bool(answer) == facts[cur_q]['right']:
#         points += 1
#     if cur_q < len(facts) - 1:
#         cur_q += 1
#         fact['text'] = facts[cur_q]['text']
#     else:
#
#         points_label = Label(text='Вы набрали ' + str(points) + ' очка',
#                              font=('Arial', 34), fg='red', bg='white')
#         points_label.place(x=0, y=0, width=700, height=250)
#
#
# label_title = Label(text='Тестирование по вселенной Marvel',
#                     font=('Arial', 24), fg='white', bg='red')
# label_title.place(width=700, height=50, x=0, y=0)
#
# fact = Message(text=facts[cur_q]['text'], font=('Arial', 14),
#                width=680, borderwidth=0)
# fact.configure(justify=CENTER)
# fact.place(x=10, y=70)
#
# var = IntVar()
# true = Radiobutton(text="Ложь", variable=var, value=0)
# true.place(x=10, y=120)
#
# false = Radiobutton(text="Правда", variable=var, value=1)
# false.place(x=10, y=170)
#
# b = Button(text='Ответить', font=('Arial', 24),
#            fg='black', command=check)
# b.place(x=200, y=130)
#
# window.mainloop()



# При достижении 20 очков, меняет цвет
# from tkinter import *
# import random
# import time
#
# window = Tk()
# window.geometry('700x500')
# window.title('Кликер')
#
#
# points = 0
# b_colour = 'red'
#
# def check():
#     global points
#     b.place(x=random.randint(1,550),y=random.randint(1,350))
#     points +=1
#     label['text'] = points
#     if points == 20:
#         b['bg'] == b_colour
#
#
#
#
# b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check)
# b.place(x=200,y=130)
# label = Label(text = points, font=('Arial',15), fg='black')
# label.place(x=10,y=10)
#
# window.mainloop()


# При достижении 20 очков, программа 'зависает' на 2 секунды
# from tkinter import *
# import random
# import time
#
# window = Tk()
# window.geometry('700x500')
# window.title('Кликер')
#
#
# points = 0
#
# def check():
#     global points
#     b.place(x=random.randint(1,550),y=random.randint(1,350))
#     points +=1
#     label['text'] = points
#     if points == 20:
#         time.sleep(2)
#
#
# b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check)
# b.place(x=200,y=130)
# label = Label(text = points, font=('Arial',15), fg='black')
# label.place(x=10,y=10)
#
# window.mainloop()
#
