#Перестрелка танков
import random
class Tank:
    def __init__(self, model, health, armor,  min_damage, max_damage):
        self.model = model
        self.health = health
        self.armor = armor
        self.damage = random.randint(min_damage,max_damage)

    def print_info(self):
       print(self.model, 'имеет', self.health, 'hp и', self.damage, 'урона')


    def health_down(self, enemy_damage):
        self.health -= enemy_damage
        print(self.model)
        print('По нам попали! У нас осталось', self.health, 'hp')

    def shot(self, enemy):
      if enemy.health <=0 or self.damage >= enemy.health:
          enemy.health = 0
          print(enemy.model, 'уничтожен')
      else:
          print()
          print(self.model)
          print('Есть пробитие! По ', enemy.model, 'нанесено', self.damage, 'hp')
          enemy.health_down(self.damage)

class SuperTank(Tank):
    def __init__(self, model, health, armor,  min_damage, max_damage, forceArmor):
        super().__init__(model, health, armor,  min_damage, max_damage) #super - унаследование
        self.forceArmor = forceArmor

    def health_down(self, enemy_damage):
        super().health_down(enemy_damage//2)


tank1 = Tank('t-34', 100, 50, 10, 60)
tank2 = Tank('Maus', 50, 10, 10, 50)
sTank = SuperTank('BABAHA', 1000,300,50,90,True)
tank1.health_down(30)

sTank.print_info()
tank1.print_info()
tank2.print_info()

tank1.shot(sTank)


#Наследование
# class A:
#     def one(self):
#         print(1)
#     def two(self):
#         print(2)
#
# class B(A):
#     def two(self):
#         print('two')
#     def three(self):
#         print(3)
#
# a = A()
# a.one()
#
# b=B()
# b.one()
# b.three()


#Игра с классами
# import random
# class User:
#     def __init__(self, nickname, health,  min_damage, max_damage):
#        self.health = health
#        self.damage = random.randint(min_damage,max_damage)
#        self.nickname = nickname
#
#
#     def hp_down(self, enemy_damage):
#         self.health -= enemy_damage
#         print(self.nickname)
#         print('У  врага осталось', self.health, 'hp')
#
#     def slash(self, enemy):
#       if enemy.health <=0 or self.damage >= enemy.health:
#           enemy.health = 0
#           print(enemy.nickname, 'уничтожен')
#       else:
#           print()
#           print(self.nickname)
#           print('Попал!',  enemy.nickname, 'получил', '-', self.damage, 'hp')
#           enemy.hp_down(self.damage)
#
# class Warrior(User):
#     def __init__(self, nickname, health,  min_damage, max_damage):
#         super().__init__(nickname, health,  min_damage, max_damage)
#
# class  Mage(User):
#     def __init__(self, nickname, health,  min_damage, max_damage):
#         super().__init__(nickname, health,  min_damage, max_damage)
#
# class  Archer(User):
#     def __init__(self, nickname, health,  min_damage, max_damage):
#         super().__init__(nickname, health,   min_damage, max_damage)
#
# player1 = Mage('qwerty', 100, 10,30)
# player2 = Warrior('quepro', 100, 10,30)
# player1.slash(player2)
#
