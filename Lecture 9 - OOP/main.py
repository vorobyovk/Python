from collections import UserDict, UserList, UserString
from dataclasses import dataclass
from enum import Enum, auto


# class Person:
#     def __init__(self, name, age, email, phone):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone

#     def say(self):
#         return f"Hello {self.name}"
    
#     def call(self):
#         return f"Calling {self.name} to phone num: {self.phone}"
    
#     def mail(self):
#         return f"Mail to {self.name} using address: {self.email}"

# p = Person('kir', 20, 'kir@mail.com', '3809512345678')
# p2 = Person('Nat', 23, 'nat@mail.com', '+3809512345678') 
# p2.phone = "0501234567"
# print(p.call())
# print(p.mail())
# print(p.say())
# print(p2.call())

# class MyDictionary(UserDict):
#     # Приклад додавання нового методу
#     def add_key(self, key, value):
#         self.data[key] = value
# # Створення екземпляра власного класу
# my_dict = MyDictionary({'a': 1, 'b': 2})
# my_dict.add_key('c', 3)
# print(my_dict)

# contacts = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     {
#         "name": "Chaim Lewis",
#         "email": "dui.in@egetlacus.ca",
#         "phone": "(294) 840-6685",
#         "favorite": False,
#     },
#     {
#         "name": "Kennedy Lane",
#         "email": "mattis.Cras@nonenimMauris.net",
#         "phone": "(542) 451-7038",
#         "favorite": True,
#     }
# ]

# class Customer(UserDict):
#     def phone_info(self):
#         return f"{self.get('name')}: {self.get('phone')}"

#     def email_info(self):
#         return f"{self.get('name')}: {self.get('email')}"

# customers = [Customer(el) for el in contacts]
# print("---------------------------")
# for customer in customers:
#     print(customer.phone_info())
# print("---------------------------")
# for customer in customers:
#     print(customer.email_info())
# print(customers)

# class MyList(UserList):
#     # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, якщо він ще не існує
#     def add_if_not_exists(self, item):
#         if item not in self.data:
#             self.data.append(item)
#         else: print(f"This element: '{item}' already exist in the list")    
#     def summ_list(self):
#         return sum(self.data)        

# # Створення екземпляру MyList
# my_list = MyList([1, 2, 3])
# print("Оригінальний список:", my_list)
# # Додавання елементу, якщо він не існує
# my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
# my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
# print("Оновлений список:", my_list)
# print(my_list.summ_list())

# class MyString(UserString):
#     # Додавання методу, який перевіряє, чи рядок є паліндромом
#     def is_palindrome(self):
#         return self.data == self.data[::-1]
# # Створення екземпляру MyString
# my_string = MyString("radar")
# print("Рядок:", my_string)
# print("Чи є паліндромом?", my_string.is_palindrome())
# # Створення іншого екземпляру MyString
# another_string = MyString("hello")
# print("Рядок:", another_string)
# print("Чи є паліндромом?", another_string.is_palindrome())

# class TruncatedString(UserString):
#     MAX_LEN = 7
#     def truncate(self):
#         self.data = self.data[:self.MAX_LEN]
# ts = TruncatedString('hello world!')
# ts.truncate()
# print(ts)

# @dataclass
# class Person:
#     name: str
#     age: int

# Kir = Person('Kir', 20)
# print(Kir)
# Nat = Person('Nat', 23)
# print(Nat)

# @dataclass
# class Rectangle:
#     width: int
#     height: int

#     def area(self) -> int:
#         return self.width * self.height

# rect1 = Rectangle(10, 5)
# rect2 = Rectangle(7, 3)
# rect3 = Rectangle(8, 6)
# print(f"Площа прямокутника 1: {rect1.area()}")
# print(f"Площа прямокутника 2: {rect2.area()}")
# print(f"Площа прямокутника 3: {rect3.area()}")

# class Day(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7

# today = Day.MONDAY
# print(today.name)
# print(today.value)
# print(today)

# class OrderStatus(Enum):
#     NEW = auto()
#     PROCESSING = auto()
#     SHIPPED = auto()
#     DELIVERED = auto()

# class Order:
#     def __init__(self, name: str, status: OrderStatus):
#         self.name = name
#         self.status = status

#     def update_status(self, new_status: OrderStatus):
#         self.status = new_status
#         print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

#     def display_status(self):
#         print(f"Статус замовлення '{self.name}': {self.status.name}.")
    
# order1 = Order("Ноутбук", OrderStatus.NEW)
# order2 = Order("Книга", OrderStatus.NEW)
# order1.display_status()
# order2.display_status()
# order1.update_status(OrderStatus.PROCESSING)
# order2.update_status(OrderStatus.SHIPPED)
# order1.display_status()
# order2.display_status()

# class Owner:
#     def __init__(self, name: str, phone: str):
#         self.name = name
#         self.phone = phone

#     def info(self):
#         return f"{self.name}: {self.phone}"

# class Cat:
#     def __init__(self, nickname: str, age: int, owner: Owner):
#         self.nickname = nickname
#         self.age = age
#         self.owner = owner

#     def get_info(self):
#         return f"Cat Name: {self.nickname}, Age: {self.age}"

#     def sound(self):
#         return "Meow"

# owner = Owner("Boris", "+380503002010")
# cat = Cat("Simon", 4, owner)
# print(cat.owner.info())
# print(cat.get_info())

# class Task:
#     def __init__(self, name: str, description: str):
#         self.name = name
#         self.description = description
#     def display_info(self):
#         print(f"Задача: {self.name}, Опис: {self.description}")
# class Project:
#     def __init__(self, name: str):
#         self.name = name
#         self.tasks: list[Task] = []
#     def add_task(self, name: str, description: str):
#         self.tasks.append(Task(name, description))
#     def remove_task(self, name: str):
#         self.tasks = [task for task in self.tasks if task.name != name]
#     def display_project_info(self):
#         print(f"Проект: {self.name}")
#         for task in self.tasks:
#             task.display_info()
# # Створення проекту
# my_project = Project("Веб-розробка")
# # Додавання задач
# my_project.add_task("Дизайн інтерфейсу", "Створити макет головної сторінки.")
# my_project.add_task("Розробка API", "Реалізувати ендпоінти для користувачів.")
# # Відображення інформації про проект
# my_project.display_project_info()
# # Видалення задачі
# my_project.remove_task("Розробка API")
# # Перевірка видалення задачі
# my_project.display_project_info()

# class AgeVerificationError(Exception):
#     def __init__(self, message="Вік не задовольняє мінімальній вимозі"):
#         self.message = message
#         super().__init__(self.message)
# # Функція для перевірки віку
# def verify_age(age: int):
#     if age < 18:
#         raise AgeVerificationError("Вік особи менший за 18 років")
# if __name__ == "__main__":
#     # Обробка винятку
#     try:
#         verify_age(19)  # Змініть вік для різних результатів
#     except AgeVerificationError as e:
#         print(f"Виняток: {e}")
#     else:
#         print("Вік перевірено, особа доросла.")

# class NameTooShortError(Exception):
#     pass
# class NameStartsFromLowError(Exception):
#     pass
# def enter_name():
#     name = input("Enter name: ")
#     if len(name) < 3:
#         raise NameTooShortError("Name is too short, need more than 2 symbols")
#     if not name[0].isupper():
#         raise NameStartsFromLowError("Name should start from capital letter")
#     return name

# if __name__ == "__main__":
#     try:
#         name = enter_name()
#         print(f"Hello, {name}")
#     except (NameTooShortError, NameStartsFromLowError) as e:
#         print(e)

# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

# class Cat(Animal):
#     pass

# my_cat = Cat("masha", 5)
# print(my_cat.nickname)
# print(my_cat.age)

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

# animal = Animal("Simon", 10)
# print(animal.nickname)
# print(animal.weight)
# animal.say()
# animal.change_weight(15)
# print(animal.weight)

class Color:
    def __init__(self, color):
        self.color = color

class Animal:
    color = "white"
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
        self.color: str[Color] = self.color      
    def say(self):
        pass
    def change_weight(self, weight):
        self.weight = weight
    def change_color(self, color: str):        
        self.color: str[Color] = color
        
first_animal = Animal("Simon", 10)
print(first_animal.color)
first_animal.change_color("red")
second_animal = Animal("Back", 3)
print(second_animal.color)
second_animal.change_color("red")
print(first_animal.color)
print(second_animal.color)

# class Task:
#     def __init__(self, name: str, description: str):
#         self.name = name
#         self.description = description
#     def display_info(self):
#         print(f"Задача: {self.name}, Опис: {self.description}")
# class Project:
#     def __init__(self, name: str):
#         self.name = name
#         self.tasks: list[Task] = []
#     def add_task(self, name: str, description: str):
#         self.tasks.append(Task(name, description))
#     def remove_task(self, name: str):
#         self.tasks = [task for task in self.tasks if task.name != name]
#     def display_project_info(self):
#         print(f"Проект: {self.name}")
#         for task in self.tasks:
#             task.display_info()

