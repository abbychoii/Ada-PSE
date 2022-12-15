def validate_array_all_positive(array):
    if all(num>0 for num in array) and array == sorted(array):
        return array
    else: 
        raise ValueError("Array must be all positive integers and sorted.")


def kth_missing_positive_number(array, k):
    array = validate_array_all_positive(array)

    if k < array[0]: 
        return k 
    
    index = 0 
    while index < len(array)-1:
        # print(f'{array[index]=}')
        diff = array[index + 1] - array[index] -1
        if k <= diff:
            return array[index] + k
        k -= diff
        index += 1
    return array[-1] + k

array = [1,2,3,4,6]
k = 2
print(kth_missing_positive_number(array, k)) #7

array = [2,3,4,6]
k = 1
print(kth_missing_positive_number(array, k)) #1

array = [1,3,4,6]
k = 5
print(kth_missing_positive_number(array, k)) #9    

array = [1,2,4,6]
k = 2
print(kth_missing_positive_number(array, k)) # 5





    # diff = array[-1] - array[0]
    # if diff > len(array) and diff > k :
    #     # this solution is coming from a missing number inside of the given array
    #     #find out how many times to iterate to find k 
        
    #     pass
    # else: 
    #     # find out how mnay numbers missed in array + add from there
    #     # missing number is after the array 

