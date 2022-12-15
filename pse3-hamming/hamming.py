'''
Clarifying question 
1. will strings be the same length? 
2. what should we be optimizing for here?
3. case sensitivity? 
4. empty/null strings? 
5. invalid inputs? - edge cases

'''

def hamming_distance(strand1,strand2):
    if len(strand1) == len(strand2):
        # space complexity - O(n) creating new list that will store values that differ 
            # worst case, and in worst case where all differ, new list = same as long => O(n)
        # time complexity - O(n)
        return len([strand1[i] for i in range(len(strand1)) if strand1[i].lower() != strand2[i].lower()])
    else:
        raise ValueError
        
# strand1 = "GAGCCTACTAACGGGAT"
# strand2 = "CATCGTAATGACGGCCT"
# print(hamming_distance(strand1, strand2))

# strand1 = "GAG"
# strand2 = "GAG"
# print(hamming_distance(strand1, strand2))

# strand1 = "GAG"
# strand2 = ""
# print(hamming_distance(strand1, strand2))

def hamming_distance1(strand1, strand2): 
    '''
    time complexity - O(n)
    space complexity - O(1)
    '''
    if len(strand1) != len(strand2):
        raise ValueError(f"Lengths must be equal, found lengths of strand1: {len(strand1)} and strand2: {len(strand2)}")
    
    count = 0 
    for i in range(len(strand1)): # O(n) - looping through length of list n 
        if strand1[i].upper() != strand2[i].upper(): 
            #time complexity
            #indexing single item - O(1)
            #.upper or .lower - O(1)
            # comparign 2 letter - O(1)
            # incrementing a value - O(1)
            count += 1
            #space complexity 
            # allocate space for the .upper() but fixed at 1 per so O(1)
    return count 

def hamming_distance2(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError(f"Lengths must be equal, found lengths of strand1: {len(strand1)} and strand2: {len(strand2)}")
    
    # count = 0 
    # for letter1, letter2 in zip(strand1, strand2): 
    #     # zip of unequal length => stop with shorter one 
    #     # zip doesn't increase space complexity
    #     if letter1.upper() != letter2.upper():
    #         count +=1
    # return count
    
    #list comprehension 
    diffs = [1 for letter1, letter2 in zip(strand1, strand2) if letter1 != letter2]
    # time complexity - O(n)
    # space complexity - O(n)
    return len(diffs)

strand1 = "GAGCCTACTAACGGGAT"
strand2 = "CATCGTAATGACGGCCT"
print(hamming_distance2(strand1, strand2))

strand1 = "GAG"
strand2 = "GAG"
print(hamming_distance2(strand1, strand2))

# strand1 = "GAG"
# strand2 = ""
# print(hamming_distance2(strand1, strand2))


def hamming_distance3(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError(f"Lengths must be equal, found lengths of strand1: {len(strand1)} and strand2: {len(strand2)}")
    # time complexity - O(n)
    # space complexity - O(n)
    return sum(1 for letter1, letter2 in zip(strand1, strand2) if letter1 != letter2) # will be summing up the data as it is being generated 
    # sum -> doesn't produce a different list -> O(1) space complexity
    #generator expression - iterate directly over the logic (can't take length cause it won't know when it will end, so use sum because can go one step at a time)
'''
zip - n python 3.x, the zip function itself runs in O(1) time, as it just allocates a special iterable (called the zip object), and assigns the parameter array to an internal field. The function invocation itself (before control reaches in zip) is O(N), as the interpreter must convert the parameters to an array. Every subsequent next call on the iterator also runs in O(N). Exhausting the zip object is therefore O(N*M) assuming M is the average (or minimum) length of the iterables, excluding the time the iterables themselves take to generate items (as it is independent of zip).
'''
    


