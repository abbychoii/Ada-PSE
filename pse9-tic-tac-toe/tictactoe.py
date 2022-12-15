'''
Imagine working on software that determines the winner of a game of Tic Tac Toe. Create a function named tic_tac_toe_winner that is responsible for determing the state of a Tic Tac Toe board - Either there's no winner, it's a tie, 'X' won, or 'O' won. This function should take in 3x3 matrix as a parameter. Each element is either an 'X', 'O', or empty string ''. This function should have a return value of the winner 'X' or 'O', 'Tie' (for a full board with no winner), or None (for a game that is still in progress).

Example 1: Input:

[
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'X', 'O']
]

Output: 'Tie'

Example 2: Input:

[
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'O', '']
]

Output: 'O'

Example 3: Input:

[
    ['X', 'O', 'O'],
    ['O', 'X', 'O'],
    ['', '', 'X']
]

Output: 'X'

Example 4: Input:

[
    ['X', '', 'O'],
    ['O', 'X', 'X'],
    ['', '', '']
]

Output: None
'''

'''
    check if 1-3, 4-6, 7-9 are same = (1+2+3)=6, (4+5+6)=15, (7,8,9) =24
    check if 1,4,7 - 2,5,8 - 3,6,9 = 12, 15, 18 - 3 diff
    check if 1,5,9 - 3,5,7 = 15, 15


    if 6, 12, 15, 18, 24
    if //3 and // 6 -> will be a tic tac toe
    
'''
    
'''
ways to win: 
check row 
check column
check diagonal
'''
def check_in_progress(grid):
    if len(grid) < 3:
        return False
    for row in grid: 
        if len(row) < 3:
            return False
        if '' in row or ' ' in row: 
            return True
    return False

def tic_tac_toe_winner(grid):
    if check_in_progress(grid):
        return None

    grid_flat =[]
    for row in grid: #O(n^2) - loop & extend 
        grid_flat.extend(row)
    # print(f'{grid_flat=}')
    
    index_holder = {
        'X' :  [],
        'O' : []
    }

    for i in range(len(grid_flat)):
        if grid_flat[i].upper() == "X":
            index_holder["X"].append(i+1) 
        elif grid_flat[i].upper() == "O":
            index_holder["O"].append(i+1) 
    # print(f'{index_holder=}')

    x_win = False
    o_win = False
    
    win_conditions = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

    for condition in win_conditions:
        # print(all(item in index_holder['X'] for item in condition))
        # print(all(item in index_holder['O'] for item in condition))

        if all(item in index_holder['X'] for item in condition):
            x_win = True
        elif all(item in index_holder['O'] for item in condition):
            o_win = True
        
    if o_win and x_win or not o_win and not x_win :
        return "Tie"
    elif o_win:
        return "O"
    else:
        return "X"


        

    
# input= [
#     ['X', 'X', 'O'],
#     ['O', 'X', 'X'],
#     ['X', 'O', 'X']
# ]

# print(tic_tac_toe_winner(input))
# # print(check_in_progress(input))