'''
Clarifying Questions
1. numbers instead of strings?
2. input is empty string?
3. what to return if datatype not a string?
4. how to handle white spaces?
5. case sensitivity?
'''

# def palindrome(s):
#     if isinstance(s, str):
#         return s.lower()[::] == s.lower()[::-1]
#     return False

# def palindrome(s):
#     if type(s) == str:
#         if s.lower() == s.lower()[::-1]:
#             return True
#         return False
#     raise ValueError

# def palindrome(s):
#     word = ""
#     if isinstance(s, str):
#         for character in s:
#             if character.isalpha():
#                 word += character.lower()
#         if word == word[::-1]:
#             return True
#         return False
#     raise TypeError("Please input a string type!")

def palindrome(s):
    word = ""
    j = -1

    if isinstance(s, str):
        for letter in s:
            if letter.isalpha():
                word += letter.lower()
    else:
        raise TypeError(f"Given input: {type(s)}. Palindrome function only takes in strings.")
    
    length = len(word)
    
    for i in range(length):
        if word[i] != word[j]:
            return False
        else: 
            j -= 1
    return True
        
    
