import time
import re

# from math import *
# import math
# print(pi)
# print(e)            
# print(tau)
# print(inf)  
# print(nan)
# print(cos(0))

# a = math.log(9,3)
# print(a)  
# print(math.exp(4*math.log(2)))  

# for i in range(1, 101):
#     if i == 100: 
#         print("Completed!")
#     else: 
#         print(f"\r{i}% Ready", end=' ')
#     time.sleep(0.1)

# TEXT1 = "Hello, \v World!" + chr(43)
# print(TEXT1)

# print('\' \\ \\xc3')

# text = """This is first line
# And second line
# Last third line"""

# song = '''Jingle bells, jingle bells
# Jingle all the way
# Oh, what fun it is to ride
# In a one horse open sleigh'''

# # print(text)
# # print(song) 
# # print("Length of text: ", len(song))
# # print(song.find("it"))
# # print(song.index("it"))
# # print(song.count("it"))

# result = song.split()
# print(result)

# result2 = ' '.join(result)
# print(result2)

# text = "one fish, two fish, red fish, blue fish"
# new_text = text.replace("fish", "bird", 2)
# print(new_text) 
# print(text.removeprefix("one"))
# print(text.removesuffix("fish"))

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)
# obj_query = {}
# for el in query.split('&'):
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)

# user_input = input("Введіть число: ")
# if user_input.isdigit():
#     print("Це дійсно число!")
#     if int(user_input) %2 == 0:
#         print("Це парне число!")
#     else:
#         print("Це непарне число!")
# else:
#     print("Це не число!")

# for char in "Hello 123":
#     if char.isdigit():
#         print(f"'{char}' - це цифра")
#     else:
#         print(f"'{char}' - не цифра")

# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)
# str = "This is string example"
# print(str.translate(trantab))

# symbols = "0123456789ABCDEF"
# code = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
# MAP = {}
# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c
# result = "34 DF 56 AC".translate(MAP)
# print(result)
# print(MAP)

# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#               'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
#               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#               '8': '---..', '9': '----.'}
# # Перетворення ключів словника на Unicode коди
# table_morze_dict = {}
# for k, v in morze_dict.items():
#     table_morze_dict[ord(k)] = v
# string = "Hello world"
# result = ""
# for ch in string:
#     result = result + ch.upper().translate(table_morze_dict)
# print(result)

# for i in range(8):
#     s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
#     print(s)

# width = 5
# for num in range(12):
#     print(f'{num:^10} {num**2:^10} {num**3:^10}')

# name = "Alice"
# formatted = f"{name:>10}"
# print(formatted)

# completion = 0.756
# formatted = f"{completion:.1%}"
# print(formatted)

# text = "Вивчення Python може бути веселим."
# pattern = "Python"
# match = re.search(pattern, text)
# if match:
#     print("Знайдено:", match.group())
# else:
#     print("Не знайдено.")

# text = "Вивчення Python може бути веселим."
# pattern = r"ве\w*м"
# match = re.search(pattern, text, re.IGNORECASE)
# if match:
#     print("Знайдено:", match.group())
# else:
#     print("Не знайдено.")

# text = "Моя електронна адреса: example@example.com"
# pattern = r"\w+@\w+\.\w+"
# match = re.search(pattern, text)
# if match:
#     print("Електронна адреса:", match.group())

# email = "Моя електронна адреса: username@domain.com"
# #email = "Моя електронна адреса:"
# pattern = r"(\w+)@(\w+\.\w+)"
# match = re.search(pattern, email)
# if match:
#     user_name = match.group(1)
#     domain_name = match.group(2)
#     print("Ім'я користувача:", user_name)
#     print("Домен:", domain_name)
# else:
#     print("Електронна адреса не знайдена.")

# text = "Рік 2023 був складнішим, ніж 2022"
# pattern = r"\d+"
# matches = re.findall(pattern, text)
# print(matches)

# text = "Python - це проста, але потужна мова програмування."
# pattern = r"\w+"
# matches = re.findall(pattern, text)
# print(matches)  # Виведе список всіх слів у рядку

# text = "Контакти: example1@example.com, example2@sample.org"
# pattern = r"\w+@\w+\.\w+"
# matches = re.findall(pattern, text)
# print(matches)  # Виведе всі знайдені електронні адреси

# phone = """
#         Михайло Куліш: 050-171-1634
#         Вікторія Кущ: 063-134-1729
#         Оксана Гавриленко: 068-234-5612
#         """
# pattern = r"(\d{3})-(\d{3})-(\d{4})"
# replacement = r"(\1) \2-\3"
# formatted_phone = re.sub(pattern, replacement, phone)
# print(formatted_phone)

# text = "Python - це проста, але потужна мова програмування."
# pattern = r"\s+"
# words = re.split(pattern, text)
# print(words)  # Виведе список слів у рядку

# text = "Python - потужна; проста, універсальна: мова!"
# pattern = r"[;,\-:!\s]+"
# elements = re.split(pattern, text)
# print(elements)  # Виведе список частин, розділених пунктуацією

text = "apple#banana!mango@orange;kiwi"
pattern = r"[#@;!]"
fruits = re.split(pattern, text)
print(fruits)

