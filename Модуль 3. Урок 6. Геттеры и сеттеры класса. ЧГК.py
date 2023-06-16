# class Year:
#     def __init__(self):
#         self.__days = 365
# # -----------------------------------------
#         self.__property = 2
#
#     def get_days(self):
#      return self.__days
#
#     def set_days(self,days):
#         if days == 365 or days == 366:
#           self.__days = days
#         else:
#             raise Exception('Некорректное значение!')
# # ---------------------------------------------
#     def get_property(self):
#      return self.__property
#
#     def set_property(self, property):
#         if property == 2 or property == 3:
#           self.__property = property
#         else:
#             raise Exception('Попробуй заново!')
#
# chosen = Year()
# chosen.set_property(3)
# print(chosen.get_property())
# # ----------------------------------------
# year1 = Year()
# year1.set_days(366) #с set будет проверка через функцию
# print(year1.get_days())
#
#
#



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
    # @property #это getter
#     def age(self):
#      return self.__age
#     def name(self):
#         return self.__age
#
#
#     @name.setter
#     def name(self,name):
#         self.__name = name
#
#     @age.setter #age - то что мы хотим поменять #это setter !getter без setter не существует!
#     def age(self,age):
#      if age >= 0:
#        self.__age = age
#      else:
#        raise Exception('Дозревай молодой!')
#
#
#
#
#
# person = Person('Иван', 25)
#
#
# person.age = -5
# print(person.age)
