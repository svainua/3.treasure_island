first_step = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ')
if first_step == "Left".lower():
    second_step = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')
    if second_step == "Wait".lower():
        third_step = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if third_step == "Red".lower():
            print("It's a room full of fire. Game Over.")
        elif third_step == "Blue".lower():
            print("You enter a room of beasts. Game Over.")
        elif third_step == "Yellow".lower():
            print("You found the treasure! You Win!")
        else:
            print("Game Over")
    else:
        print("You get attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")

