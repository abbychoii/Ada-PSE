def reshape_matrix(matrix, desired_r,desired_c):
    #matrix - list of lists containing numbers
    #r - rows
    #c- columns 

    # for list in matrix: 
    #     matrix_dict[count] = list
    #     count +=1
    r= len(matrix)
    c= len(matrix[0])

    pool = []
    for list in matrix:
        for num in list:
            pool.append(num)

    if desired_r * desired_c != len(pool):
        return matrix
    
    new_matrix = {}
    for i in range(desired_r):
        new_matrix[i] = pool[:desired_c]
        pool = pool[desired_c:]
    # print(new_matrix)
    result = []
    for i in range(len(new_matrix)):
        result.append(new_matrix[i])
    return result

    # column = length 
    # row = how many times we iterate through 
    # result = []
    # i = 0
    # while i < desired_r:
    #     new_row = pool[:desired_c]
    #     result.append(new_row)
    #     pool = pool[desired_c:]
    #     i += 1
    # return result
    
nums =[[1,2],[3,4],[5,6],[7,8]]
r = 2
c = 4
print(reshape_matrix(nums, r,c))

