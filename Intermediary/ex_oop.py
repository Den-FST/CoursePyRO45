"""
###################
1. create classes
	a. Person (name, surname, age, phone number), Employee(Person + id, salary, position, responsibilities), Intern(Person, salary, scolarship, menthor)
		employee_list = [
			Employee("solo", "bogdan", 30, "07xxyyyzzz", 1, 5000, "HR", "Recruiting"),
			Employee("bobonete", "mihai", 28, "07xxyyyzzz", 2, 7000, "Sales", "Selling"),
			Employee("bordea", "catalin", 23, "07xxyyyzzz", 3, 8000, "Sales", "Selling"),
			Employee("nae", "nicolae", 45, "07xxyyyzzz", 4, 9500, "Programmer", "Coding"),
			Employee("bendeac", "mihai", 33, "07xxyyyzzz", 5, 7000, "Marketing", "Promoting"),
			Employee("popesco", "cristi", 23, "07xxyyyzzz", 6, 5000, "HR", "Recruiting")
		]

		intern_list = [
			Intern("mincu", "alexandru", 21, "07xxyyyzzz", 2000, 0, "solo"),
			Intern("popovici", "maria", 22, "07xxyyyzzz", 2100, 500, "bobonete"),
			Intern("bojoc", "costel", 23, "07xxyyyzzz", 2200, 700, "bobonete")
		]

	b. sort employee list by salary and intern list by age
	c. print all emplyees from sales department
	d. delete intern "popovici maria" (implement __eq__ function)
	e. implement a polymorfic function that increase the salary by a specific amount. amount is given as a parameter.
	f. increase salary to bobonete, nae and popesco by 1000 and bojoc by 500. print salaries to see if they were increased.
	g. perform a shallow and deep copy for employee bendeac and intern mincu. change the salaries and see the results with print
	h. create an abstract methods inside Person called show_finance(), expenses() - 80% from salary and implement them inside Employee and Intern
	i. create a class method inside Intern class to be able to create objects with this method
	j. create a static method inside Intern class to be able to check if Intern is valid (salary needs to be max. 2500 and needs to have a menthor)
###################

"""
import dataclasses
from abc import abstractmethod
from dataclasses import dataclass
from copy import deepcopy


class Person:
    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        print(f"{self.name} {self.surname}, {self.age} ani si tel: {self.phone_number}")

    @abstractmethod
    def show_finance(self):
        pass

    @abstractmethod
    def expenses(self):
        pass

class Employee(Person):
    def __init__(self, name, surname, age, phone_number, id, salary, position, responsibilities):
        super().__init__(name, surname, age, phone_number)
        self.id = id
        self.salary = salary
        self.position = position
        self.responsibilities = responsibilities

    def expenses(self):
        return f"Expenses: {self.salary * 0.8}"

    def show_finance(self):
        return f"Salary: {self.salary}"


class Intern(Person):
    def __init__(self, name, surname, age, phone_number, salary, scholarship, mentor):
        super().__init__(name, surname, age, phone_number)
        self.salary = salary
        self.scholarship = scholarship
        self.mentor = mentor

    def show_finance(self):
        print(f"Salary: {self.salary}, Scholarship: {self.scholarship}")

    def expenses(self):
        print(f"Expenses: {self.salary * 0.8 + self.scholarship}")

    # @classmethod
    # def from_string(cls,string):
    #     name, surname, age = string.split(",")
    #     return cls(name, surname, age )
    #
    # @classmethod
    # def create_from_string(cls, sentence):
    #     name, age, scholarship = sentence.split()
    #     # age, scholarship = int(age), float(scholarship)
    #     return cls(name, age, scholarship)

    @classmethod
    def create_intern(cls, name, surname, age, phone_number, mentor):
        return print(cls(name, surname, age, phone_number, 2000, 0, mentor))


    @staticmethod
    def is_valid(salary, mentor):
        if salary > 2500:
            return False
        if mentor == "":
            return False
        return True

def main():
    employee_list = [
        Employee("solo", "bogdan", 30, "07xxyyyzzz", 1, 5000, "HR", "Recruiting"),
        Employee("bobonete", "mihai", 28, "07xxyyyzzz", 2, 7000, "Sales", "Selling"),
        Employee("bordea", "catalin", 23, "07xxyyyzzz", 3, 8000, "Sales", "Selling"),
        Employee("nae", "nicolae", 45, "07xxyyyzzz", 4, 9500, "Programmer", "Coding"),
        Employee("bendeac", "mihai", 33, "07xxyyyzzz", 5, 7000, "Marketing", "Promoting"),
        Employee("popesco", "cristi", 23, "07xxyyyzzz", 6, 5000, "HR", "Recruiting")
    ]

    intern_list = [
        Intern("mincu", "alexandru", 21, "07xxyyyzzz", 2000, 0, "solo"),
        Intern("popovici", "maria", 22, "07xxyyyzzz", 2100, 500, "bobonete"),
        Intern("bojoc", "costel", 23, "07xxyyyzzz", 2200, 700, "bobonete")
    ]


# --------------------------- B Sorting  --------------------------------------
    employee_list_sorted_by_salary = sorted(employee_list, key=lambda e: e.salary)
    intern_list_sorted_by_age = sorted(intern_list, key=lambda i: i.age)

    print("Employee List Sorted by Salary:")
    for employee in employee_list_sorted_by_salary:
        print(f"{employee.name} {employee.surname} ({employee.position}): {employee.salary}")

    print("\nIntern List Sorted by Age:")
    for intern in intern_list_sorted_by_age:
        print(f"{intern.name} {intern.surname} (Mentor: {intern.mentor}): {intern.age}")

# --------------------------- Sales dep PRint ----------------------

    print("\nSales department list: ")
    for sales in employee_list:
        if sales.position == 'Sales':
            print(f" {sales.name} {sales.surname} - {sales.position}")

# --------------------------- D Stergem pe popovici ----------------------
    for i, intern in enumerate(intern_list):
        if intern.name == 'popovici':
            del intern_list[i]

# ---------------------------  Print lista interni  ---------------------
    print('\nLista de interni')
    for intern in intern_list:
        print(f"{intern.name} {intern.surname} ({intern.age}): {intern.salary}")

# ---------------------------  Func increase salaries  --------------------------------------
    def increase_salary(obj, amount):
        obj.salary += amount
        # print(f"{obj.name}'s salary increased by {amount}.")

# ---------------------------  Increase salaries  ---------------------------------
    print("\nIncreasd salaries bobonete, nae and popesco by 1000 and bojoc by 500.")
    for i, employee in enumerate(employee_list):
        # Increase salaries
        if employee.name == 'bobonete' or 'popesco' or 'nae':
            increase_salary(employee_list[i], 1000)

    for i, intern in enumerate(intern_list):
        # Increase salaries
        if intern.name == 'bojoc':
            increase_salary(intern_list[i], 500)

    print('\nLista de employes')
    for employee in employee_list:
        print(f"{employee.name} {employee.surname} ({employee.position}): {employee.salary}")

    print('\nLista de interni')
    for interni in intern_list:
        print(f"{interni.name} {interni.surname} {interni.salary}")

# ---------------------------  DeepBlock --------------------------------------
    deep_emp = deepcopy(employee_list)
    deep_int = deepcopy(intern_list)

    print('\nLista deep')
    for i, e in enumerate(deep_emp):
        if e.name == 'bendeac':
            increase_salary(deep_emp[i], 7300)
            print(f"Employee: {deep_emp[i].name} {deep_emp[i].surname} {deep_emp[i].salary}")

    for i, int in enumerate(deep_int):
        if int.name == 'mincu':
            increase_salary(deep_int[i], 7100)
            print(f"Intern: {deep_int[i].name} {deep_int[i].surname} {deep_int[i].salary}")

# ---------------------------  Method intern to create member --------------------------

    Intern.create_intern('Denis', 'Schimbator', 35, "07xxxxx", "Selling")

    print('\nLista de interni')
    for interni in intern_list:
        print(f"{interni.name} {interni.surname} {interni.salary}")

# ---------------------------  end --------------------------------------

if __name__ == "__main__":
    main()