from functools import reduce

pairs = [(1,10), (2, 9), (3, 8)]

sorted_pairs = sorted(pairs, key=lambda  x: x[1])
sorted_pairs_1 = sorted(pairs, key=lambda  x: reduce(lambda z, y: z+y,x))

min_pairs = min(pairs)
max_pairs = max(pairs, key=lambda x: x[0])
max_pairs1 = max(pairs, key=lambda x: x[1])


print(f"pairs: {pairs}")
print(f"pairs1: {sorted_pairs}")
print(f"pairs2: {sorted_pairs_1}")

print(f"pairs: {min_pairs}")
print(f"pairs: {max_pairs}")
print(f"pairs: {max_pairs1}")

print('\n\n')

students = {
    'solo' : 8.5,
    'bobonete' : 10,
    'popesco' : 7,
    'bordea' : 9
}

list_of_sorted_keys = sorted(students)

pairs_sorted_by_keys = sorted(students.items())
pairs_sorted_by_keys1 = sorted(students.items(), key=lambda x: x[0])
pairs_sorted_by_value2 = sorted(students.items(), key=lambda x: x[1])

dict_sorted_by_keys1 = dict(sorted(students.items()))
dict_sorted_by_keys2 = dict(sorted(students.items(), key=lambda x: x[0]))
dict_sorted_by_value2 = dict(sorted(students.items(), key=lambda x: x[1]))


print(f'list_of_sorted: {list_of_sorted_keys}')
print(f'list_of_sorted_by_keys: {pairs_sorted_by_keys}')
print(f'list_of_sorted_by_keys1: {pairs_sorted_by_keys1}')
print(f'list_of_sorted_by_value2: {pairs_sorted_by_value2}')
print(f'dict_sorted_by_keys1: {dict_sorted_by_keys1}')
print(f'dict_sorted_by_keys1: {dict_sorted_by_keys2}')
print(f'dict_sorted_by_keys1: {dict_sorted_by_value2}')


print('\n\n')




