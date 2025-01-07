example_tuple = ()
print(type(example_tuple))

person_information = ('James', '22', 'England')

print('What do you want to find out?' )
print('1. Name | 2. Age | 3. Location ')
choice_made = input()

if choice_made == '1':
    print(person_information[0])
elif choice_made == '2':
    print(person_information[1])
elif choice_made == '3':
    print(person_information[2])
else:
    print('No option chosen.')