# Функции - это именованная часть программы, которая может вызываться в других частях программы столько раз сколько нужно

# def name_of_function(<a, b> #параметры):
    # <body> код, какая то логика, которая будет запускаться при обращении к функции  
    # [<return>] оператор для возвращения результата

# name_of_function(5, 6 #аргумент)

# Параметры функции - переменные которые будет принимать ваша функция, для того чтобы мы смогли работать с данными которые попадают в нашу функцию, данные сохраняются в параметрых 

# Аргумент - данные которые мы передаем для параметров при вызове функции

# return - оператор который нужен чтобы функция возвращала результат, если нет return в функции, функции по умолчанию возвращает None

# res = print('Hello')
# print(res)

# res = max(range(1,100))
# print(res)

# def sum_two_nums(num1, num2): # пареметры
#     result = num1 + num2
#     return result
# result = sum_two_nums(5, 6)
# print(result)


# def our_len(a):
#     try:
#        res = 0
#        for x in a:
#             res += 1
#        return res
#     except TypeError:
#         return 'Value is not iterable!'
# ls = [1,2,3,4,5,6,7,8,9]
# str1 = 'Hello world! My name is John Snow!'
# print(our_len(ls))
# print(our_len(str1))
# print(our_len(True))


# def is_even(num):
#     if num % 2 == 0:
#       return True
#     return False
# b = int(input('Enter the numbers: '))
# print(is_even(15))
# print(is_even(b))
# print(is_even(24))
# print(is_even(98))


# def get_polindorms(words):
#     result = []
#     for x in words:
#         if x.lower() == x[::-1].lower():
#             result.append(x)
#     return result        
# some_words = ['John', 'ono', 'Kazak', 'peter', 'Dovod', 'tenet', 'anna', 'kak', 'piko']
# polindorms = get_polindorms(some_words)
# print(polindorms)











