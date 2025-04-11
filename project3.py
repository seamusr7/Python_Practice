#treasure island game

print("Welcome to Treasure Island")
print("your mission is to find the treasure")

def play_game():
    door1 = input("you have reached a path that leads to 2 doors. which door do you choose? left or right\n")

    if door1 == "left":
        print("you chose correctly, continue down the path\n")
    else:
        print("you were eaten by the boogeyman.\n")
        return

    door2 = input("you have reach another impass, you have two choices over or around the bridge. which do you choose (type over or around)\n")

    if door2 == "over":
        print("you successfully made it throught the shortcut\n")
    else:
        print("you were robbed by bndits and sold into slavery. big rip\n")
        return

    door3 = input("you have reached the final block. there are 3 roads to take, blue, red, yellow. which will you choose?\n")

    if door3 == "blue":
        print("you win! you successfully cleared all the paths and found the treasure!!")
    else:
        print("you lose, better luck next time loserrrrrrrrr hahahahahaha")
        return
play_game()
