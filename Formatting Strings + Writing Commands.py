# writing comments help describe purpose

list_of_users = []

name_one = "Abdus"
age_one = 28 + (355/365)
phone_number_one = 7712345678

name_two = "John"
age_two = 33 + (245/365)
phone_number_two = 7787654321

print("name:", name_one, "age:", age_one)

# cleaner way of doing it
print(f"name: {name_one} age: {age_one}")

# can also be saved as a variable
user_one = f"name: {name_one} age: {age_one:.2f} His phone number is {phone_number_one:011d}"
list_of_users.append(user_one)
user_two = f"name: {name_two} age: {age_two:.2f} His phone number is {phone_number_two:011d}"
list_of_users.append(user_two)

# this is extremely useful for any string output that needs to be repeated
print(user_one, user_two)

# putting it into a list might be easier
print(list_of_users[0:2])

# your code should be clear enough to see what's going on - comments should only be here to describe why something is the way it is

# can also split comments
# like this

# can also be used as a reminder to do something later but shouldn't have too many
# be careful with using too many, code should be self-explanatory
