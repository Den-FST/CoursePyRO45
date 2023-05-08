### Decorators Task ###

###################
1. create a main function that calls the following functions:
	a. eat breakfast (everyday between 8-10)
	b. eat lunch (everyday between 13-15)
	c. eat dinner (everyday between 18-20)
	d. go to work (everyday between 9-11)
	e. clean apartment (every saturday)
	f. have fun (every sunday)
	g. pay bills (every month on 1st and 15th)
	h. create a global variable that we can manually enter the date that simulate datetime.now()


2. create a dictionary with the following categories:
	a.	create the same functions that we have at ex. 1 (above)
	b.	activity_feeling = {
			'breakfast': 'eating and feeling good!'
			'lunch': 'eating and feeling good!'
			'dinner': 'eating and feeling good!'
			'go to work': 'I feel like sleeping and do nothing all day BUT I NEED TO WORK!'
			'clean apartment': 'I wish I could afford a maid!'
			'have fun': 'This is the life I deserve!'
			'pay bills': 'Being poor sucks!'
		}

	c. print on the screen the message for each function when it the function is called. USE a decorator for this.


###################
import datetime

now = datetime.datetime(2023, 3, 15, 14)
def eat_breakfast():
	print("I'm eating breakfast")