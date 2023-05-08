### Serialization ###
"""
1. pickle module
    a. serialization
    b. deserialization
2. CSV files
    a. read
    b. write
3. JSON files
    a. read
    b. write
"""

import pickle
import csv
import json

def pickle_serialization():

    data = {
        'a': [1, 2.0, 3, 4+6j],
        'b': ("Alice has a cat", "Python is great!"),
        'c': [False, True, False]
    }

    ### context is closing automatically the file ### managing resources properly ###
    with open('files/data.pickle', 'wb') as my_file:
        pickle.dump(data, my_file)


def pickle_deserialization():

    with open('files/data.pickle', 'rb') as my_file:
        data = pickle.load(my_file)

    print("\n\n")
    for key in data:
        print(f"{key}: {data[key]}")

    print("\n\n")


def csv_read_lines():
    
    ### option 1 ###
    with open("files/employees.csv") as my_file:

        reader = csv.reader(my_file)

        for row in reader:
            print(row[1])

        print("\n\n")


    ### option 2 ###
    with open("files/employees.csv") as my_file:

        reader = csv.DictReader(my_file)

        data = {}

        for line in reader:

            name = line["Name"]
            salary = line["Salary"]
            department = line["Department"]

            data[name] = {'salary': salary, 'department': department}


        print(f"{data}\n")

        for key in data:
            print(f"{key}:")

            for key_lvl_2 in data[key]:
                print(f"    - {key_lvl_2}: {data[key][key_lvl_2]}")

            print("\n")

        print("\n\n")


def csv_write_lines():
    
    data = {
        '1': ["solo", "mate-info", 9],
        '2': ["terminator", "filologie", 9.6],
        '3': ["batman", "stiinte", 7.6],
        '4': ["superman", "filologie", 10],
        '5': ["aquaman", "sport", 6.5],
        '6': ["sandokan", "sport", 7.3]
    }

    ### write ###
    with open ("files/students.csv", mode="w", newline='') as out_file:

        writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Name", "Profile", "Grade"])

        for key in data:
            writer.writerow(data[key])


    ### write ###
    with open ("files/students.csv", mode="a", newline='') as out_file:

        writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["songoku", "mate-info", "9.8"])




dogs_and_cats = dict()

def read_json():

    global dogs_and_cats
    
    with open("files/dogs_and_cats.json") as my_file:
        dogs_and_cats = json.load(my_file)


    # print(dogs_and_cats)

    for aninal_type in dogs_and_cats:
        print(f"\n{aninal_type.title()}")

        for aninal in dogs_and_cats[aninal_type]:
            # print(aninal)
            for key in aninal:
                print(f"{key}: {aninal[key]}")

            print("\n")

    print("\n\n")


def write_json():

    global dogs_and_cats
    
    for aninal_type in dogs_and_cats:

        text_file = f"files/{aninal_type}.json"
        with open(text_file, "w") as my_file:
            json.dump(dogs_and_cats[aninal_type], my_file, indent=4)


def main():

    pickle_serialization()
    pickle_deserialization()

    csv_read_lines()
    csv_write_lines()

    read_json()
    write_json()
    

if __name__ == "__main__":
    main()