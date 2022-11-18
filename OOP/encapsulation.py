# Инкапсуляция:
# 1. Связь данных с методами которые должны управлять этими данными
# 2. Механизм при помощи которого можно ограничить доступ компонентов программы к другим компонентом(сокрытие данных)

# Инкапсуляция как связь

# class Phone:
#     number = '+996 503-503-503'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')

# my_phone = Phone()
# my_phone.print_number()


# Инкапсуляция как управления доступом
# 3 уровня доступа в питоне:
    # 1. Публичный(public) = self.number, def get 
    # 2. Защищенный(_protected, parent/child) = _number, def _get
    # 3. Приватный(__private, частные, используется только в текущем классе) = __number, def __get

# class Car:
#     _country = 'Germany'

#     def __init__(self) -> None:
#         self.brand = 'BMW' #public
#         self._model = '7 series' #protected
#         self.__motor = 'ABC' #private

#     def _get_date(self):
#         print('1 September')

# class Audi(Car):
#     pass

# class Auto(Audi):
#     pass

# obj = Auto()
# print(obj._country)

# audi = Audi()
# print(audi.brand)
# print(audi._model)
# print(_Audi__motor)

# car = Car()
# print(car.brand)
# print(car._country)
# print(car._model)
# print(car._Car__motor)
# car._get_date()

# -------------------------------------------------------

# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_talks = 15

#     def call(self):
#         print(f'{self._caller} звонит вам!')
#         question = input('Сбросить или взять: yes/no: ')
#         if question.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print('Пошел ты!')

#     def __turn_on(self):
#         self.__count_of_talks += 1
#         print('Алло пидр!')
#         print(f'Count of talks with Jamie {self.__count_of_talks}')

# john = Phone()
# john.call()
# john.call()

# --------------------------------------------------------------------------

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f'My name is {self.name} and I am {self.age} years old!')

# obj = Person('James', 18)
# obj.display_info()
# obj.name = 'Raychel'
# obj.age = -18
# obj.display_info()

# getter & setter
# Они использаются для получение и установки значений, чтобы добавить логику валидации(проверки) данных которые будут установлены в атрибуты которые имеют защиту
# Еще для того чтобы избежать прямого обращения к защишенному полю класса
  


