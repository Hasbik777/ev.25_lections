# функция высшего порядка - функция котороя в качестве аргумента принимает другую функцию

# Декоратор - функция, которая позволяет без изменения кода "обернуть" другую функцию для того чтобы расширить функционал обернутой функции

# def decorator(func):
#     print(f'Name of function: {func.__name__}')
#     print(func) # что за функция, и где она находиться
#     return func()
# def hello():
#     print('Hey stranger!')
#     print('My name is John Snow!')
# decorator(hello)    

# Pythonic way -> красота и простота кода
# Синтаксический сахар -> красота кода
# @ -> декоратор

# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         finish = time.time()
#         print(f'Время выполнения функции {func.__name__}, заняло: {finish - start}')
#     return wrapper
# @benchmark    
# def loop():
#     i = 0
#     while i <= 10000:
#         print(i)
#         i += 1
# @benchmark        
# def add():
#     ls = []
#     for i in range(0, 10001):
#         ls.append(i)                
# loop()
# add()


# def bold(func):
#     def wrapper(*args, **kwargs):
#         return '<bolt>' + func() + '</bold>'
#     return wrapper
# def div(func):
#     def wrapper(*args, **kwargs):
#         return '<div>' + func() + '</div>'
#     return wrapper
# @bold    
# @div    
# @bold   
# def str_():
#     return 'John Snow'            
# print(str_())

# ------------------------------------------------

# def capitalize(func):
#     def wrapper(name):
#         modified_name = name.title()
#         return func(modified_name)
#     return wrapper
# @capitalize        
# def say_hello(name):
#     return f'Hello, {name}!'
# @capitalize    
# def say_whatsup(name):
#     return f'What\'s up broo, {name} nigga!'    
# print(say_hello('john'))
# print(say_whatsup('lock dog'))    

# -----------------------------------------------

# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвона {func.__name__}(), \n {args}, {kwargs}')
#         original_result = func(*args, **kwargs)
#         print(f'Trace: вызвона {func.__name__}(), \nфункция вернула: {original_result}')
#         return original_result
#     return wrapper
# @trace        
# def say(name, line):
#     return f'{name}: {line}'
# @trace    
# def hello(name, last_name, country):
#     return f'Hello {name} {last_name} form {country}!'    
# say('John', '564 line')
# hello('Tirion', 'Lanister', 'Casterly Rock')

