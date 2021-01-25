import random

highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = -2   # initialise to any number that doesn't equal the answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("You have quit")
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        if guess > answer:  # guess must be greater than answer
            print("Please guess lower")

        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed it")




# binary search equation: low + (high - low) // 2
# for range of 10 this is: 1  + ( 10  -  1 ) // 2 which gives us 1 plus 4 = 5. integer division rounds down. 9 // 2 = 4










# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You are correct!")


# tree1 = 'put your first tree name here'
# tree2 = 'put your second tree name here'
#
# if tree1 == tree2:
#     print("The trees are the same.")
# else:
#     print("The trees are different.")


# x = 7
# y = 7

# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is smaller than y")
# elif x == y:
#     print("x equals y")
