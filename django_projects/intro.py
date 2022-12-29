# 1. Создали вертуальное окружения
   #  python3 -m venv venv

# 2. Установка библиотек и джанго
    # 1) pip install <library>
    # pip freeze > req.txt
    # 2) Запись названий в req.txt
    # pip install  -r req.txt

# 3. Создание проекта и файла manage.py 
    # django-admin startproject <name> .

# 4. Создать приложение для проекта
    # python3 manage.py startapp <name>
    # django-admin startapp <name>

# 5. Добавить приложение в настройки проекта, в настройки install_apps(подключение прилодения в ваш проект)

# 6. Настройка база данных
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': '<name>',
#         'USER': '<user>',
#         'PASSWORD': '<1>',
#         'HOST': 'localhost',
#         'POST': 5432
#     }
# }
# Создали бд в postgres

# 8. Работа с  миграциями
    # 8.1 Создание файла миграции
    #    python3 manage.py makemigrations
    # 8.2 Запускаем файл миграции(отправить изменения в бд)
    #    python3 manage.py migrate

# Запуск сервера
    # python3 manage.py runserver

# Создание суперюзера
    # python3 manage.py createsuperuser

# models.py -> отвечает за связь с бд
# Каждый класс это таблица с определенными полями
# Модуль который вносит изменения в БД - psycopg2-binary
# ./ manage.py makemigrations -> подготавливает файл  запрос для БД
# ./ manage.py migrate -> применяет команды на БД

# urls.py -> маршрутизатор
# Клиент кидает запрос - запрос проходит проверки
# - запрос попадает в файл urls.py -> среди путей которые прописаны в urlpatterns находиться совподающая ссылка -- вызывается функция-обработчика

# views.py - файл с функциями обработчиками которые отвечает за получение или модификацию данных

# В зависимости вида запроса (get -> 
# 1. кидает запрос в базу  данных и получают QuerySet
# 2. использует сериализатор чтобы конвертировать данные в нужный формат
# 3. возвращает данные фронту)






















