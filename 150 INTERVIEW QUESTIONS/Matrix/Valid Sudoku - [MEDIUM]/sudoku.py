# Link to the exercise : https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:

#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.

############### EXERCISE ###############
########################################

### Functions ###
def check_row(row, board):
    temp = board[row]
    temp = list(filter(lambda a: a != ".", temp)) #filtering unused values
    
    if any(i < 0 and i > 9 for i in temp):      #checking invalid values
        return False
    
    elif len(temp) != len(set(temp)):       #checking for duplicates
        return False
    else:
        return True

def check_col(col, board):
    temp = [row[col] for row in board]
    temp = list(filter(lambda a: a != ".", temp))    #filtering unused values
    
    if any(i < 0 and i > 9 for i in temp):      #checking invalid values
        return False
    
    elif len(temp) != len(set(temp)):       #checking for duplicates
        return False
    else:
        return True

def check_squares(board):
    for row in range(0, 9, 3):      # making subsquares
        for col in range(0,9,3):
            temp = []
            for r in range(row,row+3):
                for c in range(col, col+3):
                    if board[r][c] != '.':
                        temp.append(board[r][c])

            if any(i < 0 and i > 9 for i in temp):  #checking invalid values
                return False
            
            elif len(temp) != len(set(temp)):   #checking for duplicates
                return False
    return True

### Main ###
def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    
    for i in range(9):
        result_row = check_row(i, board)
        result_col = check_col(i, board)
        
        if (result_row == False or result_col == False):
            return False
    
    result_squares = check_squares(board)
    if (result_squares == False):
        return False
    else:
        return True

