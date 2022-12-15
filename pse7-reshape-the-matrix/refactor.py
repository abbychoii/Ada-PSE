def matrixReshape(matrix, r: int, c: int):
	m = len(matrix)
	n = len(matrix[0])
	if n*m!=r*c: #if the total number of elements in the original matrix wouldn't fit into a r by  c matrix
		return matrix #return original
	ans = [[0 for i in range(c)] for j in range(r)] #new empty matrix
	num = 0 #keep track of how many elements we have added to our new array
	for i in range(m): #iterating through mat
		for j in range(n):
			row = num//c #the row we are writing into
			col = num%c #the column we are writing into
			ans[row][col] = matrix[i][j] #add this element to the row in ans
			num+=1 #we added the last element
	return ans

nums =[[1,2],[3,4],[5,6],[7,8]]
r = 2
c = 4

print(matrixReshape(nums, r,c))
nums = [[1,2,3,4,5],[6,7,8,9,10]]
r= 5
c= 2
print(matrixReshape(nums, r,c))