###############################################################################
#   Gomoku: This is a simple two player game involving the placement of black
#           or white stones on a (typically) 15x15 board. A streak of 
#           (typically) 5 pieces from a single player are required to win. 
#
#   Displays blank board, current player, and prompts for a row and column.
#   
#   Checks if row and column are valid inputs, else displays error message.
#   Checks if position is unoccupied, else displays error message.
#
#   If error message is displayed, reprompts for new input.
#
#   Places player's piece once input is valid, checks to see if winning streak
#   was made.
#
#   If no winner, prompts for next player to make an input.
#
#   If winner, winner is displayed and game ends.
###############################################################################

class GoPiece(object):
    ''' Represents pieces used in the game.'''
    
    def __init__(self,color = 'black'):
        ''' Creates a piece (black or white).'''

        if color == 'black' or color == 'white':
            self.__color = color

        else: #if color is not black or white
            raise MyError('Wrong color.') 
        
    def __str__(self):
        '''Displays each color's respective piece.'''

        if self.__color == 'black':
            return ' ● '
        
        else: #if color is white
            return ' ○ '

    def get_color(self):
        ''' Returns color of piece.'''
        
        return str(self.__color) # 'black' or 'white'
            
class MyError(Exception):
    
    def __init__(self,value):
        self.__value = value
        
    def __str__(self):
        return self.__value

class Gomoku(object):
    '''Sets up, displays, and plays the game.'''
    
    def __init__(self,board_size = 15,win_count = 5,current_player = 'black'):
        '''Initiates board size, number of pieces in a row needed to win, and
        current player's color.'''
        
        if current_player == 'black' or current_player == 'white':
            
            if type(board_size) == int and type(win_count) == int:
                self.__current_player = current_player
                self.__board_size = board_size
                self.__win_count = win_count
                self.__current_player = current_player
                self.__go_board = [ [ ' - ' for j in range(self.__board_size)]\
                                     for i in range(self.__board_size)]
        
            else: #if board size and win count are not integers
                raise ValueError
                
        else: #if color is not black or white
            raise MyError('Wrong color.')    
            
    def assign_piece(self,piece,row,col):
        '''Places piece at specified location on the board.'''

        #  if input column and row are within the range of the board
        if col in range(self.__board_size + 1) and row in \
        range(self.__board_size + 1): 
            
            if self.__go_board[row-1][col-1] == ' - ':
                self.__go_board[row-1][col-1] = piece #add piece to position
                
            else: #if position is something other than a ' - '
                raise MyError('Position is occupied.')
                 
        else: 
            raise MyError('Invalid position.')
            
    def get_current_player(self):
        '''Returns string of current player's color'''
        
        return str(self.__current_player) # 'black' or 'white'
    
    def switch_current_player(self):
        '''Returns string of other player's color'''
        
        if self.__current_player == 'white':
            self.__current_player = 'black'
            return str(self.__current_player) # 'black'
        
        else:
            self.__current_player = 'white'
            return str(self.__current_player) # 'white'
            
    def __str__(self):
        s = '\n'
        for i,row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i+1)
            for item in row:
                s += str(item)
            s += "\n"
        line = "___"*self.__board_size
        s += "    " + line + "\n"
        s += "    "
        for i in range(1,self.__board_size+1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player \
                                   == 'black' else '○')
        return s
        
    def current_player_is_winner(self):
        ''' Checks all columns and rows to see if the player has a winning 
        sequence of pieces. Can be horizontal, vertical, or diagonal.'''
        
        #did this for simplicity of typing variables
        win_count = self.__win_count 
        piece = ' ● ' if self.__current_player == 'black' else ' ○ '
        board = self.__go_board
        board_size = self.__board_size
        winning_seq = piece * win_count
        
        new_board = [] #version of board with player pieces changed to strings
        for sublist in board:
            new_sublist = []
            for item in sublist:
                if item != ' - ':
                    new_item = str(item)
                    new_sublist.append(new_item)  
                else:
                    new_sublist.append(item)  
            new_board.append(new_sublist)
                    
        vert_list_of_lists = [] #new list w items in each column instead of row
        for i in range(board_size):
            vert_list = []
            for j in range(board_size):
                vert_list.append(new_board[j][i])
            vert_list_of_lists.append(vert_list)
            
            
        diag_list = [] #new list w items in each ascending diagonal line
        for row in range(board_size - win_count + 1):
            for col in range(win_count - 1, board_size):
                diag_sublist = []
                for i in range(win_count):
                    diag_sublist.append(new_board[row+i][col-i])
                diag_list.append(diag_sublist)
                
        diag_list_2 = []#new list w items in each descending diagonal line
        for row in range(board_size - win_count + 1):
            for col in range(board_size - win_count + 1):
                diag_sublist_2 = []
                for i in range(win_count):
                    diag_sublist_2.append(new_board[row+i][col+i])
                diag_list_2.append(diag_sublist_2)
            
        for item in new_board: #checks for horizontal sequences
            line_str = "".join(item)
            if winning_seq in line_str:
                return True
        
        for item in vert_list_of_lists: # checks for vertical sequences
            line_str = "".join(item)
            if winning_seq in line_str:
                return True

        for item in diag_list: #checks for ascending diagonal sequences
            line_str = "".join(item)
            if winning_seq in line_str:
                return True

        for item in diag_list_2: #checks for descending diagonal sequences
            line_str = "".join(item)
            if winning_seq in line_str:
                return True
        
        return False
        
def main():

    board = Gomoku()
    print(board)
    piece = GoPiece()
    
    play = input("Input a row then column separated by a comma (q to quit): ")
    
    while play.lower() != 'q':
        play_list = play.strip().split(',')
        
        try: 
            if len(play_list) != 2: #if there are not exactly 2 items input
                raise MyError("Incorrect input.")
            
            else: 
                try: 
                    row = int(play_list[0].strip())
                    col = int(play_list[1].strip())
                    
                except ValueError: #if input items are not integers
                    raise MyError("Incorrect input.")
                
                board.assign_piece(piece,row,col) #assign piece to board
                
                if board.current_player_is_winner() == True: #if winning seq
                    print(board)
                    print("{} Wins!".format(board.get_current_player()))
                    break

                else:
                    new_piece = board.switch_current_player() #switch player
                    piece = GoPiece(new_piece)
                    
        except MyError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
            
        print(board)
        play = \
        input("Input a row then column separated by a comma (q to quit): ")

if __name__ == '__main__':
    main()
