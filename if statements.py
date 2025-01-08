# this will allow you to check for certain conditions

list_of_users = []

user_one = input("what is your name? ")
list_of_users.append(user_one)

if user_one == "abdus":
    print(f"Hi {user_one}")
else:
    print(f"unknown user recognised")

# can also be used as inequalities
# choosing a player for the team with a certain overall rating

football_players = [
    {"name": "Abdus", "rating": 83, "preference": 5},
    {"name": "Zohaib", "rating": 84, "preference": 7},
    {"name": "Saif", "rating": 88, "preference": 7},
    {"name": "Waj", "rating": 87, "preference": 7},
    {"name": "Haitham", "rating": 88, "preference": 5},
    {"name": "Junaid", "rating": 83, "preference": 5},
]

while True:
    game_input = input("Will it be a 5 or 7 a-side game? ")

    if game_input.isdigit():
        game_to_play = int(game_input)
        if game_to_play == 5 or game_to_play == 7:
            break
        else:
            print("Please use the number 5 or 7 only.")
    else:
        print("Incorrect format, please enter a number.")

lowest_rating = int(input(f"what is the lowest rating you need? "))
highest_rating = int(input(f"what is the highest rating you need? "))

print("Players to use:")
for player in football_players:

    if (lowest_rating <= player["rating"] <= highest_rating
        and player["preference"] == game_to_play):

        print(f'{player["name"]} {str(player["rating"])}')
    else:
        print("None in the directory. Find other people.")

# else is used when you have 2 options
# elif is used when you have many conditions that need to be checked before concluding
