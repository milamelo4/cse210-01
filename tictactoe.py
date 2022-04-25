print("Welcome to my Tic Tac Toe")


def main():
    pass

board = ["-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"]


current_player = "x"
winner = None

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2]) 
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("----------") 
   
#print_board(board)  

     
    
def player_input(board):
    user_input = int(input("Please enter a slot number between 1 through 9 or enter 'quit' to exit the program "))
    if user_input >= 1 and user_input <=9 and board[user_input-1] == "-":
        board[user_input-1] = current_player
    else:
        print("Slot already taken.")    
        
                  
def check_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
     
    
    
while True:    
    print_board(board)
    player_input(board)

    
    
   

        
   
        
                 
            
        
        
        
        
#if __name__ == "__main__":
   # main()