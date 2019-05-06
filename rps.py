### Create a simple rock, paper, scissors game in java script

#Add Welcome messaage
#1.1 Ask user how many games they'd like to play (best 3 out of 5 etc)
#Ask user to select rock, paper, or scissors
#Press 1 for Rock <br>Press 2 for Paper<br>Press 3 for Scissors");
#Get the input from the user
#Show them their selection
#Have computer randomly select rock, paper, or scissors
#Display computer selection
#Determine outcome
    #paper beats rock, rock beats scissors, scissors beats paper
#Display win, lose, tie message
#Ask if user wants to play again
#Have option to list the rules of the game

def choose_weapon():
    weapon = input('Press 1 for Rock: \nPress 2 for Paper: \nPress 3 for Scissors:\n')
    if weapon == '1':
        print('Your weapon is a mighty rock!')
        weapon == 'rock'
    elif weapon == '2': 
        print('Your weapon is a smooth piece of paper!') 
        weapon == 'paper'
    elif weapon == '3':
        print('Your weapon is a pair of sharp scissors!')
        weapon == 'scissors'
    else:
        print('Sorry, that\'s not one of your options, try again.')
    # Go back to the top...how to do that? Call function again? 
 
def main():
    choose_weapon()


if __name__ == '__main__':
    main()
