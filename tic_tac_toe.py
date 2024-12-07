# Milestone Project 1
# Congratulations on making it to your first milestone!
# You've already learned a ton and are ready to work on a real project.

# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

# Here are the requirements:

# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
# Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python" otherwise you won't learn anything!) Keep in mind that this project can take anywhere between several hours to several days.

# There are 4 Jupyter Notebooks related to this assignment:

# This Assignment Notebook
# A "Walkthrough Steps Workbook" Notebook
# A "Complete Walkthrough Solution" Notebook
# An "Advanced Solution" Notebook
# I encourage you to just try to start the project on your own without referencing any of the notebooks. If you get stuck, check out the next lecture which is a text lecture with helpful hints and steps. If you're still stuck after that, then check out the Walkthrough Steps Workbook, which breaks up the project in steps for you to solve. Still stuck? Then check out the Complete Walkthrough Solution video for more help on approaching the project!

# There are parts of this that will be a struggle...and that is good! I have complete faith that if you have made it this far through the course you have all the tools and knowledge to tackle this project. Remember, it's totally open book, so take your time, do a little research, and remember:


# Rows
row1 = ['_','_','_']
row2 = ['_','_','_']
row3 = ['_','_','_']
player = ''
game_end = False
player_won = ''


def game_plan(row1,row2,row3):
    # grid print
    print(row1)
    print(row2)
    print(row3)

def row_selection():
    #user row coordinate selection
    row_choice = 'wrong'
    while row_choice not in ["0","1","2"]:
        row_choice = input('Select index of row (0-2):\n')
        if row_choice not in ["0","1","2"]:
            print('You put invalid number')
    return int(row_choice)

def column_selection():
    #user column coordinate selection
    column_choice = 'wrong'
    while column_choice not in ["0","1","2"]:
        column_choice = input('Select index of column (0-2):\n')
        if column_choice not in ["0","1","2"]:
            print('You put invalid number')
    return int(column_choice)

def replace_check(row_index,column_index):
        # check if selecting position is empty or already filled
        if row_index == 0 and (row1[column_index] == 'X' or row1[column_index] == 'O'):
            print('Your coordinates are already taken')
            return True
        elif row_index == 1 and (row2[column_index] == 'X' or row2[column_index] == 'O'):
            print('Your coordinates are already taken')
            return True
        elif row_index == 2 and (row3[column_index] == 'X' or row3[column_index] == 'O'):
            print('Your coordinates are already taken')
            return True
        else:
             return False


def string_replace(row_index,column_index):
    # string replace by player´s mark
    if player == 'Player 1':
        if row_index == 0:
            row1[column_index] = 'X'
            return row1[column_index]
        elif  row_index == 1:
            row2[column_index] = 'X'
            return row2[column_index]
        elif row_index == 2:
            row3[column_index] = 'X'
            return row3[column_index]
        else:
            pass
    elif player == 'Player 2':
        if row_index == 0:
            row1[column_index] = 'O'
            return row1[column_index]
        elif  row_index == 1:
            row2[column_index] = 'O'
            return row2[column_index]
        elif row_index == 2:
            row3[column_index] = 'O'
            return row3[column_index]
        else:
            pass


def end_game():
    # End game check
    winning_combinations = [
        [row1[0], row1[1], row1[2]],
        [row2[0], row2[1], row2[2]],
        [row3[0], row3[1], row3[2]],
        [row1[0], row2[0], row3[0]],
        [row1[1], row2[1], row3[1]],
        [row1[2], row2[2], row3[2]],
        [row1[0], row2[1], row3[2]],
        [row1[2], row2[1], row3[0]],
    ]
    for combo in winning_combinations:
        if combo == ['X', 'X', 'X']:
            return 'Player 1'  # Player 1 wins
        elif combo == ['O', 'O', 'O']:
            return 'Player 2'  # Player 2 wins
    return None  # No winner
def tie_game():
    if '_' not in row1 and '_' not in row2 and '_' not in row3:
        return True
    else:
        return False

while game_end == False:
    game_plan(row1,row2,row3)
    # player 1 section
    player = 'Player 1'
    print('Player 1 Turn')
    replace_status_1 = True
    while replace_status_1:
        row_index_1 = row_selection()
        column_index_1 = column_selection()
        replace_status_1 = replace_check(row_index_1,column_index_1)
    string_replace(row_index_1,column_index_1)
    if tie_game():
        print("It's a tie!")
        break

    winner = end_game()
    if winner:
        print(f"{winner} has won!")
        break

    game_plan(row1,row2,row3)

    #player 2 section
    player = 'Player 2'
    print('Player 2 Turn')
    replace_status_2 = True
    while replace_status_2:
        row_index_2 = row_selection()
        column_index_2 = column_selection()
        replace_status_2 = replace_check(row_index_2,column_index_2)
    string_replace(row_index_2,column_index_2)
    if tie_game():
        print("It's a tie!")
        break

    winner = end_game()
    if winner:
        print(f"{winner} has won!")
        break

game_plan(row1,row2,row3)

    

