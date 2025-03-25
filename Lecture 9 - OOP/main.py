class Person:
    def __init_(self, name:str, age:int, email:str, phone:str):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone     

    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
    def say(self):
        return f"Hello {self.name}"
    
    def call(self):
        return f"Calling {self.name} to phone num: {self.phone}"
    
    def mail(self):
        return f"Mail to {self.name} using address: {self.email}"

p = Person('kir', 20, 'kir@mail.com', '3809512345678')
p2 = Person('Nat', 23, 'nat@mail.com', '+3809512345678') 
p2.phone = "0501234567"

print(p.call())
print(p.mail())
print(p.say())
print(p2.call())

