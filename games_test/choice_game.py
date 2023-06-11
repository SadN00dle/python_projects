import random

to_be_chosen = ['rias', 'akeno', 'power']


def char_choice():
    while True:
        print("choose from: rias/akeno/power")

        user_chosen = input("What is your choice? ").lower()
        if user_chosen in to_be_chosen:
            com_choice = random.choice(to_be_chosen)
            print(f"{com_choice} was drawn")
            if user_chosen == com_choice:
                print(f"you acquired {user_chosen}")

                # card score tab

                rias_card = 0
                akeno_card = 0
                power_card = 0

                if user_chosen == "rias" and com_choice == "rias":
                    rias_card += 1
                    print(f"your total rias card are {rias_card}")
                if user_chosen == "akeno" and com_choice == "akeno":
                    akeno_card += 1
                    print(f"your total akeno card are {akeno_card}")
                if user_chosen == "power" and com_choice == "power":
                    power_card += 1
                    print(f"your total power card are {power_card}")

                break
            else:
                print("Try again!")

        else:
            print("Only a single given character should be chosen")
    return user_chosen

char_choice()



