user1 = input('Player1 Name: ')
user2 = input('Player2 name: ')


def chooseinput():
    choice1 = input('For Player1 - choose one and give 1 2 or 3: "1.Rock, 2.Paper or 3.scissor":')
    choice2 = input('For Player2 - choose one and give 1 2 or 3: "1.Rock, 2.Paper or 3.scissor":')
    return(choice1,choice2)
    #rock = 1 scissor = 2 paper = 3

def repeat():
    repeat = input("Want to play again?:(y/n):")
    return(repeat)

gameon = True

while(gameon):
    chooseinput()
    if choice1 = choice2:
        print("its  tie!!")
        repeat()
        if repeat = n:
            gameon = false
    elif choice1 > choice2:
        print(f'congratulations!! {player1} has won!')
        repeat()
        if repeat = n:
            gameon = false
    else:
        print(f'congratulations!! {player2} has won!')
        repeat()
         if repeat = n:
            gameon = false