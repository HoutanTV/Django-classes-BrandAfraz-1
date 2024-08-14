# import time
#
#
# def time_calculator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f'this function --{func.__name__}-- took {execution_time} seconds to complete.')
#         return result
#     return wrapper
#
#
# @time_calculator
# def count_until(number):
#     our_numbers = []
#     for num in range(number):
#         our_numbers.append(num)
#     return our_numbers
#
# count_until(1000000)
#
#
# @time_calculator
# def count_a(inp):
#     count = 0
#     for ch in inp:
#         if ch.lower() == 'a':
#             count += 1
#     return count
#
# jomle = 'ahmad agha rafte sare kooche kharid kone biad'
#
# print(count_a(jomle))
#
#
# @time_calculator
# def factorial(number):
#     output = 1
#     for num in range(2, number + 1):
#         output *= num
#     return output
#
# factorial(100000)

# OOP

# number = 10
#
# print(type(number))
#
# our_list = [10 , 2]
#
# print(type(our_list))


# age = 20
# name = "vanw"
# score = 16

# def show_student_score():
#     pass
#
# student1
#
# class Animal:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#     def make_sound(self,sound):
#         return sound
# #
# animal1 = Animal('pashmak', 'cat')
# animal2 = Animal('jimy', 'dog')
#
# print(animal2.name)
# print(animal1.name)
#
# print(type(animal1))
# print(type(animal2))

#
# print(animal1.make_sound('meow'))

# print(animal1)
# print(animal2)


# constructor -- sazande

class User:
    def __init__(self, username_inp,password_inp , phonenumber_inp, email_inp):
        # instance attributes

        self.username = username_inp
        self.password = password_inp
        self.phonenumber = phonenumber_inp
        self.email = email_inp

    def reset_password(self ,new_password):
        self.password = new_password
        return 'successful'


user1 = User('akbar_56', 'kflvoaom123vnai', '091212345678', 'akbar_56@gmail.com')
print(user1.password)

print(user1.reset_password('voawoevn13nod'))
user1.password = 'voawoevn13nod'
print(user1.password)
