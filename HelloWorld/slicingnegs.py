#                   1
#         01234567890123
parrot = "Norwegian Blue"

print(parrot[0:6])      # Norweg
print(parrot[-14:-8])   # Norweg

print(parrot[-4:2])     # can't go backwards from starting position

print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl

print(parrot[-8:14])    # ian Blue

# Steps in a slice. Number after 2nd colon is for steps, print index from 0-6 in steps of 2
print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

# Slice starts on first character, then carries on every 5 steps
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

