#Вирус со скримером
# from tkinter import*
#
# window = Tk()
# window.geometry('900x300')
# window.resizable(width=False, height=False) #resizable - разрешить или запретить стягивание окна
# window.config(bg='black')
#
# text = Label(text='Ваш компьютер заражён!!!', bg='black', font=('Courier New',34), fg='red')
# text.place(x=100, y=100, width=700, height=100)
#
# count_text = Label(text = '6', fg='green', bg='black', font=('Courier New',36))
#
# def count_start():
#  if int(count_text['text']) > 0 :
#      count_text['text'] = int(count_text['text'])-1
#      count_text.place(x=250, y=25, width=400, height=100)
#      window.after(1000,count_start) #after - задержка в МИЛЛИСЕКУНДАХ!
#
#
#  else:
#   width = window.winfo_screenwidth()
#   height = window.winfo_screenheight()
#   window.geometry(str(width)+ 'x' + str(height)) #Эта часть растягивает окно на весь экран
#
#   photo = PhotoImage(file='D:\Репет\PyCharm\Работы\skelet.gif')
#   label = Label(image=photo, bg='black')
#   label.image = photo #Эти 3 строчки загружают фотку на окно
#
#   label.place(width=width, height=height, x=0, y=0)
#
# def on_close():
#     count_start()
#
# window.protocol('WM_DELETE_WINDOW', on_close) #protocol - настройки окна
#
# print(window.winfo_screenwidth())#window.winfo_screenwidth - разрешение монитора
#
# window.mainloop()

# Скам с меняющейся кнопкой
# from tkinter import*
#
# window = Tk()
# window.geometry('1300x300')
# window.resizable(width=False, height=False) #resizable - разрешить или запретить стягивание окна
# window.config(bg='yellow')
#
# text = Label(text='Вы выиграли в лотерее!!!', bg='yellow', font=('Courier New',34), fg='red')
# text.place(x=300, y=100, width=700, height=100)
#
# win_b = Button(text = 'Получить выйгрыш', font = ('Arial', 36), fg = 'red')
# win_b.place(x=0, y=200)
#
#
# def text_update():
#  global win_b
#  win_b.config(text='Чтобы забрать выйгрыш необходимо внести 1000руб.')
#
#
# def on_close():
#         text_update()
#
#
# win_b = Button(text = 'Получить выйгрыш', font = ('Arial', 36), fg = 'red', command= text_update)
# win_b.place(x=0, y=200)
#
#
# window.protocol('WM_DELETE_WINDOW', window)
#
# window.mainloop()
