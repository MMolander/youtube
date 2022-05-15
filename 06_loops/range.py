# Using range()
# range() generates the integer numbers
# between a given start and stop value

#loop 3 times starting at 0
# note that range() doesnt include the last number in the result
for i in range(3):
    print(f"Now we´re in loop number: {i}")


print("---")

#loop 3 times starting at 0
# note that range() doesnt include the last number in the result
for i in range(0, 3):
    print(i)

print("---")
# loop 3 times, starting at 2
# note that range() doesnt include the last number in the result
for i in range(2, 5):
    print(i)

print("---")
# loop 3 times, starting at 3, jumping by 3
# note that range() doesnt include the last number in the result
for i in range(0, 9, 3):
    print(i)