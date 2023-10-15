"This code is all about Functions"


def hello_func_pass():
    pass


print(hello_func_pass())


def hello_func():
    print("Hello Function!")


hello_func()


def hello_func_return():
    return 'Hello Function Return!'


print(hello_func_return())


def hello_function_required_parameter(greeting):
    return f"{greeting} Function."


print(hello_function_required_parameter("Hi"))


def hello_function_notrequired_parameter(greeting, name="You"):
    return f"{greeting}, {name}."


print(hello_function_notrequired_parameter("Hi"))
print(hello_function_notrequired_parameter("Hi", name='Masoud'))


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leep(year):
    "Return True for leap year, False for non-leap years."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    "Return number of days in that month in that year."
    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and is_leep(year):
        return 29
    return month_days[month]


print(days_in_month(2017, 2))
print(days_in_month(2000, 2))
