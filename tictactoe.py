"""
This is my Tic Tac Toe game.
Its the first time I created
this game. It was challenging, and I'm
sure there is a lot to improve.
Author: Camila Melo.

"""

print("Welcome to my Tic Tac Toe")
print()

def main():
    player = switch_player("") 
    board = create_board()
        
    while not (check_winner(board) or check_tie(board)):
        print_board(board)
        player_input(player, board)            
            
        print()
        player = switch_player(player)          
        message(board)      
    
        
    print(f"Thank you for playing.")
    answer = input("Would you like to play again 'yes' or 'no? ")
    if answer.lower() =="yes":
        play_again(board)
    
    else:
        print("Goodbye!") 
           

def message(board):       
    if check_winner(board)== True:
        print_board(board)
        print("We have a winner!") 
          
    if check_tie(board)== True:
        print_board(board)
        print("We have a tie!") 
                
    
def play_again(board):
    player = switch_player("") 
    board = create_board()
    while not (check_winner(board) or check_tie(board)):      
      
        print_board(board)
        player_input(player, board)
        player = switch_player(player)     
    
    print_board(board)
    message(board)
    
    answer = input("Thank you for playing. Would you like to play again 'yes' or 'no? ") 
    if answer.lower() =="no":
        print("Goodbye!")
    while answer.lower() == "yes":
        play_again(board)
        break
        
        
def create_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}') 
    print("----------")
    print(f'{board[3]} | {board[4]} | {board[5]}')  
    print("----------")
    print(f'{board[6]} | {board[7]} | {board[8]}') 
    print("----------") 
   

def check_tie(board):
    for slot in range(9):
        if board[slot] != "x" and board[slot] != "o":
            return False
    return True   

def check_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])    
    
        
def player_input(player, board):
    user_input = int(input(f"\nPlayer {player}, Please enter a slot number between 1-9: "))
    
    a = user_input - 1    
    if board[a]  != "x" and board[a] != "o":
        board[user_input-1] = player              
    else:        
        print("Slot already taken.") 
        player_input(player, board)                 
           
 
def switch_player(player):
    if player == "" or player == "o":
        player= "x"
    elif player == "x":
        player ="o"             
        
    return player     
        
if __name__ == "__main__":
   main()