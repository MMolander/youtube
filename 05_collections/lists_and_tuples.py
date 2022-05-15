# List of email strings
emails = [
    "foo@example.com",  #index 0
    "molle@best.com",   #index 1
    "bar@sverige.se",   #index 2
]

index_0 = emails[0]
index_1 = emails[1]
index_2 = emails[2]

print( index_0, index_1, index_2)

# Augmented Assignment
emails += ["bla@bla.com", "hej@dig.se"]
print(emails)

#List concatenation
scores = [1,2,3] + [4,5] + [6]
print("Initial concatenated scores: ", scores)

# modify a list in place!
scores.append(7)
print("scores after appending 7: ", scores)

scores.extend([8, 9])
print("scores after extending [8, 9]: ", scores)

#remove item at index 5
result = scores.pop(5)
print(result)

scores.insert(3, "inserted!")
print(scores)

scores.remove("inserted!")
print(scores)

# Getting the minimum and maximum values of a list
my_list = [100, 200, 300]

list_max = max(my_list)
list_min = min(my_list)
print(f"max value: {list_max} , min value: {list_min}" )

# Slicing lists
# some_list[a:b] => gets just part of the list
# from a to b, non-inclusive of b
steps = [
    "wake up",
    "get out of bed",
    "make coffee",
    "go for walk",
    "start work",
]
print(steps)
print(steps[0:2])
print(steps[0])
print(steps[0:])
print(steps[:3])
print(steps[0:4:2])     # from 0 to 4 taking 2 steps
print(steps[0::1])      # from 0 to the end taking 1 step (full list again)
print(steps[-2])        # Negative numbers are valid

#syntax for reversing a list:
print(steps[::-1])

#reversing a string
print("look at this backwards"[::-1])

#tuples
# tuples are immutable
x = ("foo", "bar", "baz")
y = ["foo", "bar", "baz"]
print(type(x), type(y))

y[0] = "quux"
print (x[::-1])
print(y)