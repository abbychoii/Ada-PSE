# Store the number of rows and number of columns in the matrix in variables row and column
# If rowcolumn does not equal rc, return the matrix
# Initialize an empty list reshaped_matrix
# Iterate through the number of rows
# Initialize a new row
# Iterate through the columns
# Append the correct item to the new row
# Append the new row to the reshaped_matrix
# return the reshaped_matrix

def reshape_matrix(matrix, r, c):
    '''
    time complexity: O(len(matrix) * len(matrix[0])) == O(r*c)
    if n = number of elements in the original matrix,
    time complexity is actually O(n) b/c only iterate through as many elements as are in the matrix

    if n = number of columns, m = number of rows, then will be O(n * m)
    
    space complexity: O(n), where n is the number of elements in the matrix 
    will create a new matrix of the same size as the previous matrix

    '''

    #TODO: validation
    if len(matrix) * len(matrix[0]) != r*c:
        return matrix

    new_matrix = []
    new_row = []
    #flatten our matrix
    for row in matrix: #O(len(matrix)) - # of rows in original
        for item in row: #O(len(matrix[0])) - # of columns in original
            new_row.append(item) # O(1)
            if len(new_row) == c: # O(1)
                new_matrix.append(new_row)# O(1)
                new_row = [] # O(1)
    return new_matrix


