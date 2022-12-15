def validate_list(list): #because of the sorted validation -> O(n log n) time complexity
    for num in list:
        if type(num) != int:
            raise ValueError
    if sorted(list) != list:
        raise ValueError
    return list

# def merge_sorted_lists(list1, list2): #space complexity - O(n) where new list will depend on the size fo the input
#     list1 = validate_list(list1)
#     list2 = validate_list(list2)
    
#     i = 0
#     j = 0
#     new_list = []

#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             new_list.append(list1[i])
#             i += 1
#         else:
#             new_list.append(list2[j])
#             j += 1
        
#     while i < len(list1): #catch any of the leftover values in a list after we escape the first while loop
#         new_list.append(list1[i])
#         i += 1
#     while j < len(list2):
#         new_list.append(list2[j])
#         j += 1
    
#     return new_list

def merge_sorted_lists(list1, list2): #space complexity - O(n) where new list will depend on the size fo the input
    list1 = validate_list(list1)
    list2 = validate_list(list2)

    list3 = list1 + list2
    list3.sort() #The sort() function returns nothing, which means it makes changes to the object passed, i.e., the original sequence.
    return list3

