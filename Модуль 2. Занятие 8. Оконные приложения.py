#Переводчик валюты Центробанка с курсами вают
from tkinter import*
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='

def getCourse(id):
    response = requests.get(url)
    xml = BeautifulSoup(response.content, 'html.parser')
    valute = xml.find('valute', {'id': id})
    return  valute.value.text

usd = getCourse('R01235')

window = Tk()
window.geometry('410x400')
window.title('Банк MAXIMUM')

title = Label(window, text = 'Курс валют\n Maximim Банк', bg = 'orange', font ='Arial 22' )
title.place(y=40, x=170)

img_logo = PhotoImage(file='банк.png')
logo = Label(window, image = img_logo)
logo.place(x=0,y=0)

today = datetime.today()
today = today.strftime('%d.%m.%y')
date_info = Label(window, text = 'Курс на ' +  today, font='Arial 14', bg='brown' )
date_info.place(y=160,x=120)

usd_label = Label(window,text = '$' +  getCourse('R01235'), font='Arial 18', bg='orange' )
usd_label.place(y=200,x=25)

eur_label = Label(window,text = '€' +  getCourse('R01239'), font='Arial 18', bg='orange' )
eur_label.place(y=200,x=260)

cny_label = Label(window,text = '¥' +  getCourse('R01375'), font='Arial 18', bg='orange' )
cny_label.place(y=200,x=140)

def converte():
    res = int(input_value.get()) * float(getCourse('R01235').replace(',', '.'))
    result['text'] = res



input_value = Entry(window, width=10, fg='orange')
input_value.place(x=30, y=310)

btn = Button(text = 'Конвертировать!', bg='#555', font='Arial 12', command=converte)
btn.place(x=120,y=305)


result = Label(window,text = 'Введите\n сумму', font = 'Arial 12', bg='brown')
result.place(x=280, y=300)





window.resizable(width=False, height=False)
window.mainloop()