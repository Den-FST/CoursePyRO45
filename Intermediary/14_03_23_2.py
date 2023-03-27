import  datetime

def disable_at_night(func):
    def wrapper():
        if 7 <= my_hour < 22:
            func()
    return wrapper

def run_only_between(from = 7, to = 22):
    def decorator(func):
        def wrapper():
            if from_ <= my_hour < to_:
                func()
        return wrapper
### run between 7 - 22
@disable_at_night

@run_only_between(7, 22)

def say_somethong():
    print("\n\nHello WOrld!")
    print("How are you?\n\n")

### run between 14 - 16
@run_only_between(14, 16)
def say_something_else():
    print("Fac ce vreau eu!\n\n")


my_date = datetime.datetime(2023, 3, 14, 22, 30)
my_hour = my_date.hour
print(f"current time: {my_date}")
print(f"current hour: {my_hour}")


