from operator import truediv

boolean_true = True
boolean_false = False

print(boolean_true, boolean_false, type(boolean_true), type(boolean_false))

var_one = 3
var_two = 5

print(var_one==var_two)
print(var_one!=var_two)

print(int(var_one) <= int(var_two))

var_none = None

print(var_none)

#this is used to when something is not there

def print_number(num=None):
    if num is None:
        print("No number provided")
    else:
        print(f"The number is {num}")

print_number()