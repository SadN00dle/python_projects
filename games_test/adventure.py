name = input("What is your name? ")
print(f'Hello {name}, Welcome to the adventure game.'
      f' Choose wisely and follow your destiny!')

answer = input("You're infront of a river. "
               "\nIf you wish to cross it type 'cross'"
               " \nand if you want to go around it type 'skip': ").lower()

if answer == 'cross':
    print("You crossed the river!")
    q2 = input("You meet a villager! "
               "\nType 'talk' to talk to the villager or 'skip' to ignore: ").lower()
    if q2 == 'talk':
        print("Villager: Hello traveler"
              "I am the gatekeeper for the empire and i cannot find my sword."
              "\nWould you help me find my sword. I will be forever grateful to you.")
        q3 = input("Type 'accept' accept the quest."
                   "\n (It is the first quest so you cannot skip this one.) "
                   "\n *Hint: Search along the river bank: ").lower()
        if q3 == 'accept':
            print("Will continue later.....")
        else:
            print("Invalid command!")
    else:
        print("Wrong command! You Lost")
elif answer == 'skip':
    print("You chose to go around the river!")
    print("You found a sword lying in the river bank.")
    q4 = input("A villager approaches you and asks about the sword."
               "\nType 'lie' to lie and 'truth' to tell the truth.").lower()
    if q4 == 'lie':
        print("You are dead!(until further notice)lol.")
    elif q4 == 'truth':
        print("continue in another version.")
    else:
        print("Invalid command!")

else:
    print("Invalid command!")