### OOP ###
"""
1. Inheritance + Multiple Inheritance --- MRO -> Method Resolution Order - it is a concept used in inheritance
2. Polymorphism
3. Abstract Method 
4. class and static methods
5. dataclass
6. deep and shallow copy
"""

from abc import abstractmethod
from copy import deepcopy
from dataclasses import dataclass

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def show_finance(self):
        pass

    ### print method ###
    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):

    def __init__(self, name, age, rate, num_of_hours):
        Person.__init__(self, name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours


    def show_finance(self):
        return self.rate * self.num_of_hours


    def __str__(self):
        return f"{self.name} is {self.age} years old and finance: {self.show_finance()}"


@dataclass()
class Student(Person):

    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship


    def show_finance(self):
        return self.scholarship


    @classmethod
    def create_from_string(cls, sentence):
        name, age, scholarship = sentence.split()
        age, scholarship = int(age), float(scholarship)

        if cls.is_name_correct(name):
            return cls(name, age, scholarship)


    @staticmethod
    def is_name_correct(name):
        if name[0].isupper() and name[1:].islower():
            return True

        return False


    # def __eq__(self, obj):
    #     if isinstance(obj, Student) and self.name == obj.name:
    #         return True

    #     return False

class WorkingStudent(Employee, Student):

    def __init__(self, name, age, rate, num_of_hours, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hours)
        Student.__init__(self, name, age, scholarship)


    def show_finance(self):
        return self.rate * self.num_of_hours + self.scholarship


class Somer(Person):
    def __init__(self, name, age, ajutor_somaj):
        super().__init__(name, age)
        self.ajutor_somaj = ajutor_somaj


    def show_finance(self):
        return self.ajutor_somaj



def check_finance(obj):
    print(f"{obj.name}: {obj.show_finance()}")


def main():

    
    obj_1 = Person("John", 54)      ### instantiere
    obj_2 = Employee("Jack", 36, 20, 160)
    obj_3 = Student("Agatha", 22, 1000)
    obj_4 = WorkingStudent("Monica", 24, 9.5, 70, 550)
    obj_5 = Somer("solo", 16, 700)
    obj_6 = Student("Monica", 21, 1100)
    # obj_7 = Student("solo", 17, 600)
    obj_7 = Student.create_from_string("Solo 17 600")



    print("\n\n")
    print(obj_1)
    print(obj_2)
    print(obj_3)
    print(obj_4)
    print(obj_5)
    print(obj_7)
    print("\n\n")

    check_finance(obj_3)
    check_finance(obj_4)
    check_finance(obj_5)

    print("\n\n")

    a = 10
    b = 20
    a = b + 10

    b = b+10

    print(a)
    print(b)

    my_list = [1, obj_5, 3]
    shallow_copy = my_list
    deep_copy = deepcopy(my_list)


    my_list[1].name = 'bogdan'
    shallow_copy[1]. age = 25
    print(f"my_list: {my_list[1]}")
    print(f"shallow_copy: {shallow_copy[1]}")
    print(f"deep_copy: {deep_copy[1]}")

    print("\n\n")

    print(a == b)
    print(obj_3 == obj_6)

    print("\n\n")


if __name__ == "__main__":
    main()