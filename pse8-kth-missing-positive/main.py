'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Find the kth positive integer that is missing from this array.

constraints 
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
'''


#expected output = 5
def validate_array_all_positive(array):
    if all(num>0 for num in array) and array == sorted(array):
        return array
    else: 
        raise ValueError("Array must be all positive integers and sorted.")

def kth_missing_positive_number(array, k):
    '''
    time complexity: O(n logn) - because of the sorted in the validation, for the rest of the function O(n) where worst case it iterates through the len of the array
    space complexity: O(1) - because will be making the same variables regardless of length of array (will create diff, index variable and change k through the while loop)
    '''
    array = validate_array_all_positive(array)

    if k < array[0]: 
        return k 
    k -= (array[0] - 1)
    
    index = 0 
    while index < len(array)-1:
        # print(f'{array[index]=}')
        diff = array[index + 1] - array[index] -1
        if k <= diff:
            return array[index] + k
        k -= diff
        index += 1
    return array[-1] + k



# def kth_missing_positive_number(array, k):    
#     counter = []
    
#     if array[0] > k:
#         return k
    
#     if array[0] != 1:
#         counter.append(1)
#     i = 0
#     while i < len(array)-1: # len(array) -
#         if array[i] + 1 != array[i+1]: 
#             counter.extend(range(array[i]+1, array[i+1])) # O(k) - where k is the number of items in the range to be added due to
#             # print(counter)
#             i += 1
#         else:
#             i += 1
        
#     while len(counter) < k:
#         if len(counter) == 0 or array[-1] > counter[-1]:
#             counter.append(array[-1] + 1)
#         else: 
#             counter.append(counter[-1] + 1)

#     return counter[k-1]

# array = [1,2,3,4]
# k = 2
# print(kth_missing_positive_number(array,k)) #expecting 6

# array = [1,2,3,5]
# k = 2
# print(kth_missing_positive_number(array,k)) #6

# array = [2,3,4,7,11]
# k = 5
# print(kth_missing_positive_number(array,k)) #9

# array = [1,2,5,7,9,24]
# k = 100
# print(kth_missing_positive_number(array,k)) # 15



