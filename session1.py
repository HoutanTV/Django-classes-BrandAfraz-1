# if condition:
#     #code block

# user_inp = int(input('please enter the number: '))
#
# if user_inp > 9:
#     print('salam')
# elif user_inp == 7:
#     print('number is 7')
# else:
#     print("i don't know")


# for item in items:
#     #code block

# for num in range(1,11):
#     print(f'the number is {num}')
#

# while condition:
#     #code block

# user_guess = ''
# attempts = 0
#
# while user_guess != 'salam':
#     user_guess = input('enter something: ')
#     if user_guess == 'salam':
#         print('well done')
#         break
#     attempts += 1
#     print(f'wrong guess \nattempts:{attempts}')

# def function_name(arguments):
#     #code block
#     return # something

# def greet(name):
#     print(f'hello {name}')
#     return name

# print(greet('houtan'))

# def greet1(name):
#     print(f'hello {name}')
#
# def greet2(name):
#     return name

# greet1('mmd')
# print(greet1('mmd'))

# greet2('mmd')
# print(greet2('mmd'))

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(10))

# 1 1 2 3 5


# argument and keyword arguments

#positional arguments
# def describe_animal(animal, breed=None):
#     if animal == "bird" and breed !='kalagh':
#         return 'jik jik'
#     elif animal == 'cat':
#         return 'meow'
#     return 'unkonwn animal'

# print(describe_animal('bird', 'gonjeshk'))

# print(describe_animal(breed='kalagh', animal='bird'))

# variable-length arguments
# def pizza_topping(*toppings):
#     for topping in toppings:
#         print(topping)
#
# pizza_topping('goje', 'zeytoon')

#keyword variable-length arguments
# def user_info(phonenumber, *hobbies, **info):
#     print(f"phonenumber : {phonenumber}")
#     print('user hobbies are:')
#     for hobby in hobbies:
#         print(hobby)
#     for key, value in info.items():
#         print(f"{key} : {value}")
#
# user_info(912111112 ,'swimming', 'footbal', 'game',firstname='mmd', lastname='mohammadi', age='25', email='mmd@gmail.com')


#decorators

def decorator(func):
    def wrapper(*args, **kwargs):
        #do something
        func(*args, **kwargs)
        #do something
        return None
    return wrapper

def save(func):
    def wrapper():
        func()
        print('saved')

    return wrapper

@save
def say_hello():
    print('hello world')
say_hello()


def say_goodbye():
    print('goodbye')
# say_goodbye()
# print('saved')


#...