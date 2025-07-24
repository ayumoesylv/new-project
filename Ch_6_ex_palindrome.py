def first(s):
    """
    params
        s (str): string 
    """
    return s[0]

def last(s):
    """
    params
        s (str): string
    """
    return s[-1]

def middle(s):
    """
    params
        s (str): string
    """
    return s[1:-1]

def is_palindrome(s):
    """
    returns true if string passed is palindrome, false if not

    params
        s (str): string
    returns
        (bool): whether string is palindrome or not
    """
    # base case
    if (len(s) == 1) or (len(s) == 0):
        return True
    else:
        if first(s) != last(s):
            return False
        is_palindrome(middle(s))
    return True

word = 'hellolleh'
start = first(word)
end = last(word)
center = middle(word)
status = is_palindrome(word)
print(start, end, center, status)


