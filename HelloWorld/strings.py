print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = input("Please enter your name ")
print(greeting + name)

# if we want a space, we can add that too. Greeting is a variable
print(greeting + ' ' + name)


age = 24
print(age)

# age here is an integer, greeting is a string. type finds type

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 /  7:12.50f}")

pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")