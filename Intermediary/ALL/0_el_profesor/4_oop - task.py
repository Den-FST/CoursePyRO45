### Exception Task ###

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


2. Create a School database using classes
	a. classes: Student, Teacher
	b. functionalities:
		i.    create a Student (id, cnp, name, surname, age, address, class_no, profile)
		ii.   create a Teacher (id, cnp, name, surname, age, specialty_subject)
		iii.  Student should have a grade notebook and we should be able to give a mark to a student at a specific subject
		iv.   we should be able to assign a subject to a specific Student
		v.    we should be able to assign a class to a specific Teacher
		vi.   we should be able to see all the classes a Teacher is assigned to teach
		vii.  we should be able to see all the teachers that a Student has
		viii. we should be able to see the AVG(grade) for each subject for each Student and AVG(all_subjects)
		ix.   create a polymorfic function that calculates the Valedictorian for each class_no
		x.    create a polymorfic function that calculates the Valedictorian for the whole school

###################