#sets are:
# Unordered
# Contains distinct elements
# Contain only hashable types
# - strings, numbers, some collections if their elements are hashable
# NOT dicts or lists, for instance


# Using the set literal syntax
colors_1 = {"blue", "green", "red"}
print(colors_1)

# Use set
user_ids = set([123, 433, 222, 222, 222, 433])
print(user_ids)

number_unique_user_ids = len(user_ids)
print(number_unique_user_ids)

sentence = "Iam learning Python..."
print(set(sentence))

s = {123, False, "foo"}
print(s)

# Union
s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = s1 | s2    # s3 = s1.union(s2)
print("Union of s1 | s2:", s3)

# Intersections
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1 & s2    # s3 = s1.intersection(s2)
print("Intersection of s1 & s2:", s3)

# difference
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1 - s2    # s3 = s1.diffrence(s2)
print("difference of s1 - s2:", s3)

# symmetric difference
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1 ^ s2    # s3 = s1.symmetric.difference(s2)
print("symmetric difference of s1 ^ s2:", s3)

drinks = {"water", "tea", "coffee"}
drinks.add("mineral water")
drinks.remove("water")
# drinks.remove("wine")  #throws an error if "wine" not in set
drinks.discard("wine")   #does nothing if "wine" is not in set
print(drinks)