# def say_hello(string):
#     print("Hello, " + string + "!")
# say_hello("Kyrylo")

# def print_sum(a, b):
#     print(a + b)
# print_sum(3, 5)

# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum
# result = add_numbers(5, 10)
# print(result)

# def greet(name: str) -> str:
#     return f"Привіт, {name}!"
# name = input("Введіть своє ім'я: ")
# greeting = greet(name)
# print(greeting) 

# # immutable objects
# def modify_string(original: str) -> str:
#     original = "змінено"
#     return original
# str_var = "оригінал"
# print(modify_string(str_var)) 
# print(str_var)                
# # mutable objects
# def modify_list(lst: list) -> None:
#     lst.append(4)
# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3, 4]

# # copy mutable objects and modify new list
# def modify_list(lst: list) -> list:
#     lst = lst.copy()
#     lst.append(4)
#     return lst
# my_list = [1, 2, 3]
# my_list_mod = modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3]
# print(my_list_mod)  # виведе: [1, 2, 3, 4]

# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes
# my_string = input("Введіть рядок: ")
# codes = string_to_codes(my_string)
# print(codes)  # виведе словник з кодами символів рядка

# # LEGB change Global variable
# x = 50
# def func():
#     global x
#     print('x дорівнює', x)  # x дорівнює 50
#     x = 2
#     print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2
# func()
# print('Значення x складає', x)# Значення x складає 2

# def greet(name, message="Привіт"):
#     print(f"{message}, {name}!")
# greet("Кирило")  # виведе: Привіт, Кирило!

# def say(message, times=1):
#     print(message * times)
# say('Привіт') 
# say('Світ', 5)

# def real_cost(base: int, discount: float = 0) -> float:
#     return base * (1 - discount)
# price_bread = 15
# price_butter = 50
# price_sugar = 60
# current_price_bread = real_cost(price_bread)
# current_price_butter = real_cost(price_butter, 0.05)
# current_price_sugar = real_cost(price_sugar, 0.07)
# print(f"Ціна хліба: {current_price_bread}")
# print(f"Ціна масла: {current_price_butter}")
# print(f"Ціна цукру: {current_price_sugar}")    

# def print_all_args(*args):
#     for arg in args:
#         print(arg)
# print_all_args(1, 'hello', True)
# def concatenate(*args) -> str:
#     result = ""
#     for arg in args:
#         result += arg
#     return result
# print(concatenate("Hello", " ", "world", "!"))
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# greet(name="Alice", age=25)
# def example_function(*args, **kwargs):
#     print("Позиційні аргументи:", args)
#     print("Ключові аргументи:", kwargs)
# example_function(1, 2, 3, name="Alice", age=25)

# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83 : is_next = True
# else: is_next = False
# print(is_next)

# work_experience = int(input("Enter your full work experience in years: "))
# if work_experience > 1 and work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience <= 1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"
# print(f"Developer type: {developer_type}")

# num = int(input("Enter a number: "))
# if num > 0:
#     if num % 2 != 0:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"
# print(result)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# while num > 0:
#     sum += num
#     num -= 1
# print(f"Sum of numbers: {sum}")    

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for i in message:
#     if i == search:
#         result += 1
# print(f"Number of occurrences of the letter '{search}': {result}")

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity
#     print(f"Each mailing will receive {chunk} letters")
# except ZeroDivisionError:
#     print('Divide by zero completed!')

# def greeting():
#     print("Hello world!")
# greeting()

# def invite_to_event(username):
#     invite = (f"Dear {username}, we have the honour to invite you to our event")
#     return invite   
# string_invite = invite_to_event("Alice")
# print(string_invite)

# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price = price * (1 - discount)
#     apply_discount()    
#     return price
# price = 100
# discount = 0.1
# new_price = discount_price(price, discount)
# print(new_price)  # виведе: 90.0

# def get_fullname(firstname, lastname, middlename=""):
#     if not middlename == "":
#         return (f"{firstname} {middlename} {lastname}")
#     else:
#         return (f"{firstname} {lastname}")
# print(get_fullname("Petro","","Zaliznyak"))

# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     if len(string) < length:
#         spaces = (length - len(string)) // 2
#         formatted_string = " " * spaces + string
#     return formatted_string
# print(format_string("Hello", 10))  # виведе: "  Hello"

# def first(size, *args):
#     return size + args.__len__()
# def second(size, **kwargs):
#     return size + kwargs.__len__()    
# print(first(3, 1, 2, 3))
# print(second(3, a = 1, b = 2, c = 3))

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)
# def number_of_groups(n, k):
#     return int(factorial(n) / (factorial(k) * factorial(n - k)))
# n = 50
# k = 5
# result = number_of_groups(n, k)
# print(result)  # виведе: 2118760.0
