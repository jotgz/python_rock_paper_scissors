import random

computer_score =  0
player_score = 0

def game_logic():
    while True:
        global player_score
        global computer_score

        computer_options = ('Rock', 'Paper', 'Scissors')
        computer_choice = random.choice(computer_options)
        player_choice = input('What is your weapon? Rock, Paper or Scissors? ').capitalize()
        

        if player_choice == computer_choice:
            print('It \'s a draw!!!')
                # Player Choosing Rock
        elif player_choice == 'Rock':
            if computer_choice == 'Scissors':
                player_score += 1
                print('You win this round!')
            elif computer_choice == 'Paper':
                computer_score += 1
                print('The computer won this round!')

                # Player Choosing Paper
        elif player_choice == 'Paper':
            if computer_choice == 'Rock':
                player_score += 1
                print('You win this round!')
            elif computer_choice == 'Scissors':
                computer_score += 1
                print('The computer won this round!')

                # Player Choosing Scissors
        elif player_choice == 'Scissors':
            if computer_choice == 'Paper':
                player_score += 1
                print('You win this round!')
            elif computer_choice == 'Rock':
                computer_score += 1
                print('The computer won this round!')
       

        print('\n')
        print(f'Player Score: {player_score}')
        print(f'Computer Score: {computer_score}')
        print('\n')

        continue_game = input("Would you like to play again? Press Y or N ").capitalize()

        print('\n')
        

        if continue_game == 'Y':
            return game_logic()
        elif continue_game == 'N':
            print('Thanks for playing! Come again!!!')


game_logic()