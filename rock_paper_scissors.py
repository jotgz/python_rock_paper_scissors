import random
from tkinter import *

# computer_score = 0
# player_score = 0


def game():

    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    print(computer_choice)
    text = ''

    def player_pick(choice):
        global text
        if choice == 'Rock':
            if computer_choice == 'Scissors':
                text = f'You won! {choice} beats {computer_choice}'
            if computer_choice == 'Paper':
                text = f'You lost! {computer_choice} beats {choice}'
            elif computer_choice == choice:
                text = 'It\'s a tie!'

        if choice == 'Paper':
            if computer_choice == 'Rock':
                text = f'You won! {choice} beats {computer_choice}'
            if computer_choice == 'Scissors':
                text = f'You lost! {computer_choice} beats {choice}'
            elif computer_choice == choice:
                text = 'It\'s a tie!'

        if choice == 'Scissors':
            if computer_choice == 'Paper':
                text = f'You won! {choice} beats {computer_choice}'
            if computer_choice == 'Rock':
                text = f'You lost! {computer_choice} beats {choice}'
            elif computer_choice == choice:
                text = 'It\'s a tie!'

        final_lbl.config(text=text)
        return text

    app = Tk()
    app.config(height=350, width=350)
    app.title('Rock Paper Scissors')

    lbl = Label(app, text='Choose rock, paper, or scissors')
    lbl.place(relx=0.5, rely=0.1, anchor='center')

    rock_button = Button(app, padx=30, pady=25, text='Rock', command=lambda: player_pick('Rock'))
    paper_button = Button(app, padx=30, pady=25, text='Paper', command=lambda: player_pick('Paper'))
    scissors_button = Button(app, padx=25, pady=25, text='Scissors', command=lambda: player_pick('Scissors'))

    rock_button.place(relx=0.20, rely=0.25, anchor='center')
    paper_button.place(relx=0.50, rely=0.25, anchor='center')
    scissors_button.place(relx=0.80, rely=0.25, anchor='center')

    global final_lbl
    final_lbl = Label(app, text=text)
    final_lbl.place(relx=0.5, rely=0.5, anchor='center')
    app.mainloop()


game()
