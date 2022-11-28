# magic methods (магические методы)
# dunder methods (double underscore) -> init
# служебные методы


# res = 5 + 5 # add
# print(res)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))

# Магические методы сравнения:

# __eq__(self, other) -> 5 == 8

# __ne__(self, other) -> !=

# __lt__(self, other) -> <

# __gt__(self, other) -> >

# __le__(self, other) -> <=

# __ge__(self, other) -> >=

# print('15' > 'Abc')

# class Word(str):
#     def __new__(cls, obj):
#         # print(cls, '!!!!!!!')
#         # print(object, '--------')
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)

#     def __gt__(self, other: str) -> bool:
#         print('gt сработал')
#         print(self, '!!!')
#         print(other, 'xxxxxx')
#         return 'John Snow'

#     def __le__(self, other: str) -> bool:
#         return len(self) <= len(other)

# obj = Word('   He l lo     ')
# obj1 = Word('    Salam    ')
# print(obj1 > obj)
# print(obj <= obj1)
# print(obj == obj1)
# print(obj, len(obj))
# print(obj1, len(obj1))

# --------------------------------------------------------------
# Конструктор -> __new__
# Инициализатор -> __init__

# class Conventer(float):
#     def __new__(cls, x):
#         print('new сработал')
#         print(cls)
#         if x < 50:
#             raise ValueError('x меньше 50!') 
#         return super().__new__(cls, x)

#     def __init__(self, x):
#         print('init сработал')
#         print(self)
#         self.number = x

# obj = Conventer(51)
# print(obj.number)

# ------------------------------------------------
# Дандер метода для строкового отображения обьектов
# __str__
# __repr__

# class Base:
#     def __init__(self, stroka) -> None:
#         self.string = stroka

#     def print_john(self):
#         print('John Snow')

#     def __str__(self) -> str:
#         return f'Обьект: {self.string}'

#     def __repr__(self) -> str:
#         return f'Base("Example")'

# obj = Base('Jasy')
# print(obj)
# print(repr(obj))
# obj2 = eval(repr(obj))
# print(obj2, '!!!!!!!')
# obj.print_john()

# ----------------------------------------------------------------

# + - / * // % **

# + -> __add__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __div__
# % -> __mod__
# ** -> __pow__

# class Cifra(int):
#     def __new__(cls, number):
#         if not 0 < number < 100:
#             raise ValueError('Enter the numbers in range 0-100!')
#         instance = super().__new__(cls, number)
#         return instance

#     def __init__(self, number) -> None:
#         self.number = number

#     def __add__(self, other: int) -> int:
#         print('add вызван')
#         print(f'Result: {self} + {other} = {self.number + other.number}')

# value1 = Cifra(17)
# value2 = Cifra(56)
# value1 + value2

# -----------------------------------------------------------------------------

# class User:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __call__(self):
#         print(f'User object: {self.name}')

# user1 = User('Jasy Lili')
# user2 = User('Sherman Mclaren') 
# print(callable(user1))
# user1()
# user2()
# ----------------------------------------------------------
# from datetime import datetime
# print(datetime.today().strftime('%H:%M:%S'))
# print(datetime.now().time())
# ------------------------------------------------------------

# class LogSetFile:
#     def __init__(self, file) -> None:
#         self.file = file
#         self.number = 0

#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             from datetime import datetime
#             self.number += 1
#             with open(self.file, 'a') as file:
#                 file.write(f'{self.number} Func name: {func.__name__}, Called time {datetime.now().time()}\n')
#             return func(*args, **kwargs)
#         return wrapper

# test = LogSetFile('log.txt')

# @test
# def start_test():
#     pass

# @test
# def hello():
#     pass

# @test
# def world():
#     pass

# start_test()
# hello()
# world()
# start_test()

# --------------------------------------------------------

# class MyList(list):
#     def __init__(self, ls):
#         self.ls = ls

#     def __getitem__(self, index):
#         if index == 0:
#             print('Invalid index')
#         elif index < 0:
#             print(self.ls[index])
#         else:
#             print(self.ls[index - 1])

# x = MyList([1,2,3,4,5])
# x[1]
# x[4]
# x[2]
# x[-1]
# x[0]
