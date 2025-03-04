#length = "2.75"
#width = "1.75"
#area = float(length) * float(width)
#show = f"With width {width} and length {length} of the room, its area is equal to {area}".format(width, length, area)
#print(show)


#name = input("Your name? ")
#email = input("Your email? ")
#age = int(input("Your age? "))
#height = float(input("Your height "))
#is_active = input("Your active/inactive ")
#if is_active != 0 : is_active = False
#else : is_active = True
#print(f"Your name is {name}, email is {email}, age is {age}, height is {height} and is active is {is_active}")  

#length = float(input("Please input lenght "))
#width = float(input("Please input width "))
#area = length * width
#print(f"Area of the room is {area}")

#my_list = []
#my_list.insert(0, 2024)
#my_list.insert(1, "Python")
#my_list.insert(2, 3.12)
#print(my_list)

#my_list = [2024, 3.12]
#some_data = ['Python']
#my_list.extend(some_data)
#print(my_list)
#my_list.insert(1, "Python")
#print(my_list)
#my_list.reverse()
#print(my_list)

#data = {"year": 2024, "lang": "Python", "version": 3.12}
#print(data)

#cat = {"nick": "Simon", "age": 7, "characteristics": ["soft", "fluffy"]}
#info = {"status": "vaccinated", "breed": True}
#print(cat)
#print(info)
#age = cat.get("age")
#cat.update(info)
#print(cat)  

#a = 0
#while a < 6:
#    a = a + 1
#    if a % 2:
#        continue
#    print(a)

#while True:
#    number = input("number = ")
#    number = int(number)
#    while True:
#        print(number)
#        number = number - 1
#        if number < 0:
#            break
    
#numbers = {
#    1: "one",
#    2: "two",
#    3: "three"
#}
#for key in numbers:
#    print(key)
#for key in numbers:
#    print(numbers[key])
#for val in numbers.values():
#    print(val)
#for key, value in numbers.items():
#    print(key, value)
#print(numbers)

#age = input("How old are you? ")
#try:
#    age = int(age)
#    if age >= 18:
#        print("You are adult.")
#    else:
#        print("You are infant")
#except ValueError:
#    print(f"{age} is not a number")

def is_even(num: int) -> bool:
    return num % 2 == 0 

check_even = is_even(4)
print(check_even)