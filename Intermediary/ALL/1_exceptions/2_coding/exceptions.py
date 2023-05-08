### Exceptions ###
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
"""
import math

try:
	### assertion error ###
	# x = "Hello World!"
	# assert x == "Hello World", "Ala bala portocala"

	### attribute error ###
	# x = "ceva ceva"
	# x.y = 2

	### IO Error ###
	# with open('demo.txt', 'r') as file:
	# 	my_file_content = file.read()
	# 	print(my_file_content)


	### Index Error ###
	my_list = [1, 2, 3, 4]
	print(my_list[3])
	print(my_list[4])

	### import error ###
	# import math
	# import solo

	### Key Error ###
	# students = {'solo': 9, 'bobonete': 10, 'bordea':7}
	# print(students['solo'])
	# print(students['mihaitza'])

	### name error ###
	# print(solo)

	### value error ###
	# print(math.sqrt(-100))

	### zero division error ###
	# a = 1
	# b = 0
	# print(a/b)


except AssertionError as err:
	print(f"\nAssertion Error: {err}\n")

except AttributeError as err:
	print(f"\nAttribute Error: {err}\n")

except IOError as err:
	print(f"\nIO Error: {err}\n")

except (IndexError, KeyError) as err:
	print(f"\nIndex or Key Error: {err}\n")

except ImportError as err:
	print(f"\nImport Error: Either library does not exist or not installed!\n")

except NameError as err:
	print(f"\nName Error: {err}\n")

except ValueError as err:
	print(f"\nValue Error: {err}\n")

except ZeroDivisionError as err:
	print(f"\nZero Division Error: {err}\n")

except Exception as err:
	print(f"\nDefault: {err}\n")

finally:
	print("All exceptions have been handled!")


print("\n\nDONE!\n\n")

