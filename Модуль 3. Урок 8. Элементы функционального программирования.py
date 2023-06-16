
#sorted и filter
goods = [
    {
        'name': 'Iphone 14',
        'brand': 'Apple',
        'price': 1200
    },
{
        'name': 'Samsung Galaxy A23',
        'brand': 'Samsung',
        'price': 600
    },
{
        'name': 'Xiaomi Mi13 Ultra',
        'brand': 'Xiaomi',
        'price': 800
    },
{
        'name': 'Iphone 11',
        'brand': 'Apple',
        'price': 400
    }
]

# def item_price(item):   #одно и то же
#     return item['price']

# print(sorted(goods, key=lambda item: item['price'])) # двоеточие работает как return #одно и то же




#map
# a = ['1','2','3','4']



# b = map(int, a) #превращает str в int
# print(list(b))



# def sss(item):
#     return item + 'sss'
#
# print(list(map(sss, a))) #дописывает sss к каждому числу

#enumerate

# for i, item in enumerate(goods): #нумерует каждую вещь
#     print(i, item)#работа со списком телефонов

#zip

names = ['Артур','Илья','Стасян','Денис']
surnames = ['Кочергин', 'Лобанов', 'Шикирюк', 'Додолин']
favorite_object = ['Математика', 'Информатика', 'ИЗО', 'Физ-ра']




for name, surname, object in zip(names, surnames, favorite_object):
    print(name, surname, object)




#задание номер 2: a.capitalize - делает 1 букву слова заглавной

#Получение предметов одной фирмы
class Item:
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand

    def __repr__(self):
        return self.brand


items_list = [
    Item(1000, 'Apple'),
    Item(1200, 'Apple'),
    Item(900, 'Samsung'),
    Item(700, 'Samsung'),
    Item(660, 'Xiaomi')
]

result = list(filter(lambda x: x.brand == 'Apple', items_list))
for x in result: print(x.price, x.brand)
print(result)


#Выведение имён с большой буквы
names_list = ['данил', 'артём', 'никита', 'влад']
result = [name.capitalize() for name in names_list]
print(result)