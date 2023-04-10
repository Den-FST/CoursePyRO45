### Lambda Expressions ###
"""
The lambda expression is an anonymous function. 
It has no name and is defined where it is used. It does not use the def keyword.
"""

### lower, upper text and title text ###
lower_text = lambda x: x.lower()
upper_text = lambda x: x.upper()
title_text = lambda x: x.title()

print(lower_text("HEHEHEHE"))
print(upper_text("wow!"))
print(title_text("solomon ionut bogdan"))
print("\n\n")

### power^2 and equals ###
square_lambda = lambda x: x*x
equals_lambda = lambda x,y: x==y

print(square_lambda(4))
print(equals_lambda("abc", "bca"))
print(equals_lambda("abc", "abc"))
print(equals_lambda(4, 4))
print("\n\n")


### map, reduce, filter ###
items = [1, 2, 3, 4, 5]

square_1 = map(lambda x: x**2, items)
square_2 = list(map(lambda x: x**2, items))

odds_1 = filter(lambda x: x%2 == 1, items)
odds_2 = list(filter(lambda x: x%2, items))

print(f"square_1: {square_1}")
print(f"square_2: {square_2}")

print(f"odds_1: {odds_1}")
print(f"odds_2: {odds_2}")


from functools import reduce
item_sum = reduce(lambda x,y: x+y, items)
print(f"sum: {item_sum}")

print("\n\n")



### sorted, max, min ###
pairs = [(1, 10), (2, 7), (3, 3)]

sorted_pairs = sorted(pairs, key=lambda x: x[1])
sorted_pairs_1 = sorted(pairs, key=lambda x: reduce(lambda z,y: z+y, x))

min_pairs = min(pairs)

max_pairs_0 = max(pairs, key=lambda x: x[0])
max_pairs_1 = max(pairs, key=lambda x: x[1])

print(f"pairs: {pairs}")
print(f"sorted_pairs by x[1]: {sorted_pairs}")
print(f"sorted_pairs by sum: {sorted_pairs_1}")

print(f"min_pairs: {min_pairs}")

print(f"max_pairs_0: {max_pairs_0}")
print(f"max_pairs_1: {max_pairs_1}")

print("\n\n")



students = {
	'solo': 8.5,
	'bobonete': 10,
	'popesco': 7,
	'bordea': 9
}

list_of_sorted_keys = sorted(students)

pairs_sorted_by_keys_1 = sorted(students.items())
pairs_sorted_by_keys_2 = sorted(students.items(), key=lambda x: x[0])
pairs_sorted_by_value = sorted(students.items(), key=lambda x: x[1])

dict_sorted_by_keys_1 = dict(sorted(students.items()))
dict_sorted_by_keys_2 = dict(sorted(students.items(), key=lambda x: x[0]))
dict_sorted_by_values = dict(sorted(students.items(), key=lambda x: x[1]))


print(f"list_of_sorted_keys: {list_of_sorted_keys}")
print(f"pairs_sorted_by_keys_1: {pairs_sorted_by_keys_1}")
print(f"pairs_sorted_by_keys_2: {pairs_sorted_by_keys_2}")
print(f"pairs_sorted_by_value: {pairs_sorted_by_value}")
print(f"dict_sorted_by_keys_1: {dict_sorted_by_keys_1}")
print(f"dict_sorted_by_keys_2: {dict_sorted_by_keys_2}")
print(f"dict_sorted_by_values: {dict_sorted_by_values}")


print("\n\n")