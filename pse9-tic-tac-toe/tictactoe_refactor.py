def check_in_progress(grid):
    if len(grid) < 3:
        return False
    for row in grid: 
        if len(row) < 3:
            return False
    if '' in grid[0] or '' in grid[1] or '' in grid[2]:
        return True
    return False


def tic_tac_toe_winner(board):
    if check_in_progress(board): #returns true if invalid input or in-progress game
        return None
    
    first_winner = None
    second_winner = None
    # list of tuples storing the index of each must be the same 
    winning_combinations = [ [ (0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [ (0, 0), (1, 0), (2, 0)], [ (0, 1), (1, 1), (2, 1)], [ (0, 2), (1, 2), (2, 2)], [ (0, 0), (1, 1), (2, 2)], [ (0, 2), (1, 1), (2, 0)] ]

    for combination in winning_combinations: 
        # print(combination)
        # print(board[combination[0][0]][combination[0][1]])
        if board[combination[0][0]][combination[0][1]] == board[combination[1][0]][combination[1][1]] == board[combination[2][0]][combination[2][1]]:
            check = board[combination[0][0]][combination[0][1]]
            if not first_winner:
                first_winner = check
            elif check != first_winner:
                second_winner = check
    
    if first_winner and second_winner or not first_winner and not second_winner:
        return "Tie"
    elif first_winner: 
        return first_winner
    else:
        return second_winner
            

input= [
    ['T', 'Y', 'Y'],
    ['Y', 'T', 'Y'],
    ['T', '', 'Y']
]

print(tic_tac_toe_winner(input))

