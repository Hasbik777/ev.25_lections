# String - строки

'Hello world!'
"Hello world!"
"""
Hello world 
my name is John Snow
"""
# a = 5 # коммент

# Строки - это набор последовательных символов, которые мы используем для хранения и представления текстовой информации. Набор методов и операции которые мы можем использовать c данными в виде текста

# индексация в строке
# name = 'John'
# #         J = 0 = -4
# #         o = 1 = -3
# #         h = 2 = -2
# #         n = 3 = -1
# print(name)
# print(name[1]) 
# print(name[-1])

# str1 = 'birthday'
# print(str1[5], str1[6], str1[7])
# print(str1[-3], str1[-2], str1[-1])
# print(str1[0], str1[1], str1[2], str1[3], str1[4])

 
# Срезы по индексу
# [start, end, <step>]

# str1 = 'birthdaydkfgndkkjgdfghgl'
# str2 = str1[0:5]
# print(str2)
# print(str1[5:25])
# print(len(str1))
# print(str1[5:]) # до конца
# print(str1[:5])

# text = 'Hello world! My name is John! I\'m North King' 
# print(text)
# print(len(text))

# print(text[:12])
# print(text[13:29])
# print(text[30:])
# print(text[:12:2])
# print(text[::2])
# print(text[::-1])
# print(text[:12:-1])
# Конкатенация строк(слияние, соединение)

# word1 = 'Hello'
# word2 = 'World'
# probel = ' '

# result = word1 + probel + word2
# print(result)
# print(word1 + probel + word2 + '!')

# Форматирование строк
# 1. с помощью %
# 2. с помощью (.format())
# 3. Интерполяция строк(f-строки)

# % 
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')
# print('Hello, My name is', name, last_name)
# print('Hello, My name is' + ' ' + name + ' ' + last_name)
# print('Hello, My name is %s -> %s' %(name, last_name))

# .format
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')

# print('Hello, My name is {} {}'.format(name, last_name))

# f - строки
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')

# print(f'Hello, My name is {name} -> {last_name}!')

# Экранирование строк - механизм при промощи которого можно вставлять символы, которые сложно ввести с клавиатуры в строку
# \n - перенос строки
# \t - горизонтальная табуляция
# \v - вертикальная табуляция

# name = 'John\nSnow'
# lastName = '\vSnow'
# last_name = '\tSnow'

# print(name)
# print(lastName)
# print(last_name)











