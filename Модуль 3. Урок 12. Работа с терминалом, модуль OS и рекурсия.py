#в терминале cmd
#dir - вывести все директории
#dir /b - выводит только названияъ
#dir /b /on - вывести имена в алфавитном порядке
#dir /b /on > names.txt - всё сохранить в names.txt
#dir type names.txt - вывести всё из names.txt
#mkdir test - создание папки в терминале
#cd test - переход в директорию test
#cd .. - возврат в прошлую директорию
#del namex.txt - удалить файл names.txt
#rmdir /s test- удалить директорию test(/s - для тотального удаления)



#Рекурсия - вызов функции внутри самой себя
# def recurs(count):
#     print(count)
#     if count == 5:
#         return
#     recurs(count+1)
#     print(count)
#
# recurs(0)


import os

current_path = os.path.abspath(__file__)
print(current_path)

parent_path = os.path.join(current_path, '..')#возврат по директории назад
print(parent_path)
# print(os.listdir(parent_path))-вывести все файлы в директории

def get_all_files(path):
    for i_name in os.listdir(path):
        new_path = os.path.join(path,i_name)
        if os.path.isdir(new_path): #idsir - проверка на существование пути к директории
            print('Папка', i_name)
            get_all_files(new_path)#переборка папок директорий с разветвлениями
        else:
            print('-', i_name)

get_all_files(parent_path)