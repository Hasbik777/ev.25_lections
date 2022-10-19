# def sum_of_args(a, b, c, d): # параметры
#     return a + b + c + d

# result = sum_of_args(1, 2, 3, 4)
# print(result)

# ---------------------------------------------
# Дефолтные параметры(default params)

# def print_hello(name='Guest'):
#     print(f'Welcome {name}')
# print_hello('John')


# def introduce(name, last_name, work=None):
#     print(f'The Users name is {name}')
#     print(f'The Users last_name is {last_name}')
#     if work:
#         print(f'The Users work is {work}')
# introduce('John', 'Snow')
# print()
# introduce('Larry', 'Page', 'Police officer')

# ---------------------------------------------------
# Позиционные и именнованые аргументы

# def printParams(a=None, b=None, c=None):
#     print(a, 'is stored in a')
#     print(b, 'is stored in b')
#     print(c, 'is stored in c')
# printParams(1, 2, 3)
# printParams(b=2, a=1, c=3)

# ------------------------------------------
# Оператор *

# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)
# ------------------------------------------
# *args, **kwargs в функциях

# args = arguments(Позиционные аргуметны)
# kwards = keyword arguments(Именнованные аргументы)

# def printScores(student, *args):
#     print(f'Student name: {student}!')
#     # print(args)
#     # print(type(args))
#     for x in args:
#         print(f'Score: {x}')
# printScores('John', 90, 100, 85, 62, 75)


# def print_pet_names(owner, **pets):
#     print('Owner name:', owner)
#     # print(pets)
#     # print(type(pets))
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:    
#             print(f'{pet}: {name}')

# print_pet_names('John Snow', wolf='Ghost', dog='Rex', fish=['Nemo', 'Dori', 'Alex'], turtle='Mbappe')


# def get_some_data(a, b, *args, **kwargs):
#     print('Параметры:', a, b)
#     print('Arguments:', args)
#     print('Kwards:', kwargs)
#     print(args[0])
#     print(args[-1])
#     print(kwargs.keys())
# get_some_data(1,2,3,4,5,6,7,8,9, lang='Python', name='John Snow', car='BmW 7 series')    

# ------------------------------------------------------------------------------------------

# def generate_random_string(len):
#     import string as s
#     import random
#     random_str = ''.join(
#         random.choice(s.ascii_letters + s.digits + s.punctuation) for i in range(0, len)
#     )
#     return random_str
# print(generate_random_string(50))

# ---------------------------------------------------------------------------------------------

# def add(a, b): return a + b
# def subtract(a, b): return a - b
# def multiply(a, b): return a * b
# def divide(a, b):
#     try:
#         return a // b
#     except ZeroDivisionError:
#         return 'На ноль делить нельзя!'    
# def calc(num1, num2):
#     operator = input('Введите оператор(+,-,*,/): ')
#     if operator == '+': return add(num1, num2)
#     elif operator == '-': return subtract(num1, num2)
#     elif operator == '*': return multiply(num1, num2)
#     elif operator == '/': return divide(num1, num2)
#     else: return 'Вы ввели неверный оператор!'
# def main():
#     try:
#         num1 = float(input('Введите первое число: '))
#         num2 = float(input('Введите второе числол: '))
#     except ValueError:
#         print('Вы ввели некоректные данные!')
#         main()
#     while True:    
#         result = calc(num1, num2)
#         if type(result) == str:
#             print(f'Error: {result}')
#         else:
#             if result > 1 and result != 0 and result % round(result) == 0:
#                 print(f'Result: {round(result)}')
#                 break
#             elif result == 0:
#                 print(f'Result: {0}')
#                 break
#             print(f'Result: {round(result, 2)}')
#             break
#     question = input('Хотите продолжить?(Yes/No): ')
#     if question.lower().strip() == 'yes':
#         main()
#     else:
#         print('Спасибо за использование нашего калькулятора! Пока пидор!')     
# main()






