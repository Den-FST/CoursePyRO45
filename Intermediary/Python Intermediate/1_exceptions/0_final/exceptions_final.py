### Exceptions ### https://www.youtube.com/watch?v=MImAiZIzzd4 ###
"""
1. AssertionError
2. AttibuteError
3. IOError
4. IndexError
5. ImportError
6. KeyError
7. NameError
8. ValueError
9. ZeroDivisionError
10. Custom Exception
"""

import math

class ExceptieSmechera(Exception):
	pass

try:

	### assertion error ###
	# x = "Hello World!"
	# assert x == "Hello World", "Invalid Text"


	### attribute error ###
	# x = "ceva ceva"
	# x.y = 2


	### io error ###
	# with open("demo.txt", "r") as file:
	# 	my_file_content = file.read()
	# 	print(my_file_content)


	### index error ###
	# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	# print(my_list[0])
	# print(my_list[8])

	### import error ###
	# import solo


	### key error ###
	# students = {'solo': 9, 'bobonete': 10, 'bordea': 7}
	# print(students['solo'])
	# print(students['bogdan'])


	### name error ###
	# print(solo)


	### value error ###
	# print(math.sqrt(-100))


	### zero division error ###
	# a = 1
	# b = 0
	# print(a/b)


	### custom exception ### solo ###
	print("Insert a name:")
	name = input()

	if name == 'solo':
		raise ExceptieSmechera()
	else:
		print(f"{name} is a valid name!")


### the error provided by user gets printed ###
except AssertionError as err:
	print(f"Assertion Error: |{err}|")

except AttributeError as err:
	print(f"Attribute Error: |{err}|")

except IOError as err:
	print(f"IO Error: |{err}|")

except (IndexError, KeyError) as err:
	print(f"Index or Key Error: |{err}|")

except ImportError as err:
	print(f"Import Error: |{err}|")

except NameError as err:
	print(f"Name Error: |{err}|")

except ValueError as err:
	print(f"Value Error: |{err}|")

except ZeroDivisionError as err:
	print(f"ZeroDivision Error: |{err}|")

except ExceptieSmechera:
	print("Name is invalid!")

except:
	print(f"This exception is not defined yet!")


finally:
	print("All exceptions have been handled!")
