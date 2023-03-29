"""
### Serialization Task ###

###################
1. Pickle:
	a. create a dictionary with city: population (10 cities)
	b. write data in a file using pickle
	b. read data from file using pickle and print it

2. CSV
	a. create a dictionary with student_name: {grade: "8.6", school: "Gh. Lazar", profile:"mate-info"}
	b. write data inside a csv file (Name | School | Profile | Grade)
	c. read data from csv file and lower the grade with 0.5 for students that their name starts with letter "S"
	d. print data

3. JSON
	a. create a JSON with 10 students: {name:"solo", sex:"M", grade:"8.5"} and 10 cars: {id: 0, model: "Dacia", year: "2022", price: 17000}
	b. write all students in a json and all cars in a json
	c. write a json with students that are boys and a json with students that are girsl and a json with top-students (grade >= 9.5)
	d. write a json with luxury-cars (price >= 70000)
###################
"""
import json
import pickle
import csv

def pickle_serialization_city():

    data = {
        'Bucuresti': 122,
        'Cluj': 75,
        'Craiova': 58,
        'Oradea': 32,
        'Timisoara': 50,
        'Iasi': 78,
        'Suceava': 48,
        'Brasov': 85,
        'Bacao': 72,
        'Pitesti': 67
    }

    with open('files/datacity.pickle', 'wb') as my_file:
        pickle.dump(data, my_file)


def pickle_deserialization_city():
    with open('files/datacity.pickle', 'rb') as my_file:
        data = pickle.load(my_file)

    print("\n\n")
    for key in data:
        print(f"{key}: {data[key]}")
    print("\n\n")



student_data = {
    "1": [ "Ana" , 8.6,  "Gh. Lazar",  "Mate-info"],
    "2": [ "Ion", 7.5,  "Ion Creanga",  "Stiinte Sociale"],
    "3": [ "Alexandru" , 9.2,  "Mih. Sadoveanu", "Filologie"],
    "4": [ "Ioana", 6.8, "Gh. Cosbuc", "Economie"]
}

with open("files/student_data.csv", "w", newline='') as csvfile:

    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Name", "Grade", "School", "Profile"])

    for key in student_data:
        writer.writerow(student_data[key])

# with open("files/student_data.csv", "r", newline='') as csvfile:

def csv_read_lines():


    ################

    with open("files/student_data.csv") as my_file:
        reader = csv.DictReader(my_file)
        data = {}

        for line in reader:
            name = line["Name"]
            grade = line["Grade"]
            School = line["School"]
            Profile = line["Profile"]

            data[name] =  dict()
            data[name]['Grade'] = grade
            data[name]['School'] = School
            data[name]['Profile'] = Profile

        for key in data:
            if key[0] == 'A': #key.startswith('A'):

                rezult = str(float(data[key]['Grade']) - 0.5)
                print(f"{key}, {rezult}: {data[key]['School']} , {data[key]['Profile']}")


        # print(f"{key}:  {rez} : {data[name]['School']}, {data[name]['Profile']}")
        # print("\n\n")




def read_json():

    global studenti

    with open("files/studenti.json") as my_file:
        studenti = json.load(my_file)

    for student in studenti:

        print(f"\n{student.title()}")

        for student in studenti[student]:
            for key in student:
                print(f"{key} - {student[key]}")
            print(student)

    print("\n\n")


def write_json():

    global studenti

    for student in studenti:

        text_file = f"files/{student}.json"
        with open(text_file, "w") as my_file:
            json.dump(studenti[student], my_file, indent=2)

# read_json()
# write_json()
# studenti = dict()

# pickle_serialization_city()
# pickle_deserialization_city()
csv_read_lines()



