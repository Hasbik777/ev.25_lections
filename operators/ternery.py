# sentence = input('Введите предложения: ')

# if sentence[-1] == '?':
#     print('Предложение вопросительное')
# else:
#     print('Обычное предложение') 

# sentence = input('Введите предложения:')
# print('Предложение вопросительное' if sentence[-1] == '?' else 'Обычное предложение')

# Ternary operator(Тернарный оператор) - конструкция которая алалогичная по своим свойствам и действию конструкции if/else eo при этом записывается в одну строчку кода.
# <выражение если в условии True> if <условие> else <выражение если False>

# number = 18
# res = 'even number' if number % 2 == 0 else 'odd number'
# print(res)
#-----------------------------------------------------
# from string import digits

# symbols = digits + '-'
# print(symbols)
# number = input('Ввести число: ')
# is_correct = True
# for i in number: #567  #67i
#     if i not in symbols: #0123456789-
#        is_correct = False
# if is_correct:
#     print('Yes number')
#     number = int(number)
#     print('Your namber:', number)
#     result = number if number >= 0 else -number # -(-56)
# else:
#     print('Invalid values!')
# -------------------------------------------------------

# print(digits)
# print(type(digits))

# number = input('Ввести число: ')
# if number.isdigit():
#     number = int(number)
#     print('Да число')
# else:
#     print('Вы ввели не число!')

# from string import digits
# -------------------------------------------
# from string import digits
# flag = True
# symbols = digits + '-' + '.'
# while flag:
#     is_correct_number = True
#     num1 = input('Vvedite petvoe chislo: ')
    
#     if len(num1) == 1 and (num1 == '.' or num1 == '-') and num1:
#         print('Вы ввели неправильное число!')
#         is_correct_number = False

#     for x in num1:        
#         if x not in symbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue     
#     num2 = input('Vvedite vtoroe chislo: ')
    
#     if len(num2) == 1 and (num2 == '.' or num2 == '-') and num2:
#         print('Вы ввели неправильное число!')
#         is_correct_number = False

#     for x in num2:        
#         if x not in symbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break    
#     if not is_correct_number:
#         continue       
#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     print(num1)
#     print(num2)
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
# ------------------------------------------------









