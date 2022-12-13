import peewee
from models import Category, Product
import random

def add_category(name):
    try:
        data = Category(name=name.lower().strip())
        data.save()
        print(f'Сохранили категорию {name.strip()}!')
    except (peewee.IntegrityError, peewee.InternalError):
        print('Такая категория уже существует!')

# add_category('Платья      ')
# add_category('Джинсы')
# add_category('Футболки')
# add_category('Свитер')
# add_category('Обувь')

def add_product(name, price, category_name):
    try:
        print(Category.get(name=category_name.lower().strip()))
        category = Category.get(name=category_name.lower().strip())
        print(category, '!!!!!!!')
        category_exists = True
    except peewee.DoesNotExist:
        category_exists = False
        print(category_exists)
    if category_exists:
        data = Product(title=name, price=price, category_id=category)
        data.save()
        print(f'Сохранили товар {name}!')
    else:
        print(f'Категории {category_name} не существует!')

# add_product('ZARA t-shirt', 400, ' Футболки')
# add_product('Supeme t-shirt', 200, 'Футболки')
# add_product('DG t-shirt', 1000, 'Футболки')
# add_product('Aygen 48', 1500, 'Платья')
# add_product('Platye 50', 300, 'Платья')
# add_product('Lives 1110', 2000, 'Джинсы')
# add_product('Nike Air Jordan', 4000, 'Обувь')
# add_product('Badlon12', 800, 'Свитер')

# -------------------------------------------------------------------

# Добавление новых данных

# add_category('car')
# add_category('smartphone')

# with open('files/cars.txt', 'r') as file:
#     ls = file.readlines()
#     print(ls)
#     for i in ls:
#         name = i.replace('\n', '')
#         price = random.randint(5000, 20000)
#         add_product(name, price, 'car')

# with open('files/telefon.txt', 'r') as file:
#     ls = file.readlines()
#     print(ls)
#     for i in ls:
#         name = i.replace('\n', '')
#         price = random.randint(200, 1000)
#         add_product(name, price, 'smartphone')


category = Category.get(name='car')
print(category, category.name)

for product in category.products:
    print(f'Title: {product.title}, Price: {product.price}, Category:{product.category_id.name}\n')