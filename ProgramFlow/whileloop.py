# for i in range(10):
#     print("i is now {}".format(i))

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1  # same as i = i + 1

# for i in range(0, 100, 7):
#     if i > 0 and i % 11 == 0:
#         break
#     print(i)

# write a program to print out all numbers from 0 - 20 that aren't divisible by 3 or 5 (using continue)

for x in range(21):
    if (x % 3 == 0) or (x % 5 == 0):
        continue
    print(x)

# without continue

# for i in range(21):
#     if i % 3 and i % 5:
#         print(i)
