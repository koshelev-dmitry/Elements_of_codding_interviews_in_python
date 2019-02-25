def is_palindromic(message):
    l = 0
    r = len(message) - 1
    while l < r:
        while not message[l].isapha() and i < j:
            l += 1
        
        while not message[r].isapha() and i < j:
            r -= 1
        
        if message[l].lower() != message[r].lower():
            return False
        l += 1
        r -= 1
    return True