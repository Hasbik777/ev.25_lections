# PostgresSQL - Система управление базами данных(СУБД/DBMS)
# Это ряд программ и инструментов позволяющих создавать БД, управлять ею и манипулировать данными внутри БД(CRUD)

# Postgres - Сама база данных, она обьектно-реалиционная, то есть данные храняться в видк таблицы имеют связи между собой (relations)

# SQL(Structured Query language) - декларированный язык структурированных запросов, он применяется для создание и получения данных при помощи запросов в БД

# ------------------------------------------------------------------------------------------
# Типы полей в Postgres

# 1. Numeric types:
    # a. smallint(2 bytes) -> -32767 to 32767
    # b. integer(4 bytes) -> -2147000 to 2147000
    # c. bigint(8 bytes) -> ...
    # d. serial(4 bytes) -> auto-increment(integer, 1-2147000)
    # c. real(4 bytes) -> число с плаваюшей точкой, вещественное число
    # f. double precision(8 bytes) -> real но только с двойной точности 

# 2. Character types(Строковые типы):
    #  a. varchar(кол-во 255) -> можем указать максимальное кол-во символов в ручную. Если мы указали максимальную кол-во символов. в 50, а заполним всего 10, то остальные 40 символов остануться не заполненными, то есть пустыми
    # b. char(255) - если не заполним все символы то остальные заполняться пробелами 
    # c. text - неограниченное  кол-во символов

# 3. Boolean types:
#      boolean(1 byte) -> True/False

# 4. date - календарная дата(год.месяц.день)

# 5. location - координатная точка -> (245, -12) (x, y)

# ----------------------------------------------------------

# связи между таблицами(relations):
        #  1. Один к одному (One-to-one) - Человек и паспорт
        #  2. Один ко многим (One-to-many) - Человек и банковские карты
        #  3. Многие ко многим (Many-to-many) - Студенты и преподы

# Ограничение(Constraints):
        #  1. NOT NULL
        #  2. UNIQUE
        #  3. CHECK -> CHECK number > 5
        #  4. PRIMARY KEY(для установки идентификатора данных в таблице)
        #  5. FOREIGN KEY(для установки связи между таблицами)        
        #  6. ON DELETE(для установки при удалении данных которые были связаны) -> SET NULL, CASCADE, RESTRICT, SET DEFAULT (value)
           
# ----------------------------------------------------------------
# ubuntu: sudo -u postgres psql -> команда для входа в постгрес через корневого пользователя postgres
# psql -> для входа в СУБД через своего юзера

# \q -> выхода из СУБД

# \du -> список всех юзеров 

# \l -> список всех баз данных

# \c <dbname> -> команда подлючения к бд
#     \dt -> список всех таблиц в бд 

# \d <dbname> -> подробная информация про бд

# ИМПОРТ данных при помощи файла:
# psql -U<ваш_юзер_нэйм> -d<база_данных_создайте_предварительно> -f<путь_до_файла> 

# CREATE DATABASE <dbname>; -> команда для создание базы данных

# CREATE USER <username> WITH PASSWORD <password>; -> команда для создания юзера

# ALTER USER <username> WITH SUPERUSER; -> команда для изменения статуса юзера на суперюзера

# SELECT <row/column> FROM <tablename>;
    # * (ALL)
    #  -> Команда для получения данных из таблиц

# WHERE: используется для фильтрации по полям. Будут выводиться только те данные которын соотвествуют условию оператору WHERE  
# Синтаксист: SELECT <row> FROM <tablename> WHERE <row> = 'чему либо'

# BETWEEN: условия 'между'
# SELCET * FROM products WHERE id BETWEEN 3 and 8;

# AND: оператор и, для множества условий

# LIKE: выводит результат который соотвествует введенному шаблону для строк. Чувствителен к регистру
# ILIKE: тоже самое только не зависит от регистра  

# ORDER BY: сортировка по входящим данным по убыванию или возрастанию.
    #    ASC(по возрастанию) DESC(по убыванию)
# Синтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC];

# Агрегационные функции - AVG(), COUNT(), MIN(), MAX(), SUM()

# AS (ALIAS)
# SELECT name, price * quantity AS total FROM products;

# CROUP BY разделяет данные которые мы получаем в SELECT, при этом группируя их по определенному  признаку. И теперь для каждой группы можно использовать функции

# SELECT city, MAX(temp_hi), AVG(prcep), SUM(temp_low) as summa_temp, MIN(date) FROM weather GROUP BY city;

# HAVING: он работает так же как и  WHERE, только с оператором GROUP BY

# Команда для создания таблицы 
# CREATE TABLE <tablename> (
#     <name_column> <type>,
#     <name_column> <type>,
# );
# DROP TABLE/DATABASE <name>; -> удаляет
        
    #    CREATE TABLE weather (city varchar(80),
    #                         date date,
    #                         temp int);


# Команда для добавления данных в таблицу
# INSERT INTO <tablename> [(columns)] VALUES (<data>);

# INSERT INTO cities (name, location) VALUES ('Bishkek', '(42, 74)');

# Команда обновления 
# UPDATE <tablename> SET <row> = <new_value>
# WHERE <row> = <value>;

# Команда для удаления
# DELETE FROM <tablename> WHERE <row>=<value>;


# --------------------------------------------------------------------------
# class ContactList(list):
#     def search_by_name(self, name):
#         self.name = name

#     def info(self):
#         return self.name

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
# print(all_contacts.search_by_name('Olya'))

# class ContactList(list):
#     def __init__(self, list_):
#         self.list_ = list_
        
#     def search_by_name(self, name):
#         a = [i for i in self.list_ if name in i]
#         # for x in self.list_:
#         #     print(x)
#         #     if name in x:
#         #         a.append(x)
#         return a
            
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
# print(all_contacts.search_by_name('Olya'))

# list_ = [x == False if x % 2 != 0 else True for x in range(1, 11)]
# print(list_)
# ---------------------------------------------------------------------------------

# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1, orders o1 WHERE p1.id = o1.product_id; - Запрос сразу в две таблицы

# JOIN соединение таблиц
# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1 JOIN orders o1 ON p1.id = o1.product_id;

# JOIN: выборка данных из 2 таблиц, соединение таблиц

# LEFT JOIN: выборка будет содержать все строки из левой таблицы

# RIGHT JOIN: выборка будет содержать все строки из правой таблицы

# INNER JOIN: выводит все данные согласно условию