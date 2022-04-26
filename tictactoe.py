import random
print("Welcome to my Tic Tac Toe")


def main():
    player = switch_player("") 
    board = create_board()
    while not (check_winner(board) or check_tie(board)):      
      
        print_board(board)
        player_input(player, board)
        player = switch_player(player) 
        computer_turn(board)
    
    
    print_board(board)
    print(f"Thank you for playing.")
    answer = input("Would you like to play again 'yes' or 'no? ")
    while answer == "yes":
        play_again(board) 
    
        break    
 
        
    
def play_again(board):
    player = switch_player("") 
    board = create_board()
    while not (check_winner(board) or check_tie(board)):      
      
        print_board(board)
        player_input(player, board)
        player = switch_player(player)     
    
    print_board(board)
    answer = input("Thank you for playing. Would you like to play again 'yes' or 'no?")     
        
def create_board():
    board = []
    for slot in range(9):
        board.append(slot + 1)
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
    user_input = int(input(f"{player}, Please enter a slot number between 1-9: "))
    if user_input >= 1 and user_input <=9:
        board[user_input-1] = player
    else:
        print("Slot already taken.")    
 
def switch_player(current_player):
    if current_player == "" or current_player == "o":
        return "x"
    elif current_player == "x":
        return "o"        
        
def computer_turn(board, current_player):
    while current_player == "0":
        guess = random.randint(0, 8)
        if board[guess] == "-":
            board[guess] = "0"
            switch_player()
                          

     

    

         
       
                  
        
        
        
if __name__ == "__main__":
   main()