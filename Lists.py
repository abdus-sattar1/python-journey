# values already within a list
list_one = [0, 1, 2, 3, 4, 5]
print('The digits in the list are:', list_one)
print('The total number of digits are', len(list_one))

# removing a value, and assign a variable to it
removed_value = list_one.pop(0)
print(list_one)
print(removed_value)

# we can put it back in if we want
list_one.append(removed_value)
print(list_one)

# as this has been added to the end, we need to change the value of it
list_one[-1] = 6
print(list_one)

#Usually the list is empty and we add to it
list_two = []
list_two.append(1)
list_two.append(1.5)
print(list_two)

#ken method also works for strings

list_three = []
list_three.append('Hello World!')
print(len(list_three[0]))

#storing usernames + passwords

user_database = []
password_database = []

user_database.append(input('Hello, please type in your username: '))
password_database.append(input('Hello,' + ' ' + user_database[0] + ' ' + 'please type in your password: '))

print('1. See more')
print('2. Log out')

choice = input('What would you like to do next? ')
if choice == '2':
    print('See you soon!')
    signed_out_user = input(print('Please type in your username to log in again: '))
    if signed_out_user in user_database:
        input(print("Thank you! Please type your password"))
    else:
        print('Username does not exist!')

# Need a 'class' that I can look back to so that I don't have to repeat code

