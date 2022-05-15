# Conditional logic
# allow us to make decisions based
# on the truthiness of an expression

if 2 > 1:   # True!
    print("ok")

if 2 < 1:   # False!
    print("OK")    #can never reach
else:
    print("Bar")

# if -> elif -> else
if 2 < 1:   #False
    print("Foo")        #can never reach
elif 2 != 2:     #false
    print("Bar")        #can never reach
else:
    print("Baf")


if 1 < 2 and "a" == "a":
    print("All good")

# an empty list is "Falsy"

errors = []

if not errors:
    print("No errors!")

if not 0:
    print("zero {0} is falsy")

if not None:
    print("None is Falsy")

if not "":
    print("Empty string is falsy")

if not set():
    print("Empty set is Falsy")