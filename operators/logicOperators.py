# Оператор сравнения
# Условия операторы
# Логические операторы

# Операторы сравнения
# <, >, ==(равно), <=, >=, !=(не равно)

# 1 < 5 -> True
# 7 > 9 -> False

# num1 = 15
# num2 = 15
# print(num1 <= num2)

# num1 = 20
# num2 = 18
# print(num1 >= num2)

# stroka1 = 'hello'
# stroka2 = 'World'
# print(stroka1 > stroka2)
       #104       #87
         
# print('Hello world!')
# print(ord('H'))
# print(ord('а'))
# print(chr(1080), chr(1089))
# print(ord('N'))

# stroka1 = 'Hello!'
# stroka2 = 'World'
# print(len(stroka1) > len(stroka2))

# Условные операторы
# if
# elif
# else

# if <condition>:
#     <body if> # сработает если в выоажении if придет True
# [elif] <condition>:
#     <body elif> 
# [else]:
#     <body else> # сработывает если во всех выше стоящих условиях пришло False

# string = input('Enter smt: ')

# if string.lower() == 'hello':
#     print('Hello stranger!')
# elif string.lower() == 'john':
#     print('Welcome back John Snow! The king of North!')
# elif string.lower() == 'abra-kadabra':
#     print('Sim Salamon Kadabra')
# else:
#     print('Совпадений не найдено!')
    
# print(string)    

# email = input('Enter email: ')
# password1 = input('Enter the password: ')

# if len(password1) < 8:
#     raise ValueError('Password too short!')
# password2 = input('Enter the password confirmation: ')

# if password2 != password1:
#     raise ValueError('Password didn\'t match')
# else:
#     print('Successfully signed up!')

# age = input('Enter your age: ')
# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid values!')    

# if age < 18:
#     print(f'Access Denied! Come again after {18 - age} age!')
# else:
#     print('You can buy it!!!')


# Логические операторы
# and -> Логическая и
# or -> Логическая или
# not -> Логическая отрицание

# my_age = 20
# your_age = 18
# result = my_age == 20 and your_age == 19
# print(result)

# result = my_age == 20 or your_age == 19
# print(result)

# result = not my_age == 20 and not your_age == 19
# print(result)















