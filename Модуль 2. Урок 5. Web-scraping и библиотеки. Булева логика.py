# Получение некоторых значений(персонажей, планет)
import requests

url = 'https://swapi.dev/api/'

response = requests.get(url) #Подключаемся к API

response = response.json() #Вытаскиваем JSON объект по адресу

peopleApi = response['people'] #Достаем персонажей
planetsApi = response['planets']

# responsePeople = requests.get(peopleApi).json() #/1 - это определенный герой, добавляется к ссылке
# print(responsePeople)

def check_people(url):
 for i in range(1,6):
     response = requests.get(url + '/' + str(i)).json()
     if len(response['starships']) >= 1:
       print(response['name'], response['starships'])

#
# def check_planets(url):
#     for i in range(1, 6):
#         response = requests.get(url +'/' + str(i)).json()
#         print(response['name'], response['diameter'])



# check_planets(planetsApi)
check_people(peopleApi)