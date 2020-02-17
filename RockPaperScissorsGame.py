import getpass

def valid_choices():
    return ["1", "2", "3"]

def select_choice(player_name):
    while True:
        choice = getpass.getpass('"'+ player_name+'": choose one and give 1 2 or 3: "1.Rock, 2.Scissor or 3.Paper":')
        if choice in valid_choices():
            return choice
        else:
            print("Invalid choice.")


def select_choices(player1, player2):
    choice1 = select_choice(player1)
    choice2 = select_choice(player2)
    return [choice1,choice2]

def can_continue():
    return str(input('Want to play again?:(y/n):'))

def calc_result(player1, choice1, player2, choice2):
    if choice1 == choice2:
        print("its  tie!!")
    elif choice1 < choice2:
        print(f'congratulations!! {player1} has won!')
    else:
        print(f'congratulations!! {player2} has won!')

def play():
    player1 = input('Player1 Name: ')
    player2 = input('Player2 name: ')
    while True:
        [choice1, choice2] = select_choices(player1, player2)
        calc_result(player1, choice1, player2, choice2)
        if can_continue().lower() != 'y':
            break

play()