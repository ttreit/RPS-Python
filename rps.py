### Create a simple rock, paper, scissors game in Python

#import libraries
import random

#Define Functions
def choose_weapon_player():    
    weapon_player = 0
    while weapon_player not in [1, 2, 3]:
        try:
            weapon_player = int(input('Press 1 for Rock \nPress 2 for Paper \nPress 3 for Scissors\n\nSelect your weapon: '))
        except Exception:
            weapon_player = 0
        if weapon_player == 1:
            print('\nYour weapon is a mighty rock!\n')
        elif weapon_player == 2:
            print('\nYour weapon is a smooth piece of paper!\n') 
        elif weapon_player == 3:
            print('\nYour weapon is a pair of sharp scissors!\n')
        else:
            print('\nSorry, that\'s not available, try again.\n')
    return weapon_player

def choose_weapon_computer():
    weapon_computer = random.randint(1, 3)
    if weapon_computer == 1:
        print('Your sworn enemy\'s weapon is a rock!\n')        
    elif weapon_computer == 2: 
        print('The enemy pulls out a piece of paper!\n') 
    elif weapon_computer == 3:
        print('Donald Trump jumps at you with a pair of scissors!\n')                   
    else: 
        print('check for error')
    return weapon_computer

# 1 = rock, 2 = paper, 3 = scissors
def compare_weapons(weapon_player, weapon_computer):
    if weapon_player == weapon_computer:
        print('It\'s a tie!')           
    elif weapon_player == 1 and weapon_computer == 2:
      print('Paper covers Rock\n\nYou Lose!')
    elif weapon_player == 1 and weapon_computer == 3:
        print('Rock smashes scissors!\n\nYou Win!')
    elif weapon_player == 2 and weapon_computer == 3:
      print('Scissors cuts paper.\n\nYou Lose!')
    elif weapon_player == 2 and weapon_computer == 1:
        print('Paper covers rock!\n\nYou Win!')
    elif weapon_player == 3 and weapon_computer == 1:
      print('Rock smashes scissors.\n\nYou Lose!')
    elif weapon_player == 3 and weapon_computer == 2:
        print('Scissors cuts paper!\n\nYou Win!')

##MAIN PROGRAM##
def main():
    player_weapon = choose_weapon_player()
    computer_weapon = choose_weapon_computer()
    compare_weapons(player_weapon, computer_weapon)


if __name__ == '__main__':
    main()
