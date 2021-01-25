# for i in range(1, 21):
#     print("i is now {}".format(i))

# for number in range(0, 10):
#     print("{}".format(number))    my correct (inefficient) solution

# for i in range(10):
#     print(i)    # better solution

for i in range(0, 10, 2):   # prints up to 10 in 2s
    print("i is now {}".format(i))

print()

for i in range(10, 0, -2):   # prints from 10 to 0 in 2s
    print("i is now {}".format(i))

print()

# This solution uses a step function
for i in range(0, 101, 7):
    print(i)
print()
# This solution uses a slice
for i in range(101)[::7]:
    print(i)

