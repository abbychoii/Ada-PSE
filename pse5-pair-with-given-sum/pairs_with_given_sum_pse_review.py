from constants import nums
#time: O(n^2)
#space: O(1)
def pairs_with_given_sum_bad(numbers, target):
    #result_pairs = []
    count = 0
    for i in range(len(numbers)):
        num1 = numbers[i]
        for j in range(i + 1, len(numbers)):
            num2 = numbers[j]
            if num1 + num2 == target:
                count += 1
                #result_pairs.append((num1, num2))
    return count


#time: O(n)
#space: O(n)
def pairs_with_given_sum(numbers, target):
    numbers_dict = {}
    count = 0
    for num in numbers:
        pair = target - num
        if pair in numbers_dict:
            count += 1
        numbers_dict[num] = True
    return count

# print(pairs_with_given_sum(nums, 10001))
