'''
Example Steps for an O(n) solution:

Check for valid input
Create a list of all possible winning combinations
winning_combinations = [ [ (0, 0), (0, 1), (O, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [ (0, 0), (1, 0), (2, 0)], [ (0, 1), (1, 1), (2, 1)], [ (0, 2), (1, 2), (2, 2)], [ (0, 0), (1, 1), (2, 2)], [ (0, 2), (1, 1), (2, 0)] ]
Loop throught the winning combinations and check to see if each element in the conbination is equal and not empty.
If this is true return the value of the first element in the combination.
'''
def tic_tac_toe_winner(board):
    '''
    INPUT: Tic Tac Toe board (3x3 matrix)
    OUTPUT: Winner
    '''
    # Check for valid input
    if board == None: return None
    
    # Create a list of all possible winning combinations

    winning_combinations = [ 
        [ (0, 0), (0, 1), (0, 2)], 
        [ (1, 0), (1, 1), (1, 2)], 
        [ (2, 0), (2, 1), (2, 2)], 
        [ (0, 0), (1, 0), (2, 0)], 
        [ (0, 1), (1, 1), (2, 1)], 
        [ (0, 2), (1, 2), (2, 2)], 
        [ (0, 0), (1, 1), (2, 2)], 
        [ (0, 2), (1, 1), (2, 0)] ]

    # Loop through the winning combinations and 
    # check to see if each element in the combination is equal and not empty.

    for combination in winning_combinations:
        char_one = board[combination[0][0]][combination[0][1]]
        char_two = board[combination[1][0]][combination[1][1]]
        char_three = board[combination[2][0]][combination[2][1]]
        
        if char_one == char_two == char_three:
            return char_one
            
    if "" in board[0] or "" in board[1] or "" in board[2]:
        return None
    else:
        return 'Tie'