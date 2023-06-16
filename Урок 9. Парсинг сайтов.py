#Инфа по фактам
# import requests
# from bs4 import BeautifulSoup
# import random
#
# response = requests.get('https://i-fakt.ru/') #это подключение к сайту, если выводится 200, то подключение успешно
# response = response.content #content - структура данного сайта
# html = BeautifulSoup(response, 'html.parser') #html.parser - превращает response в html вид
# facts = html.find_all(class_ = 'p-2 clearfix') #find_all - достанет все значения равные 'p-2 clearfix'
# # print(facts[0]) #здесь мы достали код 1-го факта
# fact = random.choice(facts)
# print(fact.text)
# # print(facts[0].text) #здесь мы достали текст первого факта
# # print(facts[0].a.attrs) #здесь мы получим атрибуты в части 'a'
# print(facts[0].a.attrs['href']) #получим ссылку



# Инфа о тексте сайта
# import requests
# from bs4 import BeautifulSoup
# import random
#
# response = requests.get('https://kudago.com/msk/festival/')
# response = response.content
# html = BeautifulSoup(response, 'html.parser')
# fests = html.find_all(class_ = 'post-title')
# fest = random.choice(fests)
# print(fest.text)
# print(fest.a.attrs['href'])


# Нахождение пути к 'h3'
# import requests
# from bs4 import BeautifulSoup
#
#
# response = requests.get('http://www.columbia.edu/~fdc/sample.html')
# response = response.content
# html = BeautifulSoup(response, 'html.parser')
# fests = [h3.text for h3 in html.find_all('h3')]
# print(fests)


# Извлечение дальшейшей инфы
# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
# response = response.content
# html = BeautifulSoup(response, 'html.parser')
#
# info = html.select_one("div.ecomerce-items-ajax")['data-items']
# print(info)