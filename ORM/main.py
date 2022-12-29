# ORM (Object-Relational Mapping) - технолог63ия программирования, благодаря которой разработчики могут использовать язык программирования для взаимодействия  с реалеционной базой данных (PostgresSQL, MySQL итд), всесто того чтобы писать оператора SQL, вы будете писать код ООП на языке программирования. Это очень сильно ускоряет разработку приложения и бд, особенно на начальных этапах.  

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'orm_db',
    user='sanjar',
    password='1',
    host='localhost',
    port=5432
)
