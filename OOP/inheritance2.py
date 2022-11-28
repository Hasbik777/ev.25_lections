# Множественное наследование - это когда класс наслндуется от 2 или более классов

# class A:
#     pass

# print(A.mro())
# print(issubclass(A, object))

# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing!')

#     def ride(self):
#         print('We are ridding on the ground!')

# class Plane:
#     def play_music_at_station(self):
#         print('We started to listen music!')

#     def fly(self):
#         print('We are flying')

# class FuterAuto(Auto, Plane):
#     pass

# obj1 = FuterAuto()
# obj1.ride()
# obj1.fly()
# obj1.play_music_at_station()

# ---------------------------------------------------------------------
# MRO(Method Resolution Order) -> механизм для корректного родительских методов. Был создан для того чтобы решить проблемы ромба, которая появилась после введения класса object в пайтон

# class Zero:
#     def say(self):
#         print('Class Zero')

# class First:
#     def say(self):
#         print('Class First')

# class Second:
#     def say(self):
#         print('Class Second')

# class MyClass(First, Second):
#     def say(self):
#         super().say()

# obj = MyClass()
# obj.say()
# print(MyClass.__mro__)

# -----------------------------------------------------------
    
# class Y:
#     pass

# class X:
#     pass

# class A(X, Y):
#     pass

# class B(Y, X):
#     pass

# class MyMRO(type):
#     def mro(cls):
#         return [object, A, cls, B, X, Y]

# class C(A, B, metaclass=MyMRO):
#     pass

# obj = C()
# print(C.mro())

# ------------------------------------------------------------------
# Mixins(Миксины, Примеси)
# В каких случаях:
# 1. Вы хотите предоставить множество доп функции (методов) для класса,
# 2. Вы хотите использовать одну конкретную функцию во множестве разных классов

# class Machanisms:
#     def start_engine(self):
#         print('Started engine!')

# class MusicPlayerMixin:
#     def play_music(self):
#         print('Music is playing!')

# class Auto(Machanisms, MusicPlayerMixin):
#     pass

# class Boat(Machanisms, MusicPlayerMixin):
#     pass

# class WashingMachine(Machanisms):
#     pass

# obj_auto = Auto()
# obj_boat = Boat()
# obj_wash = WashingMachine()

# obj_auto.start_engine()
# obj_auto.play_music()
# obj_boat.start_engine()
# obj_boat.play_music()
# obj_wash.start_engine()

# -------------------------------------------------------------

# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         self.km = km
        # return f'Такси {self.name}, стоимость поездки: {self.cost} сом'

# class Namba(Taxi):
#     def __init__(self, name, cost):
#         self.name = name
#         self.cost = cost

#     def get_total_cost(self):
#         self.km = 10
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом'

# class Yandex(Taxi):
#     def __init__(self, name, cost):
#         self.name = name
#         self.cost = cost
        

#     def get_total_cost(self):
#         self.km = 6
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом'

# class Jorgo(Taxi):
#     def __init__(self, name, cost):
#         self.name = name
#         self.cost = cost

#     def get_total_cost(self):
#         self.km = 14
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом'
    
# taxi1 = Namba('Namba', 179)
# taxi2 = Yandex('Yandex', 127)
# taxi3 = Jorgo('Jorgo', 238)

# print(taxi1.get_total_cost())
# print(taxi2.get_total_cost())
# print(taxi3.get_total_cost())

# ---------------------------------------------------------------------------

# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone =  phone

#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}'

# contact = Phone('John', 'Snow', +996707707707)
# print(contact.get_info())        

# ------------------------------------------------------------------------

# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.exp = experience

#     def count_percent(self):
#         res = self.salary * self.exp * (self.percent / 100) 
#         return res
# obj = Salary(10_000, 10)
# print(obj.count_percent())

# ---------------------------------------------------------------------

# import datetime
# class Nobel:
#     time = datetime.datetime.now().year
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         res = self.time - self.year
#         return f'выиграл {res} лет назад'

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())
