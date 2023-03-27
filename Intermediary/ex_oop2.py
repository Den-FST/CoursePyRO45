"""
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

2. Create a School database using classes
	a. classes: Student, Teacher
	b. functionalities:
	+	i.    create a Student (id, cnp, name, surname, age, address, class_no, profile)
	+	ii.   create a Teacher (id, cnp, name, surname, age, specialty_subject)
	+	iii.  Student should have a grade notebook and we should be able to give a mark to a student at a specific subject
	+	iv.   we should be able to assign a subject to a specific Student
	+	v.    we should be able to assign a class to a specific Teacher
	+	vi.   we should be able to see all the classes a Teacher is assigned to teach
	+	vii.  we should be able to see all the teachers that a Student has
		viii. we should be able to see the AVG(grade) for each subject for each Student and AVG(all_subjects)
		ix.   create a polymorfic function that calculates the Valedictorian for each class_no
		x.    create a polymorfic function that calculates the Valedictorian for the whole school

"""


class Student:
    def __init__(self, id, cnp, name, surname, age, address, class_no, profile):
        self.id = id
        self.cnp = cnp
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.class_no = class_no
        self.profile = profile
        self.notebook = {}
        self.subjects = []
        self.teachers = []

    def add_grade(self, subject, grade):
        if subject in self.notebook:
            self.notebook[subject].append(grade)
        else:
            self.notebook[subject] = []
            self.notebook[subject].append(grade)


    def assign_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)

    def assign_teacher(self, teacher):
        self.teachers.append(teacher)



class Teacher:
    def __init__(self, id, cnp, name, surname, age, specialty_subject):
        self.id = id
        self.cnp = cnp
        self.name = name
        self.surname = surname
        self.age = age
        self.specialty_subject = specialty_subject
        self.class_assigned = []

    def assign_class(self, class_no):
        if class_no is not self.class_assigned:
            self.class_assigned.append(class_no)


    def assign_subject(self, student, subject):
        if subject not in student.subjects:
            student.subjects.append(subject)
        else:
            pass

student_list = [
    Student(0, "987987987", "Denis", "Schimbator", 36, "Cluj", 1, "Real"),
    Student(1, "123456879", "Ion", "Bendeac", 25, "Bucuresti", 3, "Umanist")
]

teacher_list = [
    Teacher(0,"12345678", "Maria", "Popovici", 30, "Matematica"),
    Teacher(1,"98756465", "Ioana", "Popescu", 35, "Chimia")
]

student_list[0].add_grade('mate', 9)
student_list[0].add_grade('mate', 7)
student_list[0].add_grade('Chimia', 8)
student_list[0].add_grade('Chimia', 9)

student_list[1].add_grade('mate', 7)
student_list[1].add_grade('mate', 8)
student_list[1].add_grade('Chimia', 9)
student_list[1].add_grade('Chimia', 10)

student_list[1].assign_subject("Chimia")
student_list[1].assign_subject("Mate")

student_list[0].assign_teacher(teacher_list[1].name)
student_list[0].assign_teacher(teacher_list[0].name)
student_list[1].assign_teacher(teacher_list[1].name)
student_list[1].assign_teacher(teacher_list[0].name)

teacher_list[0].assign_subject(student_list[0], "chimia")
teacher_list[0].assign_subject(student_list[0], "chimia") # for test
teacher_list[0].assign_subject(student_list[0], "Mate")
teacher_list[0].assign_subject(student_list[0], "Mate")   # for test

teacher_list[0].assign_class(1)
teacher_list[1].assign_class(3)





for std in student_list:
    print(f"\n{std.name} {std.notebook}  Obiecte: {std.subjects} Class no:{std.class_no} {std.teachers}\n----------- ")


for tch in teacher_list:
    print(f"\n{tch.name} {tch.surname} - {tch.specialty_subject}, Class assigned: {tch.class_assigned} \n-----------")
