# Functions only runs when called
# Functions can be passed data as parameters
# Functions can return values
# White space in Python is important!


# A simple function
def print_name():
    my_name = "Molle"
    print((my_name))


print_name()


#a function that takes a single parameter



#a function that takes a single parameter
# and returns a value
def get_days_old(age_in_years):
    days_in_year = 365
    return age_in_years * days_in_year

days_old = get_days_old(24)
print(days_old)

# A Function that takes a single parameter
# and calls another function
def print_days_old_report(age_in_years):
    age_in_days = get_days_old(age_in_years)
    report = f"I´m about {age_in_days} days old"
    print(report)

print_days_old_report(37)