import sys


# string = "Textul meu"
#
# str1 = string.encode("utf-8")
# str2 = str1.decode("utf-8")

# print(" Encoded: ", str1, "\n", "Decoded: ", str2)
# print(ascii("abcdefg"))
# print(ascii("jalepeño"))
# print(bin(50))                  #BINARY
# print(bytes("🐍", "utf-8"))  #bytes()
# print(chr(97), chr(7048))
# print(ord("a"))


# print("What", "for","beautiful", "day", ".", sep="-")
# print('1','2','3',4,5, sep = "<")
# name = 'Bob'
# print('Hello,'f"{name}")

# hello = "Hello, World!"
# print(hello[7:12])  # Returns World

# hello = "Hello, World!"
# print(hello[::-1])  # Returns "!dlroW ,olleH"
#
# hello = "Hello, World!"
# print(hello.upper())  # Returns HELLO, WORLD!
#
# hello = "Hello, World!"
# print(hello.lower())  # Return hello, world!
#
# hello = "Hello, World!"
# print(hello.replace('l', 'Z'))  # Returns HeZZo, WorZd!

# alphabet = ['a', 'b', 'c', '...', 'z']
# print(f"The first letter of the alphabet is '{alphabet [0]}'.")
# print(f"And the last letter of the alphabet is '{alphabet [-1]}'.")
# alphabet = ['a', 'b', 'c']
# alphabet.sort()
# print(f"Alphabet (sorted): {alphabet} (length: {len(alphabet)})")
# print("Index:[2] ", alphabet[2])
# print(alphabet.reverse())

# phonebook = {"John": 111111111, "Jack": 222222222}
#
# # We remove items
# del phonebook["John"]
# print(phonebook)
# phonebook.pop("Jack")
#
# print(phonebook)

#
# # Creates a set
# animals = {"dog", "cat", "elephant"}
#
# # Adds a new item (equivalent to append() in lists)
# animals.add("mouse")
#
# # Adds several items at once (equivalent to extend() in lists)
# animals.update(["bird", "horse"])
#
# # Adds the same item again
# animals.add("mouse")
# print(animals)
#
# # Removes the item. Python returns an error if it is not in the set
# animals.remove("cat")
#
# # Removes the item. Python will NOT return an error if it is not in the set
# animals.discard("cat")
# print(animals)
# print(len(animals))  # len can also be used with sets




# x1 = {1, 2, 3}
# x2 = {2, 3, 4, 5, 6}
#
# print(x1 & x2)  # Displays {2, 3}
# print(x1.intersection(x2))  # Will display {2, 3}
# print(x2.intersection(x1))  # Same as above
#
# print(x1 | x2)  # Displays {1, 2, 3, 4, 5, 6}
# print(x1.union(x2))  # will display {1, 2, 3, 4, 5, 6}
# print(x2.union(x1))  # Same as above
#
# print(x1 - x2)  # Will display {1}
# print(x1.difference(x2))  # will display {1}
# print(x2.difference(x1))  # will display {4, 5, 6}

#--------------------------------------------------

# print("Hello.")
# user_name = input("What is your name: ")
# print(f"Hi, {user_name}!")

# age = input("How old are you: ")
# #age += "1"  # ERRRRRROR! age is a string, we try to add number and word!
# print("Next year you will have...")
# print(age)
# print("... years.")

# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

# x = 0
# y = 3
#
# if x > y:  # This will be translated to False because 0 is not greater than 3
#     print(f"{x} is greater than {y}")  # This will not be displayed
#
# if x < y:  # This will be translated to True because 3 is greater than 0
#     print(f"{x} is less than {y}")  # This will be displayed


# userage = input("How old are you: ")
# age = int(userage)
# if age < 15:
#     print("You are adolescent")
# elif age < 25:
#     print("var2")
# elif age  < 35:
#     print("var3")
# else:
#     print("alta")

# # Execute until n is lower than 5
# n = 0
# while n < 5:
#     n += 1  # increment n in every next loop
#     print(n)
#
# animals = ["Dog", "Cat", "Fish"]
#
#     # Write all animals from the list
# for animal in animals:
#     print(animal) # Write one animal one by one

#
# for i in range(3):
#     print(i)



# def print_hello_world():
#     print("Wlcome to the world of funcntio")
#
# print_hello_world()


# def greet_by_name(name):
#     print(f"Hi, {name}")
# # Function call greet_by_name(name) use the value "John" as the argument name
# greet_by_name("John")

# def print_hello(text: str) -> None:
#     print(f"Hello {text}")
# print_hello("you")

# def calculate_square(a):
#     return a * a
# square = calculate_square(5)
# print(square)  # Return 25

# Add any number of arguments
# def add(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
#
# print(add(1, 2, 3, 4, 5))  # Return 15
#
#
# # Return name and anything else the user provides
# def print_name_and_something(name, *strings):
#     print(f"Name: {name}")
#     for string in strings:
#         print(string)
#
#
# print_name_and_something("Jack", "a", "b", "c", "d")

# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self.name = name
#         self.age = age
#
#     def __len__(self):
#         return self.age
#
#
# print(Animal("Alex", 3))


# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self._name = name
#         self._age = age
#
#
# my_dog = Animal()
# print(my_dog._age)  # it works, will print value of name variable, from my_dog object


