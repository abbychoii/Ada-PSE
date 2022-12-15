def kth_missing_positive_number(numbers,k):
    # space complexity - O(1)
    '''check if you have a list of increasing size, then could be O(n)
    in this case, O(k) where the list will be the length of k because it stores the missing values'''
    # time complexity - O(max(n,k))
    missing_count = 0
    expecting = 1
    idx = 0 #index

    # Example 
    # arr = [1,5000] 
    # k = 555 - will go through while loop closer to k than the len of arr
    # O(n)
    # O(k)

    # O(n) or O(k), will be whichever is larger (in worst case)
    # k - break once we have the missing count
    # n - len of list
    # O(max(n,k)) or O(n+k)

    # will not be able to do any worse than the highest value in the list, cause k outside of the list is just arithmetic at the end of expecting 
    # O(numbers[-1]) <- will always be less than or equal to this worst case
    while idx < len(numbers) and missing_count < k:
        if expecting == numbers[idx]:
            idx += 1
        else: 
            missing_count += 1
        expecting += 1
    
    expecting += (k - missing_count) - 1 # -1 because we end the loop by adding 1
    # expecting - always will be O(1)
    return expecting

def kth_missing_positive_number(numbers,k): # depends on the constraints
    '''
    1 <= len(array) <= 1000
    1 <= array[i] <= 1000
    1 <= k <= 1000
    array[i] < array[j] for 1 <= i <= j <= len(array)
    '''

    result_array = []

    for i in range(1,1001):
        if i not in numbers and len(result_array) < k: 
            result_array.append(i)
        elif len(result_array) == k:
            break
    
    if len(result_array) < k: 
        diff = k - len(result_array)
        start = result_array[-1] + 1
        end = start + diff

        for i in range(start, end):
            result_array.append(i)

    ''' or 
    result_array = []
    for i in range(1,2001): 
        # change to 2001, to deal with if k is 1000 and length of array is 1000
        if i not in numbers and len(result_array) < k: 
            result_array.append(i)
        elif len(result_array) == k:
            break
    '''


    
    return result_array[-1]

