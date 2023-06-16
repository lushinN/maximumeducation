#Структура while
# a = 0
# s = 0
# while a != -1: #пока 'a' не равно -1, выполняется цикл
#  s += a
#  a = int(input())
# print(s)

#Рекомендации мероприятий
# import requests
# from bs4 import BeautifulSoup
# import random
#
# def events():
#  response = requests.get('https://kudago.com/msk/festival/')
#  response = response.content
#  html = BeautifulSoup(response, 'html.parser')
#  fests = html.find_all(class_ = 'post-title')
#  fest = random.choice(fests)
#  print(fest.text)
#  print(fest.a.attrs['href'])
#
# def facts():
#  response = requests.get('https://kudago.com/msk/facts/')
#  response = response.content
#  html = BeautifulSoup(response, 'html.parser')
#  fests = html.find_all(class_='post-title')
#  fest = random.choice(fests)
#  print(fest.text)
#  print(fest.a.attrs['href'])
#
# def conserts():
#  response = requests.get('https://kudago.com/msk/conserts/')
#  response = response.content
#  html = BeautifulSoup(response, 'html.parser')
#  fests = html.find_all(class_ = 'post-title')
#  fest = random.choice(fests)
#  print(fest.text)
#  print(fest.a.attrs['href'])
#
# user_wish = ''
#
# while user_wish != 'хватит':
#     user_wish = input('Чем бы вы хотели заняться? ').lower()#lower - будет все буквы маленькими делать
# if user_wish == 'факт':
#  facts()
# elif user_wish == 'концерт':
#   conserts()
# elif user_wish == 'фестиваль':
#   events()
# else:
#      print('Может вам остаться дома?')


#Создание PDF файла с картинкой
# from fpdf import  FPDF
#
#
# pdf = FPDF('P', 'cm', (10, 20)) #pdf-переменная
# pdf.add_page()
#
# pdf.add_font('courier', '', 'C:\WINDOWS\FONTS\COUR.ttf', uni=True)
#
# pdf.set_text_color(0,255,0) #red green blue
# pdf.set_fill_color(150,50,168)
# pdf.set_draw_color(0,0,255)
#
# pdf.set_font('courier', size=25)
# pdf.cell(8, 3, txt='Скоро новый год!', align='C', fill=True, border=1)  #fill-заливка
#
# pdf.image('', h=0, w=10, x=0, y=5) #в ковычках картинка jpeg,jpg,png
#
# pdf.output('test_fpdf.pdf')

# Проверка пароля при входе
# user_password = int(input('Введите пароль: '))
# while user_password != 235:
#  print('Неверно!')
#  user_password = int(input('Введите пароль повторно: '))
# print('Верно! Вход в систему...')
