# Milestone Project 1: Tic Tac To Game
# Created by Abhishek Patil on 23-12-2020

def accept_board_position(game_board):
    acceptable_input=[str(index+1) for index,block in enumerate(game_board) if block ==' ' ]
    possible_input=[str(num) for num in(range(1,10))]
    valid_input=False
    while not valid_input:
        user_input=input("Enter Block number: ")
        if user_input not in possible_input:
            print('Invalid Input. Input is not a number between 1 and 9.')
        elif user_input not in acceptable_input:
            print('Input position is already played.')
        else:
            valid_input=True
    return int(user_input)-1


def accept_board_position(game_board):
    acceptable_input=[str(index+1) for index,block in enumerate(game_board) if block ==' ' ]
    possible_input=[str(num) for num in(range(1,10))]
    valid_input=False
    while not valid_input:
        user_input=input("Enter Block number: ")
        if user_input not in possible_input:
            print('Invalid Input. Input is not a number between 1 and 9.')
        elif user_input not in acceptable_input:
            print('Input position is already played.')
        else:
            valid_input=True
    return int(user_input)-1


def game_over(game_board):
    
    #Check rows
    for row in range(0,7,3):
        if (game_board[row]==game_board[row+1]==game_board[row+2]!=' '):
            return True
    
    #Check columns
    for col in range(0,3):
        if (game_board[col]==game_board[col+3]==game_board[col+6]!=' '):
            return True
        
    #Check Cross
    if (game_board[0]==game_board[4]==game_board[8]!=' ') or (game_board[2]==game_board[4]==game_board[6]!=' '):
        return True
    
    return False


def update_board(game_board,player,position):
    if player==1:
        game_board[position]='X'
    else:
        game_board[position]='O'
    return game_board


def play_turn(player, game_board):
    display_board(game_board)
    print(f"Player {player+1}'s turn")
    pos=accept_board_position(game_board)
    update_board(game_board,player,pos)
    player_won=game_over(game_board)
    return (player_won,game_board)


def play_further():
    acceptable_input=['Y','N']
    valid_input=False
    while not valid_input:
        user_input = input('New Game? Y or N').upper()
        if user_input in acceptable_input:
            valid_input=True
        else:
            print('Invalid Input. Please enter Y for Yes and N for No.')
    return user_input.upper() == 'Y'




continue_play = True
while continue_play:
    game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player = 0
    game_finished = False
    turn=0
    while not game_finished and turn != 9:
        (game_finished,game_board)=play_turn(player,game_board)
        if game_finished:
            print(f'Player {player +1} won!!!')
            display_board(game_board)
        player = not player
        turn += 1
    if turn == 9:
        print("Game Draw")
        display_board(game_board)
    continue_play=play_further()
print('GAME OVER!')
