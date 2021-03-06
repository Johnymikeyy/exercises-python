# treasure island

print("welcome to treasure island")
print("your mission is to find the treasure")
choice1 = input('you\'re at a crossroad. where do you want to go? write "left" or "right"').lower()

if choice1 == "left":
    choice2 = input("write'wait' to wait the boat. write 'swim' to swim across").lower()
    if choice2 == "wait":
        choice3 = input("which color dou you choose?").lower()
        if choice3 == "red":
            print("there is fire, game over")
        elif choice3 == "yellow":
            print("you found it!")
        elif choice3 == "blue":
            print("game over")
        else:
            print("you chose a door that does not exist, game over")
    else:
        print("game over")
else:
    print("you fell into hole, game over")  