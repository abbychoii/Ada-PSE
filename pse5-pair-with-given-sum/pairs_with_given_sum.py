
def pairs_with_given_sum(numbers, target):
    pairs = []
    # number_pool = [num for num in numbers]
    for num in numbers:
        if num * 2 == target:
            if numbers.count(num) == 1: #count in for loop -> n^2
                break
            else:
                pairs.append((num, num))
                # number_pool.remove(num)
                # number_pool.remove(num)
        elif target - num in numbers:
            pairs.append((num, target-num))
            # numbers.remove(num)
    return len(pairs)/2



# use dictionary
# def pairs_with_a_given_sum(numbers,target):
#     number_bank = {}
#     pairs = 0
#     for num in numbers:
#         if num * 2 == target:
#             if numbers.count(num) == 2:
#                 pairs += 1
#         number_bank[num] = target - num
#     print(number_bank)
#     for num in numbers:
#         if number_bank[num] in number_bank:
#             pairs += 1
#             del number_bank[num]
#     return pairs

numbers = [1, 2, 3, 4, 3, 5] 
target = 6
# print(pairs_with_given_sum(numbers, target))
