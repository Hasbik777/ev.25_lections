# list() -> (список, массив) - изменяем, последовательный тип данных, который представляет из себя коллекцию каких либо обьектов(значений)


# my_list = [1, 'string', False, None, [1,2,3]]
# print(my_list)
# print(type(my_list))

# range() - возвращает последовательноть элементов (чисел)
# ----------------------------------------------------
# ls = list(range(1, 101))
# print(ls)
# print(type(ls))

# ls1 = list(range(0, 101, 2))
# print(ls1)

# ls = list(range(1, 101))

# for num in ls:
#     #print(num ** 2 if num % 2 == 0 else num ** 3)
#      if num % 2 == 0:
#         print(f'Число {num} четное, квадрат: {num ** 2}')
# else:
#         print(f'Число {num} четное, куб: {num ** 3}')

# ----------------------------------------------------
# Методы списков:

# print(dir([]))

# append(element) - Добавляет element в конце списка

# ls = [1, 2, 3]
# print(ls)
# ls.append(5)
# ls.append([6, 7, 8])
# ls.append(True)
# print(ls)

# extend(iterable) -> расширяет список элементами из iterable object

# ls = [1, 2, 3]
# ls.append('Hello')
# print(ls)
# ls.extend('Hello')
# print(ls)
   

# ls = [1, 2, 3]
# ls.append([4, 5, 6])
# print(ls)
# ls.extend([4, 5, 6])
# print(ls)
   
# insert(<index>, <element>) - добавляет элемент по указанному index

# ls = ['string', 2, 3, False]
# ls.insert(1, 4)
# ls.insert(15, True)
# print(ls)

# index(element, [start], [end]) - возврашает index елемента в списке

# ls = ['Hello', 'World', 'my', 'name', 'is', 'John']
# result = ls.index('name')
# print(result)
# print(ls[result])

# print(ls[0: 2])
# print(ls[-1][0])

# count(element) - возвращает количество вхождений element в списке

# ls = [1, 2, 3, 4, 5, 6, 5, 5, 5]
# result = ls.count(5)
# print(result)
# ----------------------------------------------------------------------
# ls = ['Hello', 'World', 'my', 'name', 'is', 'John', 'North', 'King', 'Queen', 'USA']
# print(ls)
# str1 = input('Введите слово: ')

# if str1 in ls:
#     print(f'"{str1}" если в списке его индекс: {ls.index(str1)}')
# else:
#     print('Нет!')
# -----------------------------------------------------------------------

# sort() - сортирует список, если в аргументах передать revers=True, то список будет отсортирован в убывающем порядке

# import random

# ls = []
# for x in range(0, 50):
#     ls.append(random.randint(0, 1000))
# print(ls)
# ls.sort(reverse=True) 
# print()
# print(ls)
# -----------------------
# ls = ['John', 'Deyneris', 'Tirion', 'apple', 'Aykol', 'Nurayim', 'makers']
# ls.sort(key=len)
# print(ls)
# -----------------------

# remove(element) - удаляет element из списка, если такого нет, то выводит ошибка
# pop([index]) - удаляет и возвращает element по index, но если index не указан, то удаляет последний element

# ls = [5, 1, 2, 4, 5, 5, 5]
# # ls.remove(5)
# print(ls)
# while 5 in ls:
#     ls.remove(5)

# print(ls)


# ls = [5, 1, 2, 4, 5, 5, 5, 99]
# deleted = ls.pop(0)
# print(ls)
# print(deleted)
# print(ls.pop())
# print(ls)

# update ----------------------------------- обновление значение
# ls = [1, 'h', 3]
# print(ls)
# ls[1] = 2
# print(ls)


#################################################################################
# list_ = ['world', 'hello']
# print(list_)
# new_list = list_
# new_list.reverse()
# print(new_list)

# new_list = []
# list_ = ['world', 'hello']
# for i in list_:
#     new_list = str(list_.reverse()) 
#     print(new_list)

##########################################################################

# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b + c or b >= a + c or c >= b + a:
#     print('impossible')
# elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
#     print('rectangular')
# elif a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > b**2 + a**2:
#     print('obtuse')
# elif a**2 < b**2 + c**2 or b**2 < a**2 + c**2 or c**2 < b**2 + a**2:
#     print('acute')


# string = '123123'
# if int(string[0]) + int(string[1]) + int(string[2]) == int(string[3]) + int(string[4]) + int(string[5]):
#     print('да')
# else:
#     print('нет')

# --------------------------------------------------------------

# a = int(input())
# b = int(input())
# c = int(input())
# if a > b and a > c:
#     if b > c:
#         print(a,b,c)
#     else:
#         print(a,c,b)
# elif b > a and b > c:
#     if a > c:
#         print(b,a,c)
#     else:
#         print(b,c,a)
# if c >  b and c > a:
#     if b > a:
#         print(c,b,a)
#     else:
#         print(c,a,b)

# -------------------------------------------
# a = int(input())
# b = int(input())
# c = int(input())
# ls = []
# ls.append(a)
# ls.append(b)
# ls.append(c)
# print(*sorted(ls))