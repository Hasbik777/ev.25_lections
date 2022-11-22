# Принципы ООП:
# 1. Наследование
# 2. Инкапсуляция
# 3. Полиморфизм

# 4. Абстракция
# 5. Компазиция
# 6. Агрегация
# 7. Ассоциация
# -----------------------------------------------

# Наследование -> позволяет принимать родительские методы и атрибуты для дочернего класса

# Родительский класс
# Дочерний класс
# --------------------------------------------------------------------------------------------

# class Animal:
#     def print_info(self):
#         print('I\'m an animal!')
    
# class Croco(Animal):
#     pass

# croco = Croco()
# croco.print_info()

# ----------------------------------------

# class Animal:
#     name = None
#     golos = None
#     meal = None

#     def say(self):
#         print(f'This animal is {self.name} {self.golos}!')

#     def eat(self):
#         print(f'This animal {self.name} eat {self.meal}!') 

# class Lion(Animal):
#     name = 'Lion'
#     meal = 'meat'
#     golos = 'aarrr!'
#     griva = True

#     def print_info(self):
#         print(f'Griva {self.griva}')

# class Dog(Animal):
#     name = 'Dog'
#     meal = 'meat'
#     golos = 'bark!'

# class Koala(Animal):
#     name = 'Koala'
#     meal = 'Efkalipt'
#     golos = 'rooaar!'

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()

# simba.say()
# simba.eat()
# simba.print_info()

# julian.say()
# julian.eat()

# ----------------------------------------------------

# class Employee:
#     bonus = 1.5

#     def __init__(self, name, last_name, salary):
#         self.name = name + ' ' + last_name
#         self.salary = salary

#     def get_info(self):
#         return f'FIO: {self.name}, Salary: {self.salary}'

#     def give_increase(self):
#         self.salary = self.salary * self.bonus

# class Developer(Employee):
#     def __init__(self, name, last_name, salary, language):
#         super().__init__(name, last_name, salary)
#         self.prog_lang = language

# class Manager(Employee):
#     def __init__(self, name, last_name, salary, emps=None):
#         super().__init__(name, last_name, salary)
#         if not emps:
#             self.emps = []
#         else:
#             self.emps = emps

#     def add_emp(self, employee):
#         self.emps.append(employee)

#     def show_emps(self):
#         return [x.get_info() for x in self.emps]

        
# dev1 = Developer('John', 'Snow', 1000, 'Python')
# dev2 = Developer('Steve', 'Jobs', 3000, 'C++')
# dev3 = Developer('Lary', 'Page', 1500, 'JS')
# dev4 = Developer('Raychel', 'Cruse', 1000, 'Python')
# man1 = Manager('Ivan', 'Ivanov', 2000)
# man2 = Manager('Dastan', 'Velikiy', 4000, [dev1, dev4])

# man1.add_emp(dev2)
# man1.add_emp(dev3)
# man2.add_emp(dev2)

# print(f'Manager: {man1.get_info()}, has {man1.show_emps()}, developers.')
# print(f'Manager: {man2.get_info()}, has {man2.show_emps()}, developers.')

# man2.give_increase()
# dev2.give_increase()
# print(man2.get_info())
# print(dev2.get_info())

# -------------------------------------------------

# class Person:
#     def __init__(self, name, last_name, age):
#         print('Parent init worked')
#         self.name = name 
#         self.last_name = last_name
#         self.age = age

#     def info(self):
#         print(f'My name is {self.name} {self.last_name}, and I am {self.age} year old!')
        
# class Student(Person):
#     def __init__(self, name, last_name, age, univer):
        
#         super().__init__(name, last_name, age)
#         self.univer = univer

#     def info(self):
#         super().info()
#         print(super(), '----------')
#         print(f'I am study in {self.univer}')

# obj = Student('Kyle', 'Walker', 23, 'KGTU')
# obj.info()
                
# -------------------------------------------------

# from datetime import datetime

# time = datetime.now()
# print(time)

# --------------------------------------------------------------------------------

# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_author(self):
#         return f'Автор этой песни {self.author}'

#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'

# song = Song('Happy', 'Pharrell Williams', 2013)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

# --------------------------------------------------------------

# class Laptop:
#     def __init__(self, brand, model, description, price):
#         self.brand = brand
#         self.model = model
#         self.desc = description
#         self.price = price

#     def get_info(self):
#         return {'brand': self.brand, 'model': self.model, 'description': {self.desc}, 'price': {self.price}}

# class MacBook(Laptop):
#     def __init__(self, brand, model, description, price, year, provider):
#         super().__init__(brand, model, description, price)
#         self.year = year
#         self.provider = provider

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['provider'] = self.provider
#         return repr

# class Acer(Laptop):
#     def __init__(self, brand, model, description, price, videocard, display):
#         super().__init__(brand, model, description, price)
#         self.videocard = videocard
#         self.display = display

#     def get_info(self):
#         repr = super().get_info()
#         repr['videocard'] = self.videocard
#         repr['display'] = self.display
#         return repr

# obj1 = Laptop('Acer', 'M330', '8gb, 512 SSD', 800)
# obj2 = MacBook('Apple', 'Air', '13, 8gb, 256 SSD', 1000, 2020, 'China')
# obj3 = Acer('Acer', 'Inspire', '16gb, 1tb SSD', 1000, 'gtx geforce nvidia', '15.6 Full RGB')

# print(obj1.get_info())
# print(obj2.get_info())
# print(obj3.get_info())

# ----------------------------------------------------------------------------

# class Post:
#     def __init__(self, user):
#         self.user = user
#         self.post = []
#         self.id = 0

#     #CRUD
#     def create_post(self, title, body, image):
#         self.id += 1
#         post = dict(id=self.id, title=title, body=body, image=image)
#         self.post.append(post)
#         return {'status': 201, 'msg': 'Successfully created!'}

#     def list_post(self):
#         repr = []
#         for post in self.post:
#             repr.append({'id': post['id'], 'title': post['title'], 'image': post['image']})
#         return {'status': 200, 'msg': repr}

#     def detail_post(self, id):
#         for post in self.post:
#             if post.get('id') == id:
#                 return {'status': 200, 'msg': post}
#         return{'status': 404, 'msg': 'Not found!'}

#     def update_post(self, id, **kwargs):
#         for post in self.post:
#             if post['id'] == id:
#                 post.update(kwargs)
#                 return {'status': 206, 'msg': 'Successfull update!'}
#         return {'status': 404, 'msg': 'Not found!'}

#     def delete_post(self, id):
#         for post in self.post:
#             if post['id'] == id:
#                 try:
#                     self.post.remove(post)
#                     return {'status': 204, 'msg': 'Successfully deleted!'}
#                 except:
#                     return {'status': 500, 'msg': 'Pni svoego backa!'}    
#         return {'status': 404, 'msg': 'Not found!'}

# acc1 = Post('JamesKirk')
# print(acc1.create_post('Good news', 'I will be father soon!', 'https://foto.jpg'))
# print(acc1.create_post('na chile', 'na raslabone', 'https://foto.jpg'))
# print(acc1.create_post('Ya gulyal', 'na ulice bylo precrasno!', 'https://foto.jpg'))

# print(acc1.list_post())
# print(acc1.detail_post(2))
# print()
# print(acc1.detail_post(3))
# print(acc1.update_post(3, title='My gulyali'))
# print(acc1.detail_post(3))

# print(acc1.delete_post(2))
# print()
# print(acc1.list_post())

#  ---------------------------------------------------------------------------------

# class Bankaccount:
#     def __init__(self):
#         self.balance = 0
#     def witdraw(self, amount):
#         # if amount > self.balance:
#         #     print('Недопустимая сумма')
#         #     return
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')    
        
#     def deposit(self, amount):
#         # if amount < 0:
#         #     print('Не допустимая сумма!')
#         #     return
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')

# account = Bankaccount()
# account.deposit(1000)
# account.witdraw(500) 

