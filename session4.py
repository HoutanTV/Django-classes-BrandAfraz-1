# polymorphism
# from abc import ABC, abstractmethod
#
# list1 = [1, 2, 3, 4, 5]
# dict1 = {'value1': 'key1', 'value2': 'key2'}
#
# print(len('salam khoobi?'))
# print(len(list1))
# print(len(dict1))
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# # shape1 = Shape()
#
#
# class Square(Shape):
#
#     def __init__(self, lenght):
#         self.lenght = lenght
#
#     def area(self):
#         return self.lenght ** 2
#
#     def perimeter(self):
#         return self.lenght * 4
#
#     def __str__(self):
#         return f'this is a square with a lenght of {self.lenght}'
#
#     def __add__(self, other):
#         return Square(self.lenght + other.lenght)
#
# class Circle(Shape):
#
#     def __init__(self, radious):
#         self.radious = radious
#
#     def area(self):
#         return 3.14 * self.radious ** 2
#
#     def perimeter(self):
#         return 3.14 * self.radious * 2
#
#
# square1 = Square(4)
# square2 = Square(9)
# circle1 = Circle(3)
#
# square3 = square1 + square2
# def print_shape_area(shape):
#     print(f'Area: {shape.area()}')
#
# print_shape_area(square1)
# print_shape_area(circle1)
#
#
# def add(x, y):
#     return x + y
#
# print(add(4,5))
# print(add('salam ','chetori'))

# print(square3)


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __len__(self):
#         return self.pages
#
#
# class Movie:
#     def __init__(self, title, director, duration):
#         self.title = title
#         self.director = director
#         self.duration = duration
#
#     def __len__(self):
#         return self.duration
#
#
# book1 = Book('Shab haye siah', 'mmd reza jafarpour', 167)
# movie1 = Movie('Shab haye barare', 'mehran modiri', 2)
#
# print(len(book1))
# print(len(movie1))


# Encapsulation

class User:
    def __init__(self, username, password, login=False):
        self.username = username
        self.login = login
        if User.validate_password(password):
            self._password = password
        else:
            raise ValueError('password is not valid')

    #getter
    @property
    def password(self):
        if self.login:
            return self.__password
        return 'user not logged in'

    #setter
    @password.setter
    def password(self, new_password):
        if User.validate_password(new_password):
            self.__password = new_password
        else:
            raise ValueError('password is not valid')


    @staticmethod
    def validate_password(password):
        if len(password) > 7:
            has_lower_ch = False
            has_upper_ch = False
            has_digit = False
            for ch in password:
                if ch.isupper():
                    has_upper_ch = True
                elif ch.islower():
                    has_lower_ch = True
                elif ch.isdigit():
                    has_digit = True
            if has_lower_ch and has_upper_ch and has_digit:
                return True
        return False

    def __str__(self):
        return f'username: {self.username} password: {self._password}'


user1 = User('houtan_tv', "A123456l", True)
# print(user1)
# user1.password = "123"
# user1.email = "houtan@gmial.com"
# print(user1.email)
# user1.password
# user1._password
# user1.__password
# print(user1)
# print(user1.__password)
user1.password = 'B234567c'
print(user1)
