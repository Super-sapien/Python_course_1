# activity = input("What would you like to do today? ")
#
# if "cinema" not in activity.casefold():
#     print("But I want to go to the cinema")

name = input("Please enter your name ")
age = int(input("Please enter your age "))
# print("Hello {} who is {} years old".format(name, age))

if 18 <= age < 30:
    print("Welcome club 18-30 holidays, {0}".format(name))
else:
    print("I'm sorry, our holidays are only for cool people")

