#                   1
#         01234567890123
parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg - slicing up to but not including index 6
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])   # start value defaults to start of sequence


print(parrot[10:14])
print(parrot[10:])  # end value defaults to end of sequence. still need colon for slicing

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])    # slice start at beginning and end at end

letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[1:25])


