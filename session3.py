# OOP concepts: inheritance - abstraction - polymorphism - encapsulation

# class Car:
# # class attributes
#     wheels = 4
#
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#
#     # def wheel_count(self, new_wheels):
#     #     self.wheels = new_wheels
#     #     return new_wheels
#
#     @classmethod
#     def wheel_count(cls, new_wheels):
#         cls.wheels = new_wheels
#         return new_wheels
#
#     @staticmethod
#     def taarif(jomle):
#         print('beautiful car', jomle)

#
# car1 = Car('Saipa', 'Pride')
# car2 = Car('Honda', 'Acord')
#
# Car.wheel_count(3)
# print('Car.wheels:')
# print(Car.wheels)
# print('car1:')
# print(car1.make, car1.model, car1.wheels)
# print('car2:')
# print(car2.make, car2.model, car2.wheels)
# Car.taarif('very good')


# inheritance

# parent class
# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def get_details(self):
#         return f'Name: {self.name}, ID: {self.id}'
#
#     def pay(self):
#         return 500
#
#
# employee1 = Employee('Ali', 1)


# print(employee1.get_details())


#child class
# class FixEmployee(Employee):
#     def __init__(self, name, id, yearly_salary=1200):
#         super().__init__(name, id)
#         self.yearly_salary = yearly_salary
#
#     #over riding a method
#     def pay(self):
#         return self.yearly_salary / 12
#
#
# fix_employee1 = FixEmployee('Reza', 2, 240000)


# print(fix_employee1.get_details())
# print(fix_employee1.pay())


#child class
# class HourlyEmployee(Employee):
#     def __init__(self, name, id, hours_worked, hourly_rate):
#         super().__init__(name, id)
#         # Employee('Ali', 1)
#         self.hours_worked = hours_worked
#         self.hourly_rate = hourly_rate

    #over riding a method
#     def pay(self):
#         return self.hours_worked * self.hourly_rate
#
#
# hourly_employee1 = HourlyEmployee('houtan', 3, 10.5, 100)
#
# print(hourly_employee1.get_details())
# print(hourly_employee1.pay())


#Abstraction

#shape -- area -- perimeter

#circle
#rectangle
#square

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

shape1 = Shape()


class Square(Shape):

    def __init__(self, lenght):
        self.lenght = lenght

    def area(self):
        return self.lenght ** 2

    def perimeter(self):
        return self.lenght * 4


class Circle(Shape):

    def __init__(self, radious):
        self.radious = radious

    def area(self):
        return 3.14 * self.radious ** 2

    def perimeter(self):
        return 3.14 * self.radious * 2

square1 = Square(2)
# print(square1.area())

circle1 = Circle(5)
print(circle1.area())
print(circle1.perimeter())