import random
from tkinter import *

# computer_score = 0
# player_score = 0
#
#
# def game_logic():
#     while True:
#         global player_score
#         global computer_score
#
#         computer_options = ('Rock', 'Paper', 'Scissors')
#         computer_choice = random.choice(computer_options)
#         player_choice = input('What is your weapon? Rock, Paper or Scissors? ').capitalize()
#
#         if player_choice == computer_choice:
#             print('It \'s a draw!!!')
#
#             # Player Choosing Rock
#         elif player_choice == 'Rock':
#             if computer_choice == 'Scissors':
#                 player_score += 1
#                 print('You win this round!')
#             elif computer_choice == 'Paper':
#                 computer_score += 1
#                 print('The computer won this round!')
#
#                 # Player Choosing Paper
#         elif player_choice == 'Paper':
#             if computer_choice == 'Rock':
#                 player_score += 1
#                 print('You win this round!')
#             elif computer_choice == 'Scissors':
#                 computer_score += 1
#                 print('The computer won this round!')
#
#                 # Player Choosing Scissors
#         elif player_choice == 'Scissors':
#             if computer_choice == 'Paper':
#                 player_score += 1
#                 print('You win this round!')
#             elif computer_choice == 'Rock':
#                 computer_score += 1
#                 print('The computer won this round!')
#
#         print('\n')
#         print(f'Your Choice: {player_choice}')
#         print(f'Computer Choice: {computer_choice}')
#         print(f'Player Score: {player_score}')
#         print(f'Computer Score: {computer_score}')
#         print('\n')
#
#         continue_game = input("Would you like to play again? Press Y or N ").capitalize()
#
#         print('\n')
#
#         if continue_game == 'Y':
#             return game_logic()
#         elif continue_game == 'N':
#             print('Thanks for playing! Come again!!!')
#             break
#
#
# game_logic()


def game():

    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    def choose_rock():
        return 'Rock'

    def choose_paper():
        return 'Paper'

    def choose_scissors():
        return 'Scissors'

    app = Tk()
    app.config(height=350, width=350)
    app.title('Rock Paper Scissors')

    lbl = Label(app, text='Choose rock, paper, or scissors')
    lbl.place(relx=0.5, rely=0.1, anchor='center')

    rock_button = Button(app, padx=30, pady=25, text='Rock', command=choose_rock)
    paper_button = Button(app, padx=30, pady=25, text='Paper', command=choose_paper)
    scissors_button = Button(app, padx=25, pady=25, text='Scissors', command=choose_scissors)

    rock_button.place(relx=0.20, rely=0.25, anchor='center')
    paper_button.place(relx=0.50, rely=0.25, anchor='center')
    scissors_button.place(relx=0.80, rely=0.25, anchor='center')

    app.mainloop()


game()

