# class methods, instance methods, static methods

# Методы экземпляра(обьекта) класса (isinstance methods) - это те методы в ООП которые изменяют состояние обьекта от класса
    # def methods(self) - self это ссылка на обьект

# Методы класса(class methods) - это те методы которые могут изменять состояние самого класса и манипулировать им
#     @classmethod
#     def method(cls) - это ссылка на сам класс 

# Статические методы(static method) - это те методы которые не могут изменять состояние ни обьекта ни самого класса
    #  @staticmethod
    #  def method()

# class Student:
#     school_name = 'Sibat'

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def show(self):
#         print(self.name, self.age, 'School:', Student.school_name)

#     @classmethod
#     def change_school(cls, name):
#         # print(cls, '!!!!!!')
#         cls.school_name = name

# obj = Student('John Snow', 20)
# obj.show()
# obj.change_school('ABC school')
# obj.show()

# --------------------------------------------------------------------

# class MyDict(dict):
#     def get(self, key, value='Are you kidding?'):
#         return dict.get(self, key, value)
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some')) 

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self.name, self.age)

# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         super().display()
#         print(f'faculty: {self.faculty}')

# obj_student = Student('Rick', 21, 'science')
# obj_student.display() 
# obj_student.display_student() 

# ---------------------------------------------------------------------

# class Person:
#     surname = 'Stark'
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     @staticmethod
#     def is_adult(age):
#         if age >= 21:
#             print('Person is adult!')
#         else:
#             print('Not adult!')

#     @classmethod
#     def from_birth_date(cls, name, year):
#         from datetime import date
#         age = date.today().year - year
#         return cls(name, age) 

# obj = Person('John', 24)
# obj1 = Person.from_birth_date('Jamie', 1988)
# print(obj.name, obj.age)
# print(obj1.name, obj1.age)

# ---------------------------------------------------------






