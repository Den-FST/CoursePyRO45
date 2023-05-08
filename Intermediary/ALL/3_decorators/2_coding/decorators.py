### Decorators ###
"""
Decorators in Python are based primarily on two assumptions:
    a. a function may take another function as an argument
    b. you can create a function inside another function
"""

import datetime 


def disable_at_night(func):

    def wrapper():
        if 7 <= my_hour < 22:
            func()

    return wrapper


def run_only_between(from_= 7, to_= 22):

    def decorator(func):
        def wrapper():
            if from_ <= my_hour < to_:
                func()

        return wrapper
    return decorator


### run between 7 - 22 ###
# @disable_at_night
@run_only_between(7, 22)
def say_something():
    print("\n\nHello World!")
    print("How are you?\n\n")


### run between 14 - 16 ###
@run_only_between(14, 16)
def say_something_else():
    print("Fac ce vreau eu!\n\n")



my_date = datetime.datetime(2023, 3, 14, 15, 30)
my_hour = my_date.hour
print(f"current time: {my_date}")
print(f"current hour: {my_hour}")

def main():
    
    say_something()
    say_something_else()

if __name__ == "__main__":
    main()