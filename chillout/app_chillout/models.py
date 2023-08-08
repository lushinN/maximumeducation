from django.db import models





# Create your models here.

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    descrtiption = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    acution = models.BooleanField('Торг', help_text='Укажите, уместен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


 class Employee:
     def __init__(self, name, salary):
         self.name = name
         self.salary = salary

employee1 = Employee('Ivan', 200000)


