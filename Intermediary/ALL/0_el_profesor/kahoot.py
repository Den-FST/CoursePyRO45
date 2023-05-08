
from timeit import timeit

code = """
from time import sleep

def method():
	sleep(1)

method
"""

print(timeit(code, number=1))
print("/n/n")




import re
sum = 0
pattern = 'back'

if re.match(pattern, 'backup.txt'):
	sum += 1

if re.match(pattern, 'text.back'):
	sum += 2

if re.search(pattern, 'backup.txt'):
	sum += 4

if re.search(pattern, 'text.back'):
	sum += 8

print(sum)
print("/n/n")





param = (i*i for i in range(5))
print(type(param))
print("/n/n")




a = [1, 2]
b = [x**2 for x in a if x<2]
print(b)
print("/n/n")


lower_text = lambda x: x.upper()
print(lower_text("THIS IS A trap!"))
print("/n/n")
