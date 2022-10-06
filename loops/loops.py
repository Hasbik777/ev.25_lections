# Циклы - это конструкция, при помощи которых можно организовать многократное исполнения определенного кода

# while <expression>:
#     <body>
# <else>:
#       <Body>

# i = 1
# while i <= 10:
#     print(f'Цикл выполнился {i} раз!')
#     i += 1
# else:
#     print('Конец цикла!')

# print('Начала кода')

# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != 'john' and name2.lower() != 'jamie':
#     name1 = input('Введите имя1: ')
#     name2 = input('Введите имя2: ')
#     i += 1
#     if i > 4:
#         print('Цикл остановлен!')
#         break
# else:
#     print('Вы ввели правильное имя!')

# admin = ['johnsnow23', 'ilovepython23']
# i = 3
# username = None
# password = None
# while username != admin[0] or password != admin[1]:
#     username = input('Введите username: ') 
#     password = input('Введите password: ')
#     i -= 1
#     if i == 0:
#         print('Ты далбаеб?')
#         break
# else:
#     print(f'{admin[0]} базару нет красавчик!')

#----------------------------------------------

# for <variable> in <iterable object>:
#     <body>

# list_ = [0, 1, 2, 3, 4, 5]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i)) 
# for x in list_:
#     print(x)

#----------------------------------------------

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# for x in ls:
#     print(f'Element: {x}')

# i = 0
# while i < len(ls):
#     print(f'Element: {ls[i]}')
#     i += 1

#------------------------------------------------------
# secret_list = ['DeltaViski', 'LOTR123', 'JohnSnow']
# word = input('Введите secret cod: ')
# while word not in secret_list:
#     print('Incorect word! try one more time!')
#     word = input('Введите secret cod: ')

# print(f'You\'re welcome my asshole, {word}!')

# -----------------------------------------------------
# 1)
# steps = 8
# path = 'UDDDUUDUU'
# res = 1

# 2)
# step = 9
# path = 'UDDUUDDUU'
# res = 2

# steps = 8
# path = 'UDDDUUDUU'
# sea_level = 0
# dolina = 0
# for x in path:
#     if x == 'U':
#         sea_level += 1
#         if sea_level == 0:
#             dolina += 1
#     elif x == 'D':
#         sea_level -= 1    
# print(dolina)




















