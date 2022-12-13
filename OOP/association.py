# Ассоциация, Композиция, Агрегация
# Все эти 3 принципа очень похожи друг на друга. Все они означают что внутри одного обьекта будет существовать другой обьект

# Композиция 
# class Wall:
#     def __init__(self, direction) -> None:
#         self.type = direction

#     def __str__(self) -> str:
#         return f'{self.type}'

# class Room:
#     def __init__(self) -> None:
#         self.west_wall = Wall('west')
#         self.west_wall = Wall('east')
#         self.west_wall = Wall('south')
#         self.west_wall = Wall('north')

# obj = Room()
# print(obj.west_wall)

# ------------------------------------------------------------
# Ассоциация
# class Stream:
#     pass

# class Logger:
#     def __init__(self) -> None:
#         self.stream = None

#     def print_the_stream(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print('None stream!')

# logger = Logger()
# logger.print_the_stream()
# logger.stream = Stream()
# logger.print_the_stream()

# --------------------------------------------------------

# Агрегация
# class Stream:
#     def __str__(self) -> str:
#         return 'Stream object!'

# class Logger:
#     def __init__(self, stream=None) -> None:
#         self.stream = stream

#     def print_the_stream(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print('None stream!')

# stream = Stream()
# logger = Logger(stream)
# logger.print_the_stream()

# -----------------------------------------------------------------

# class Engine:
#     country = 'Germany'

#     def __init__(self, power) -> None:
#         self.power = power

#     def __str__(self) -> str:
#         return f'Power: {self.power}'

# class AudiCar:
#     brand = 'Audi'
#     country = 'Germany'

#     def __init__(self, model, power) -> None:
#         self.engine = Engine(power)
#         self.model = model

#     def __str__(self) -> str:
#         return f'{self.brand} {self.model} -> {self.engine} -> engine country: {self.engine.country}. Country of car: {self.country}'

# car = AudiCar('A8', 600)
# print(car)

# -----------------------------------------------------------------------------------

# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.km = cost_km

#     def get_total_cost(self):
#         km = self.km * self.cost

# class Namba(Taxi):
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.km = cost_km

#     def get_total_cost(self):
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом '

# class Yandex(Taxi):
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.km = cost_km

#     def get_total_cost(self):
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом '

# class Jorgo(Taxi):
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.km = cost_km

#     def get_total_cost(self):
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом '

# taxi1 = Namba('Namba')
# taxi2 = Yandex('Yandex')
# taxi3 = Jorgo('Jorgo')
# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14)) 
















