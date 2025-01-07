integer_one =7
integer_two = 4

string_one = '1'
string_two = '2'

print(string_one+string_two)
print(integer_one+integer_two)

print(string_one+str(integer_two))
print(int(string_one)+integer_two)

print(type(string_one))

print((integer_one / integer_two))
print(integer_one % integer_two) # 4 % 7 -> 1, 3
# how many times does the second fit into the first, and then how many are left over


float_one = 1.0
float_two = 2.5

print(float_two+float_one)
print(int(float_one+float_two))