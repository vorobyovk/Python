from collections import UserList

# class Human:
#     def __init__(self, name: str, age: int = 0):
#         self.name = name
#         self.age = age
#     def say_hello(self) -> str:
#         return f'Hello! I am {self.name}'
#     def __str__(self):
#         return f"Human named {self.name} who is {self.age} years old"    
#     def __repr__(self):
#         return f"Human({self.name}, {self.age})"
# bill = Human('Bill')
# print(bill.say_hello())
# print(bill.age)
# jill = Human('Jill', 20)
# print(jill.say_hello())
# print(jill.age)
# print(bill.__repr__())
# print(jill.__repr__())
# print(bill)
# print(jill)

# class BoundedList:
#     def __init__(self, min_value: int, max_value: int):
#         self.min_value = min_value
#         self.max_value = max_value
#         self.__data = []
#     def __getitem__(self, index: int):
#         return self.__data[index]
#     def __setitem__(self, index: int, value: int):
#         if not (self.min_value <= value <= self.max_value):
#             raise ValueError(f"Value {value} must be between {self.min_value} and {self.max_value}")
#         if index >= len(self.__data):
#             # Додати новий елемент, якщо індекс виходить за межі
#             self.__data.append(value)
#         else:
#             # Замінити існуючий елемент
#             self.__data[index] = value
#     def __repr__(self):
#         return f"BoundedList({self.max_value}, {self.min_value})"
#     def __str__(self):
#         return str(self.__data)

# if __name__ == '__main__':
#     temperatures = BoundedList(18, 26)
#     for i, el in enumerate([20, 22, 25, 27]):
#         try:
#             temperatures[i] = el
#         except ValueError as e:
#             print(e)
#     print(temperatures)

# class BoundedList(UserList):
#     def __init__(self, min_value: int, max_value: int, initial_list=None):
#         super().__init__(initial_list if initial_list is not None else [])
#         self.min_value = min_value
#         self.max_value = max_value
#         self.__validate_list()
#     def __validate_list(self):
#         for item in self.data:
#             self.__validate_item(item)
#     def __validate_item(self, item):
#         if not (self.min_value <= item <= self.max_value):
#             raise ValueError(f"Item {item} must be between {self.min_value} and {self.max_value}")
#     def append(self, item):
#         self.__validate_item(item)
#         super().append(item)
#     def insert(self, i, item):
#         self.__validate_item(item)
#         super().insert(i, item)
#     def __setitem__(self, i, item):
#         self.__validate_item(item)
#         super().__setitem__(i, item)
#     def __repr__(self):
#         return f"BoundedList({self.max_value}, {self.min_value})"
#     def __str__(self):
#         return str(self.data)
#     def __getitem__(self, index):
#         # Додати спеціальну логіку тут, наприклад, логування або перевірку
#         print(f"Accessing item at index {index}")
#         # Викликати оригінальний метод __getitem__
#         return super().__getitem__(index)

# if __name__ == '__main__':
#     temperatures = BoundedList(18, 26, [19, 21, 22])
#     print(temperatures)
#     for el in [20, 22, 25, 27]:
#         try:
#             temperatures.append(el)
#         except ValueError as e:
#             print(e)
#     print(temperatures)
#     print(temperatures.__getitem__(5))

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def __eq__(self, other):
#         if not isinstance(other, Rectangle):
#             return NotImplemented
#         return self.area() == other.area()
#     def __ne__(self, other):
#         return not self.__eq__(other)
#     def __lt__(self, other):
#         if not isinstance(other, Rectangle):
#             return NotImplemented
#         return self.area() < other.area()
#     def __le__(self, other):
#         return self.__lt__(other) or self.__eq__(other)
#     def __gt__(self, other):
#         if not isinstance(other, Rectangle):
#             return NotImplemented
#         return self.area() > other.area()
#     def __ge__(self, other):
#         return self.__gt__(other) or self.__eq__(other)

# if __name__ == "__main__":
#     rect1 = Rectangle(5, 10)
#     rect2 = Rectangle(3, 20)
#     rect3 = Rectangle(5, 10)
#     print(f"Площа прямокутників: {rect1.area()}, {rect2.area()}, {rect3.area()}")
#     print(rect1 == rect3)  # True: площі рівні
#     print(rect1 != rect2)  # True: площі не рівні
#     print(rect1 < rect2)  # True: площа rect1  менша, ніж у rect2
#     print(rect1 <= rect3)  # True: площі рівні, тому rect1 <= rect3
#     print(rect1 > rect2)  # False: площа rect1 менша, ніж у rect2
#     print(rect1 >= rect3)  # True: площі рівні, тому rect1 >= rect3

# class Multiplier:
#     def __init__(self, factor):
#         self.factor = factor
#     def __call__(self, other):
#         return self.factor * other

# # Створення екземпляра функтора
# double = Multiplier(2)
# triple = Multiplier(3)
# # Виклик функтора
# print(double(5))  # Виведе: 10
# print(triple(3))  # Виведе: 9

# class Counter:
#     def __init__(self):
#         self.count = 0
#     def __call__(self, *args, **kwargs):
#         self.count += 1

# counter = Counter()
# counter()
# counter()
# print(f"Викликано {counter.count} разів")

class MyContextManager:
    def __enter__(self):
        # Ініціалізація ресурсу
        print("Enter the block")
        return self  # Може повертати об'єкт
    def __exit__(self, exc_type, exc_value, traceback):
        # Звільнення ресурсу
        print("Exit the block")
        if exc_type:
            print(f"Error detected: {exc_value}")
        # Повернення False передає виключення далі, True - поглинає виключення.
        return False

# Використання власного менеджера контексту
with MyContextManager() as my_resource:
    print("Inside the block")
    raise Exception("Something went wrong")