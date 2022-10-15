# Обработка исключений
# Операторы try.....except
# Ошибки Errors -> связаны с кодом:
#     SyntaxError
#     IdentationError
#     TabError
# и т.д
# Исключения Exceptions -> связаны с неправильными данными, которые передаются в код.
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException - прородитель исключений
# num = int(input('Enter the number '))
# print(num)
# print('очень важная строчка кода!')

# try:
#     num = int(input('Enter the number: '))
#     print(num)
#     num2 = int(input('Enter the number2: '))
#     print(num2)
#     print(num/num2)
# except:
#     print('неправильные данные!')    
# print('очень важная строчка кода!')

## try ... except

# try:
#     <body try>
# except:
#     <body except> сработает только если ошибка в try
# <else:>
#     <body else> сработает если в операторе try нет ошибки
# <finally:>
#     <body finally> сработает в любом случае

# try:
#     num1 = int(input('Enter the number: '))
# except:
#     print('Invalid values!')    
# else:
#     print(num1)
#     print(num1 + 5)
# finally:
#     print('Код закончился!')

# -------------------------------------------------
# отображение ошибки

# 1. import sys

# list_ = [1,2,3,4,5]
# index = int(input('Enter the index: '))
# try:
#     res = list_[index]
#     print(res)
# except:
#     import sys
#     print(f'Oops, we catched {sys.exc_info()[0]} error!')

# 2. Exception as e / (error)

# ls = [1,2,3,4,5]
# while True:
#     try:
#        index = int(input('Enter the index: '))
#        print(ls[index])
#     except Exception as e:
#         print(f'Oops we catched {e.__class__} error!')


# try:
#     num1 = int(input('Vvedite  chislo1: '))
#     print(num1/0)
# except ValueError:
#     print('Invalid Values')
# except ZeroDivisionError:
#     print('Divide by 0!')


# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except ValueError:
#     print('Ivalid symbols!')
# else:
#     print(result)
# finally:
#     print('The End')            
 
# -------------------------------------------------------------
# from string import digits
# flag = True
# symbols = digits + '-' + '.'
# while flag:
#     num1 = input('Vvedite pervoe chislo: ')
#     num2 = input('Vvedite vtoroe chislo: ')
#     try:    
#        num1 = float(num1) if '.' in num1 else int(num1)
#        num2 = float(num2) if '.' in num2 else int(num2)
#     except ValueError:
#         print('Вы ввели неправильное число!')
#         continue
#     operator = input('Vvedite operator(+, -, *, /): ')
#     if operator == '+':
#          print(f'Результат: {num1 + num2}')
#     elif operator == '-':
#         print(f'Резельтат: {round(num1 - num2, 2)}')   
#     elif operator == '*':
#         print(f'Резельтат: {num1 * num2}')  
#     elif operator == '/':
#         if num2 == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(f'Резельтат: {num1 / num2}')    
#     else:
#         print('Вы ввели неправильный оператор!')

#     choice = input('Хотите остановить(yes): ')
#     if choice.lower() == 'yes':
#         flag = False
#         print('Пока!')
# -----------------------------------------------------------------

