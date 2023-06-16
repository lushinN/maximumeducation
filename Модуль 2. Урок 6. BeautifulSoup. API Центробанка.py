import requests
from bs4 import BeautifulSoup

url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/'


def getCourse(id_1, year):
    response = requests.get(url)
    xml = BeautifulSoup(response.content, 'html.parser')  #BeautifulSoup - разбивает на части
    valute = xml.find('valute', {'id' : id_1})
    return valute.value.text

year = input('Введите год: ')
print(getCourse('R01239', 2010))

#Перевод тенге в рубли
# 1)Находими кол-во рублей: кол-во долларов * курс доллара
# 2)Находим кол-во тенге: кол-во рублей / курс тенге

def convert(from_valute, to_valute, value): #передаём в функию: из какой валюты, в какую валюту, сколько валюты
 rub = from_valute.course * value
 valute = rub / to_valute.course
 return valute


dict = {
    'EUR': 'R01239',
    'KZT': 'R01335',
    'USD': 'R01235'
}

convert(dict['EUR'], dict['KZT'], 25)




# array = xml.find_all('valute')

# print(array)
# print(array[0])
# print(array[0].name)
# print(array[0].name.text)

# for i in array:
#     print(i.charcode.text, i.value.text)