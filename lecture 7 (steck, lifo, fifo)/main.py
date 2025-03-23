from collections import defaultdict
from collections import deque
import decimal
from decimal import Decimal, getcontext

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)
# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)
# print(dict(grouped_words))

# # Створення стеку
# def create_stack():
#     return []
# # Перевірка на порожнечу
# def is_empty(stack):
#     return len(stack) == 0
# # Додавання елементу
# def push(stack, item):
#     stack.append(item)
# # Вилучення елементу
# def pop(stack):
#     if not is_empty(stack):
#         return stack.pop()
#     else:
#         print("Стек порожній")
# # Перегляд верхнього елемента
# def peek(stack):
#     if not is_empty(stack):
#         return stack[-1]
#     else:
#         print("Стек порожній")
# stack = create_stack()
# push(stack, 'a')
# push(stack, 'b')
# push(stack, 'c')
# print(stack)
# print(pop(stack))
# print(stack)
# push(stack, 'd')
# print(stack)

# # Створення черги
# queue = deque()
# # Enqueue: Додавання елементів
# queue.append('a')
# queue.append('b')
# queue.append('c')
# print("Черга після додавання елементів:", list(queue))
# # Dequeue: Видалення елемента
# print("Видалений елемент:", queue.popleft())
# print("Черга після видалення елемента:", list(queue))
# # Peek: Перегляд першого елемента
# print("Перший елемент у черзі:", queue[0])
# # IsEmpty: Перевірка на порожнечу
# print("Чи черга порожня:", len(queue) == 0)
# # Size: Розмір черги
# print("Розмір черги:", len(queue))

# # Створення пустої двосторонньої черги
# d = deque()
# # Додаємо елементи в чергу
# d.append('middle')  # Додаємо 'middle' в кінець черги
# d.append('last')    # Додаємо 'last' в кінець черги
# d.appendleft('first')  # Додаємо 'first' на початок черги
# # Виведення поточного стану черги
# print("Черга після додавання елементів:", list(d))
# # Видалення та виведення останнього елемента (з правого кінця)
# print("Видалений останній елемент:", d.pop())
# # Видалення та виведення першого елемента (з лівого кінця)
# print("Видалений перший елемент:", d.popleft())
# # Виведення поточного стану черги після видалення елементів
# print("Черга після видалення елементів:", list(d))

# # Список завдань, де кожне завдання - це словник
# tasks = [
#     {"type": "fast", "name": "Помити посуд"},
#     {"type": "slow", "name": "Подивитись серіал"},
#     {"type": "fast", "name": "Вигуляти собаку"},
#     {"type": "slow", "name": "Почитати книгу"}
# ]
# # Ініціалізація черги завдань
# task_queue = deque()
# # Розподіл завдань у чергу відповідно до їх пріоритету
# for task in tasks:
#     if task["type"] == "fast":
#         task_queue.appendleft(task)  # Додавання на високий пріоритет
#         print(f"Додано швидке завдання: {task['name']}")
#     else:
#         task_queue.append(task)  # Додавання на низький пріоритет
#         print(f"Додано повільне завдання: {task['name']}")
# # Виконання завдань
# while task_queue:
#     task = task_queue.popleft()
#     print(f"Виконується завдання: {task['name']}")



# print(0.1 + 0.2 == 0.3)
# print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

# print(0.1 + 0.2)
# print(Decimal("0.1") + Decimal("0.2"))

# print("===========================================")
# getcontext().prec = 6
# print(Decimal("1") / Decimal("7"))
# getcontext().prec = 8
# print(Decimal("1") / Decimal("7"))
# number = Decimal("1.45")
# # Округлення за замовчуванням до одного десяткового знаку
# print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))
# # Округлення вверх при нічиї (ROUND_HALF_UP)
# print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))
# # Округлення вниз (ROUND_FLOOR)
# print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR))
# # Округлення вверх (ROUND_CEILING)
# print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING))
# # Округлення до трьох десяткових знаків за замовчуванням
# print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000")))