# class Human():
#     is_human = True

#     def __init__(self, name,surname, age):   # consturctor
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def display(self):
#         return f"Name: {self.name}, Age: {self.age}"

#     @classmethod
#     def display_class(cls, fullname, age):
#         name, surname = fullname.split()
#         cls.name = name
#         cls.surname = surname
#         cls.age = age
#         return f"Name: {name}, Surname: {surname}"

#     @staticmethod
#     def check_age(age):
#         if age > 18:
#             return True
#         else:
#             return False


# # p1 = Human("John", 30)
# # p2 = Human("Alice", 25)
# # print(p1.display())
# # print(p1.is_human)
# # print(p2.display())
# # print(p2.is_human)
# # p3 = Human.display_class("John Doe", 28)
# # print(p3)


# print(Human.check_age(20))


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        ...


class Cat(Animal):
    def move(self):
        print("Cat can move")


p = Cat()
p.move()
