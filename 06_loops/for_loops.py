# mindful loop

things_i_see = ["computer", "plant", "window"]

for thing in things_i_see:
    print(thing)

#In Python, for loops:
# - Iterate over a sequence
# - list, tuples, dics, string
# think of as "for each element in iterable
numbers = [1, 34, 54, 24]

total_sum = 0

for n in numbers:
    total_sum += n
    print(total_sum)

# Looping over a dict

user = {
    "name" : "foo",
    "age" : 64,
    "email" : "foo@se.se",
}

for key in user:
    print(f"{key}\t -> \t {user[key]}")