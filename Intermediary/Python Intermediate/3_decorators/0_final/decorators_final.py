### Decorators ### https://www.youtube.com/watch?v=BE-L7xu8pO4 ###
"""
Decorators in Python are based primarily on two assumptions:
    a. a function may take another function as an argument
    b. you can create a function inside another function
"""

import datetime

def disable_at_night(func):

    def wrapper():
        if 15 <= datetime.datetime.now().hour < 22:
            func()

    return wrapper


def run_only_between(from_=7, to_=22):

    ### a decorator that only calls a decorated function at certain times ###
    def decorator(func):
        def wrapper():
            if from_ <= datetime.datetime.now().hour < to_:
                func()
        return wrapper
    return decorator

# def run_only_when_day_is(day):
#     def decorator(func):
#         def wrapper():
#             if day == my_current_day:
#                 func()
#         return wrapper
#     return decorator

# # my_current_day_name = datetime.datetime.now().strftime("%A") ## Tuesday
# # my_current_day_no = datetime.datetime.now().day     ### 11 if date is 11 march 2023
# # print(f"current_day: {my_current_day_name}")
# # print(f"current_day: {my_current_day_no}")

#@disable_at_night
@run_only_between(14, 16)
def say_something():
    print("Hello world!")
    print("How are you?")


# @run_only_between(7, 22)
@run_only_when_day_is("Tuesday")
def say_something_else():
    print("Fac ce vreau\n\n")

def main():
    
    say_something()
    say_something_else()


if __name__ == "__main__":
    main()