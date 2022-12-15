def is_palindrome(s):
    if type(s) != str: 
        raise TypeError("Please input a string type!")
    
    front = 0
    back = len(s) - 1
    
    while front < back: 
        while not s[front].isalpha():
            front += 1
        while not s[back].isalpha():
            back -= 1
        if s[front] != s[back]:
            return False 
        
        front += 1 
        back -= 1

    return True