#                    1         2
#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1] # Idiom for reverse order
print(backwards)
# create a slice that produces the characters qpo
print(letters[16:13:-1])
# slice the string to produce edcba
print(letters[4::-1])
# slice the string to produce the first 8 characters, in reverse order
print(letters[7::-1])
# slice the string to produce the last 8 characters, in reverse order
print(letters[25:17:-1])
print(letters[:-9:-1])

print(letters[-4:])     # Idiom for last indices
print(letters[-1:])
print(letters[:1])      # Idiom for first item in sequence
print(letters[0])

