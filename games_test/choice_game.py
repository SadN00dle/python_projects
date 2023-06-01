import random

MAX_NUMBER = 3
to_be_chosen = ['rias', 'akeno', 'power']

def char_choice():
    while True:
        character_list = print ("choose from: rias/akeno/power")
        user_chosen = input("What is your choice? ").lower()
        to_be_chosen = ['rias', 'akeno', 'power']
        if user_chosen in to_be_chosen:
            print("verified")
            break
        else:
            print("Only a single given character should be chosen")
    return user_chosen

def computer_choice():
    com_choice = random.choice(to_be_chosen)
    print(com_choice)

def get_amount_to_bet():
    while True:
        user_bet = input(f"enter the amount of bet on (1 - {str(MAX_NUMBER)}): ")
        if user_bet.isdigit():
            user_bet = int(user_bet)
            if 1 <= user_bet <= MAX_NUMBER:
                break
            else:
                print("enter a valid number.")

        else:
            print("please enter a number.")
    return user_bet



def main():
    collect = char_choice()
    while True:
        number = get_amount_to_bet()
        total_token = 1
        if total_token < number:
            print(f"not enough token, total_token = {total_token}")
        else:
            break

    print(f"You chose {collect} and betting {number}.")

    print(collect, number)



main()
