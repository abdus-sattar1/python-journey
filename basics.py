# use terminal to run the file, by typing python3 followed by file name

print("hello world and welcome to my journey!")

# I'm going to make everything number related!

number_chosen = int(input("think of a positive number "))
if number_chosen > 0:
    print(f"{number_chosen} is a positive number")
else: print("that is not a positive number!")


user_name = input("Enter name: ")
user_age = input("Enter age: ")

# we can use "" or '' to print a string of letters

print("User's name is " + user_name + " and they are " + user_age + " years old")
print(f"User's name is {user_name} and they are {user_age} years old!")

# f-string is more efficient and quicker

x = 4
y = "Bananas"
z = float(x)

print(x, y)

# by casting you can turn the given variable into a specific data type

print(type(x))
print(type(y))
print(type(z))

x, y, z = 4, "oranges", 5.6
print(x, y, z)
print(x + z)

# global variables | can be used by everything, inside and outside of functions

def func():
    global wont_work_unless_global
    wont_work_unless_global = "global worked!"
    print("User's name was", user_name)

func()
print(wont_work_unless_global)

#it is highlighted in yellow as it is bad practice to utilise global