# OOP -> Обьектно ориентированное программирование

# Класс - это описание того, как должен выглядить обьект, то есть в классе мы описываем какими свойствами(данными) и поведениями(функциями) должен обладать обьект(экземпляр).

# Обьект -  это сущность который мы создаем от класса, у обьекта есть собственное состояние свойств(данных).

# Свойствами(атрибуты) - называют обычные переменные в классе, в которых хранятся данные оперделенного обькта.  

# Поведение - это обычные функции которые описывают поведение обьекта, функции внутри класса называют методами. 

# ---------------------------------------------------------------------------------------------------

# kirk = {'name': 'Kirk McDuck', 'age': 34, 'job': 'Captain', 'salary': 2000}
# snow = {'name': 'John Snow', 'age': 24, 'job': 'Police', 'salary': 1500}
# mccoy = {'name': 'Leonard Mccoy', 'age': 18, 'job': 'Cheif', 'salary': 1000}
# print(f'Name: {kirk["name"]}\nAge: {kirk["age"]}\nJob: {kirk["job"]}\nSalary: {kirk["salary"]}')
# print()
# print(f'Name: {snow["name"]}\nAge: {snow["age"]}\nJob: {snow["job"]}\nSalary: {snow["salary"]}')
# print()
# print(f'Name: {mccoy["name"]}\nAge: {mccoy["age"]}\nJob: {mccoy["job"]}\nSalary: {mccoy["salary"]}')

# ----------------------------------------------------------------------------------------------------

# class Human:
#     def __init__(self, first_name, last_name, age, job, salary):
#         """
#         Здесь описываются атрибуты обьекта
#         """
#         self.name = first_name +  ' ' + last_name
#         self.age = age
#         self.job = job
#         self.salary = salary

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Salary: {self.salary}'

# kirk = Human('James', 'Kirk', 34, 'Captain', 2000)
# snow = Human('John', 'Snow', 24, 'Police', 1500)
# mccoy = Human('Leonard', 'Mccoy', 30, 'Cheif', 1000)
# print(kirk.name)
# print(snow.name)
# print(mccoy.name)

# print(kirk.show_info())
# print(snow.show_info())
# print(mccoy.show_info())

# -------------------------------------------------------------------------------------------------

# class Dog:
#     # аттрибуты класса
#     age = 0
#     ears = True

#     def __init__(self, name, color) -> None:
#          """ Инициализатор, именно здесь создаются(инициализируется) атрибуты от класса"""
#          self.name = name # атрибуты обьекта(экземпляр) от класса
#          self.color = color 

# bobik = Dog('Bobik', 'brown')
# yumi = Dog(name='Yumi', color='white')
# aktosh = Dog('Aktosh', 'gray')

# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ears: {bobik.ears}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ears: {yumi.ears}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ears: {aktosh.ears}')

# bobik.age = 5
# yumi.age = 2
# aktosh.age = 12
# aktosh.ears = False

# print('After:')
# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ears: {bobik.ears}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ears: {yumi.ears}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ears: {aktosh.ears}')

# --------------------------------------------------------------------------------------------

# class Human:
#     age = 0

#     def __init__(self, name, weight, nationality) -> None:
#          self.name = name 
#          self.weight =  weight 
#          self.nation = nationality
#     def birthday(self):
#         import random
#         print(f'\nHappy birthday, {self.name}!')
#         self.age += 1
#         self.weight += random.randint(3, 7)
        
# human1 = Human('John Snow', 3.7, 'American')
# human2 = Human('Abu-Bakr', 3, 'Arabian')

# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# print('After 1 year:')
# human1.birthday()
# human2.birthday()

# print(human1.name, human1.age,human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# ----------------------------------------------------------------

"""
Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 15%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
"""

# class Salary:
#     tax = 0.10
#     def __init__(self, salary, experience) -> None:
#         self.salary = salary
#         self.exp = experience

#     def get_tax(self):
#         res = (self.salary * self.tax) * (12 * self.exp)
#         print(f'Сумма налога составила {res} сомов, за {self.exp} лет работы!')
# obj1 = Salary(35000, 13)
# obj1.get_tax()

# obj2 = Salary(150_000, 8)
# obj2.get_tax()



# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.exp = experience

#     def count_percent(self):
#         res = self.salary * self.exp * (self.percent / 100) 
#         return f'Сумма налагов составило: {res} сом, за {self.exp} месяцев!'
        

# obj = Salary(10_000, 10)
# print(obj.count_percent())








