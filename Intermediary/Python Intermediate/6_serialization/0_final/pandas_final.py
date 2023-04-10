### Pandas ### https://pandas.pydata.org/docs/reference/general_functions.html ###

import pandas

### csv example ###
# my_data = {
#     '1': ['solomon', 'Gh. Lazar', 9.2],
#     '2': ['bobonete', 'O. Goga', 10],
#     '3': ['popesco', 'Brukenthal', 9.8]
# }

### pandas example ###
my_data = {
    'Name': ['solomon', 'bobonete', 'popesco', 'songoku', 'rambo'],
    'School': ['Gh. Lazar', 'O. Goga', 'Brukenthal', 'Ghibu', 'Gh. Lazar'],
    'Grade': ['9.2', '10', '9.8', '9.7', '8'],
}

def write_csv():

    global my_data

    df = pandas.DataFrame(my_data)
    df.to_csv("files/pandas_example.csv", index = False)


def read_csv():
    
    ### reads and get DataFrame ###
    employees = pandas.read_csv("files/employees.csv")


    print("\n\nNormal DataFrame:")
    print(type(employees))
    print(employees)


    print("\n\nTo String:")
    employees_to_string = employees.to_string(index = False)
    print(type(employees_to_string))
    print(employees_to_string)


    print("\n\n\n\nGroup By:")
    group_by_department = employees.groupby('Department')

    print("\nSales Team:")
    print(group_by_department.get_group('Sales'))

    
    group_by_department_and_seniority = employees.groupby(['Department', 'Seniority'])
    print("\nGroups KEYS:")
    print(group_by_department_and_seniority.groups.keys())

    print("\n\nSeniors from Sales Team:")
    print(group_by_department_and_seniority.get_group(('Sales', 'Senior')))




def main():

    read_csv()
    write_csv()


if __name__ == "__main__":
    main()