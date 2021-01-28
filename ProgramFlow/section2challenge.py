# print number of options, and allow user to select an option from list
# options should be numbered from 1-9. Program should continue looping
# allowing user to choose one of options each time around
# loop should only terminate when the user chooses 0
# if user makes valid choice, program should print message
# including value they typed. Modify program so menu is printed again
# if they choose invalid option, without duplicating lines

# print("Please choose your option from the list below:")
# options = "1.\tLearn Python \n2.\tLearn Java \n3.\tGo swimming\
#           \n4.\tHave dinner \n5.\tGo to bed \n0.\tExit"
# print(options)

# print("Please choose your option from the list below:")
# print("1:\tLearn Python")
# print("2:\tLearn Java")
# print("3:\tGo swimming")
# print("4:\tHave dinner")
# print("5:\tGo to bed")
# print("0:\tExit")

choice = "-"
while choice != "0":
    if choice in ("1", "2", "3", "4", "5"):
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()

# all code below is wrong

# options_list = [1, 2, 3, 4, 5, 0]
#
#
# chosen_option = ""
# for i in range(int(options_list)):
#     if options_list != chosen_option:
#         print(input("Please choose an option from the list above: ").casefold())
#     elif chosen_option == 0:
#         print("You have quit")
#         break
#
#     else:
#         print("You have chosen " + "{}".format(python, java, swim, dinner, bed, exit))
#         print(input("Please choose another option: ").casefold())


# for chosen_option in options_list:
#     if chosen_option == 0:
#         break
#     options_list = input("Please choose an option from the list above: ")
#     print("You have chosen {}".format(chosen_option))

