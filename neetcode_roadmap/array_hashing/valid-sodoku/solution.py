class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def col_row_check():
            digit_dict = {} # column index is key, value is list of digits in that column
            for i in range(9): # row index
                row_array = [] # list of digits in that row
                for j in range(9): # column index
                    row_val = board[i][j] # value in that cell
                    try:
                        temp = digit_dict[j] # list of digits in that column
                    except:
                        digit_dict[j] = [] # initialize list of digits in that column
                    if row_val == ".": # if cell is empty (empty cell is represented by "."), continue
                        continue
                    if row_val in digit_dict[j]: # if digit is already in column, return false
                        return False
                    if row_val in row_array: # if digit is already in row, return false
                        return False
                    digit_dict[j].append(row_val) # add digit to column list
                    row_array.append(row_val) # add digit to row list
            return True
        
        def threebythree_check():
            h_index = 0 # horizontal index of top left cell of 3x3 block
            left_top_p = 0 # vertical index of top left cell of 3x3 block
            for i in range(9): # iterate through 3x3 blocks
                num_block = [] # list of digits in that 3x3 block
                for j in range(left_top_p, left_top_p+3): # iterate through cells in 3x3 block
                    ele1 = board[h_index][j] # value of cell 1
                    ele2 = board[h_index+1][j] # value of cell 2
                    ele3 = board[h_index+2][j] # value of cell 3
                    for ele in [ele1,ele2,ele3]: # iterate through cells in 3x3 block
                        if ele == ".": # if cell is empty, continue
                            continue
                        if ele in num_block: # if digit is already in 3x3 block, return false
                            return False
                        else:
                            num_block.append(ele) # add digit to 3x3 block list
                left_top_p+=3 # move to next 3x3 block
                if left_top_p == 9: # if at end of row, move to next row
                    h_index+=3 # move to next row
                    left_top_p=0 # reset vertical index
            return True
        
        return col_row_check() and threebythree_check() # return true if both checks pass
        