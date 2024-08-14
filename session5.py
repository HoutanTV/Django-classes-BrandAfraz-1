# inheritance -- abstraction -- polymorphism -- encapsulation

#exception handling




# print('abc' + 5)

# try:
#     num_inp = int(input('enter a number: '))
#     print(10/num_inp)
#
# except ValueError:
#     print('please enter an integer')
#
# except ZeroDivisionError:
#     print('number cannot be divided to 0')

# our_list = [1, 2, 3]
#
# print(our_list[3])

#valueerror  typeerror


# print('salam' + 5)

# student teacher --> user


class User:
    def __init__(self, first_name, last_name, email, password, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if User.validate_password(password):
            self._password = password
        else:
            raise ValueError('invalid password')
        self.age = age

        # getter
    @property
    def password(self):
        return "password can't be printed"

    # setter
    @password.setter
    def password(self, new_password):
        if User.validate_password(new_password):
            self._password = new_password
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
        return f'{self.first_name} {self.last_name}'


class Student(User):
    def __init__(self, first_name, last_name, email, password, age, average):
        super().__init__(first_name, last_name, email, password, age)
        self.average = average


class Teacher(User):

    def login(self, email, password):
        if email == self.email and password == self._password:
            return True
        return False

    @staticmethod
    def set_scores(student, *args):
        if isinstance(student, Student):
            sum = 0
            for score in args:
                if score >20 or score<0:
                    raise ValueError('scores should be between 0 to 20')
                sum += score
            average = sum / len(args)
            student.average = average
        else:
            raise TypeError('student obj is not correct')


# user1 = User('houtan','tv','houtantv@gmail.com','A123456l',15)
# print(user1)
student1 = Student('houtan','tv','houtantv@gmail.com','A123456l',15, 16.22)
teacher = Teacher('mmd', 'mehdipour', 'mmd5436@gmail.com', 'sakoiwM2', 50)


teacher.set_scores(student1,5, 6 , 15, 20)
print(student1.average)

teacher_email = input('Email: ')
teacher_password = input('Password: ')

if teacher.login(teacher_email, teacher_password):
    scores = []
    while True:
        teacher_inp = input('please enter score or done: ')
        if teacher_inp == 'done':
            break
        else:
            scores.append(int(teacher_inp))
    teacher.set_scores(student1, *scores)
else:
    print('login failed')


print(student1.average)

# my_list = ['fja', 5, 4, 'ajsdio']
# print(*my_list)
# my_dict = {'key1': 'value1', 'key2': 'value2'}
#key1=value1, key2=value2