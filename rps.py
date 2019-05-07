### Create a simple rock, paper, scissors game in Python

# # Create a way for the user to select their weapon of choice
# # Create a way for the computer to select a weapon
# # Compare the two weapons
# # Determine if the outcome is a tie
# #  - if tie replay
# # Declare the winner
# # Ask to play again

import random

def choose_weapon_player():    
    weapon_player = '0'
    while weapon_player not in ['1', '2', '3']:
        weapon_player = input('Press 1 for Rock \nPress 2 for Paper \nPress 3 for Scissors\n\nSelect your weapon: ')
        if weapon_player == '1':
            print('\nYour weapon is a mighty rock!\n')

        elif weapon_player == '2': 
            print('\nYour weapon is a smooth piece of paper!\n') 

        elif weapon_player == '3':
            print('\nYour weapon is a pair of sharp scissors!\n')

        else:
            print('\nSorry, that\'s not available, try again.\n')
       
def choose_weapon_computer():
    weapon_computer = random.randint(1, 3)
    if weapon_computer == 1:
            print('Your sworn enemy\'s weapon is a rock!\n') #feature - randomize 'your sworn enemy' etc.        

    elif weapon_computer == 2: 
            print('The enemy pulls out a piece of paper!\n') 

    elif weapon_computer == 3:
            print('Donald Trump jumps at you with a pair of sharp scissors!\n')
    
    else: print('check for error')

def main():
    choose_weapon_player()
    choose_weapon_computer()
    print('End of main\n') #test that we completed main


if __name__ == '__main__':
    main()
