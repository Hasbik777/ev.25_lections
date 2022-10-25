# num = 1
# while num >= 0:
#     try:
#        num = int(input('Enter the number: '))
#     except ValueError:
#         pass   
# else:
#     print('Встретилась отрицательое число!')

# -------------------------------------------------

# from random import randint
# ls = []
# for x in range(0, 100):
#     ls.append(randint(1, 50))
# print(ls)
# ls = list(set(ls))
# res = sorted(ls)
# print(res)

# ---------------------------------

# def introduce(name, last_name, wife='Холост', **kwargs):
#     print(f'Привет это {name} {last_name}')
#     print(f'Он {wife}!')
#     if kwargs:
#         print(f'Инициалы его жены {" ".join(kwargs.values())}')
# introduce('John', 'Snow')
# introduce('Tirion', 'Lanister', 'Женат', wife_name='Sansa', wife_last_name='Stark')

# ---------------------------------------------------------------

# roles = {
#     0: 'Admin',
#     1: 'Customer',
#     2: 'Vendor',
# }
# users = [
#     {
#         'id': 1,
#         'username': 'John',
#         'role': roles[0]
#     },
#     {
#         'id': 3,
#         'username': 'Tirion',
#         'role': roles[2]
#     },
#     {
#         'id': 2,
#         'username': 'Raychel',
#         'role': roles[1]
#     }
# ]
# product = {
#     'id': 1,
#     'title': 'Iphone 14',
#     'description': 'Lorem Ipsum',
#     'price': 1200
# }
# print(f'Before: {product}')
# try:
#     id_user = int(input('Enter your id: '))
#     user = list(filter(lambda x: x['id'] == id_user, users))[0]
#     print(f'Welcom {user}!')
# except IndexError:
#     raise ValueError('Invalid id for user! User with this id does not exists!')
# print(user['role'])
# if user['role'] == roles[0]:
#     choice = input('Enter the change: ')
#     product[choice] = input('Enter the new values: ')    
# else:
#     raise Exception('Permission denied!')
# print(f'After: {product}')

# --------------------------------------------------------------------------------

# def get_percentage(money, period):
#     if money < 30_000:
#         raise Exception('Min stavka 30000 somov!')
#     if period < 3:
#         raise Exception('Min strok 3 goda!')
#     i = 0
#     while i < period:
#         money += money * 0.1 # money = money * 1.1 # money = (money / 100)
#         i +=1        
#     return money
# money = int(input('Vvedite summu deneg: '))
# year = int(input('Vvedite srok vashego deposita: '))
# print(get_percentage(money, year))

# -----------------------------------------------------------------------------

# ls = [[100,2,3], [300,3,5], [5,5,5,5], [45,45,6]]
# def find_max(ls):
#     return max(sum(x) for x in ls)
# print(find_max(ls))    

# --------------------------------------------------------

# def get_revers_string(text):
#     spisok = text.split()[::-1]
#     return ' '.join(spisok)
# print(get_revers_string('Hello world! My name is John, last name is Snow. Nice to meet you!'))    
# print(get_revers_string('hello john snow king'))