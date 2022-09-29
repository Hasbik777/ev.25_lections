# print(dir(str)) #методы строк

# replace(old, new, [count]) -  меняет в строке old на new значение, если вы укажите count, то он заменит его ровно count раз

#text = 'ha ha ha ha'
# result = text.replace('a, 'i', 2)
# print(text)
# print(f'result after replace: {result:'})

# str1 = 'Hello world! My name is John Snow'
# res = str1.replace('John Snow', 'Jamie Lanester')
# res = res.replace(' ')
# print(res) 

# print(id('H'))
# print(id('H'))
# print(id('h'))

# strip() - Убирает пробельные символы в начале и в конце  стоки
# rstrip, lstrip

# text = input('Enter the text:')
# print(text)
# print(len(text))
# res = text.strip()
# print(res)
# print(len(res))

# text = '   Hello world   '
# print(len(text))
# res = text.lstrip()
# print(res)
# print(len(res))

# print(dir(str))

# isdigit ->
# isnumeric -> -> Проверяют состоит ли наша строка полностью из чисел
# isdecimal -> 

# text = '57277772'
# if text.isdigit():
#     num = int(text)
#     print(num)
# else:
#     print('Oops! Invalid symbol!')

# text = '\u0031'
# print(text)
# print(text.isnumeric())

# isalnum() -> проверяет состоит ли наша строка из чисел и символов латинского алфавита и киррилицы

# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())

# isalpha() -> состоит ли наша строка полностью из символов латинского либо киррильского алфавита

# text = 'Helloworld'
# print(text[:5].isalpha())

# islower()
# isupper()
# istitle()

# str1 = 'Is My Name. Lower'
# print(str1.istitle())

# index(value, [start], [end]) -> выводит индекс значения value которое мы передаем в нашей строке.

# text = 'Hello world! My name is John Snow'
# print(text.index('John'))
# print(text.index('o'))
# print(text[24])

# text = 'hello o o hello'
# print(text.count('hello'))
# print(text.count('o'))
# print(text.count(' '))

# text = 'oooHello world! Myo name is John Snowooo'
# text = input('Enter the text: ')
# i = 0
# res = -1
# while i < text.count('o'):  # 4
#     res = text.count('o', res+1)
#     print(res)
#     # print(i)
#     i += 1 #инкремент

# find(value, [start], [end]) -> делает тоже самое что и index, но есть одно отличие, в том что еслии value нет в строке то возвращается индекс -1

# text = 'Hello'
# print(text.find('l'))
# print(text.find('hi'))

# swapcase() -> Переводит все символы в противоположный регистр
# upper() -> все символы в верхний регистр
# lower() -> все символы в нижний регистр

# text = 'heLLO World, JoHN, SNow'
# print(text)
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

# capitalize() - переводит первую букву в верхний регистр

# name = input('Enter your name: ').capitalize()
# print(f'Hello Mr/Mrs {name}!')

# title() -> Переводит первый символ всех слов в верхний регистр

# text = 'john jamie sansa nursultan jerry'
# print(text)
# print(text.title())
# print(text.capitalize())

# name = input('Vvedite FIO: ')
# print(name.title())

# split(разделитель) - дробит строку на несколько частей по разделителю который находится в строке, все части строки сохраняются в тип данных list

# text = 'Let me speak by my hearth in English! Cause My name is John Snow'
# ls = text.split(' ')
# print(ls)
# print(len(ls))

# 'разделитель'.join(iterable(list)) -> Соединяет по разделителю строки, которые находяться в list

# res = '#'.join(ls)
# print(res)