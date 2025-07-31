import logging
import random
logger = logging.getLogger(__name__)

# SECTION 10.7 DEMO CODE
def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res


# EXERCISE 10.1 - FINISHED; UNCHECKED
def nested_sum(t):
    """
    Returns sum of list of lists

    params
        t (list): list of lists of integers

    returns
        (int): sum of all numbers
    
    raises
        None
    """
    new_t = [add_all(x) for x in t]
    return add_all(new_t)

# EXERCISE 10.2 - FINISHED; UNCHECKED
def cumsum(t):
    """
    returns list of cumulative sums 

    params
        t (list): list of integers
    
    returns
        (list): corresponding cumulative table (in list form)
    
    raises
        None
    """
    sum = 0
    for i in range(len(t)):
        sum += t[i]
        t[i] = sum
    return t

# EXERCISE 10.3 - FINISHED; UNCHECKED
def middle(t):
    """
    returns middle of list

    params
        t (list): list
    returns
        (list): middle of list
    raises
        None
    """
    if len(t) <= 2:
        return t
    return t[1:-1]

# EXERCISE 10.4 - FINISHED; UNCHECKED
def chop(t):
    """
    take a list and modifies it: assigns its middle to it, returns None

    params:
        t (list): list
    
    returns:
        None
    
    raises:
        None
    """
    if len(t) <= 2:
        return 
    t.pop(0)
    t.pop(-1)

# EXERCISE 10.5 - FINISHED; UNCHECKED
def is_sorted(t):
    """
    returns True if list is sorted in ascending order and False otherwise

    params:
        t (list): list
    
    returns:
        (bool): True if sorted ascending, else False
    
    raises:
        None
    """
    i = 0
    while i < len(t)-1:
        if t[i] >= t[i+1]:
            return False
        i += 1
    return True

# EXERCISE 10.6 - FINISHED; UNCHECKED
def is_anagram(t1, t2): 
    """
    returns True if t1 and t2 are anagrams

    params:
        t1 (list): list 1
        t2 (list): list 2
    returns:
        (bool): True if anagrams, else False
    raises:
        None
    """
    if len(t1) != len(t2):
        return False

    if sorted(t1) == sorted(t2):
        return True
    
    return False

# EXERCISE 10.7 - FINISHED; UNCHECKED
def has_duplicates(t):
    """
    returns True if there are duplicate items, and does not modify the og list

    params:
        t (list): list
    returns:
        (bool): True if there are duplicates, else False
    raises:
        None
    """
    b = sorted(t)
    past = b[0]
    for i in b[1:]:
        if past == i:
            return True
        past = i
    return False

# EXERCISE 10.8 - FINISHED; UNCHECKED
def birthday_paradox():
    """
    Returns experimental probability that two people in a class of 23 have the same birthday. 
    """
    count = 0
    n = 10
    for i in range(n): 
        birthdays = [random.randint(1, 365) for q in range(23)]
        if has_duplicates(birthdays):
            count += 1
    return count / n

# EXERCISE 10.9 - UNFINISHED; UNCHECKED
def wordlist_v1(file):
    """
    Returns a list where each element is a word from words.txt. Uses append

    params: 
        file (File object): word file
    returns:
        words (list): list of words from file
    raises:
        None
    """
    words = []
    for line in file:
        elem = line.strip()
        words.append(elem)
    return words

def wordlist_v2(file):
    """
    Returns a list where each element is a word from words.txt. Uses idiom t = t + [x]

    params: 
        file (File object): word file
    returns:
        words (list): list of words from file
    raises:
        None    
    """
    words = []
    for line in file: 
        elem = line.strip()
        words = words + [elem]
    return words

# EXERCISE 10.10 - UNFINISHED; UNCHECKED
def in_bisect(t, v):
    """
    Takes a sorted list and a target value and returns True if the word is in the list and False if not using a bisect search
    
    params
        t (list): sorted list
        v (str): target value in list
    returns
        (bool): True if word in list and False otherwise
    raises
        When type(v) == str and 
    """
    # Find the index of halfway through list (halfindex)
    # Compare v to word at halfindex 
    # if v comes before, assign wordlist to splice [0: halfindex]; if v comes after, assign wordlist to splice [halfindex: -1]
    # if v == word at halfindex, return True, and at the end of the run, return False
    while True:
        fullindex = len(t) - 1
        halfindex = fullindex / 2 if fullindex % 2 == 0 else (fullindex + 1) / 2
        halfindex = int(halfindex)
        print(halfindex)
        if fullindex < 300: 
            print(t)
        if v == t[halfindex]:
            return True
        elif v < t[halfindex] and fullindex > 1:
            t = t[0:halfindex]
        elif v > t[halfindex] and fullindex > 1:
            t = t[halfindex + 1:]
        else:
            print(t)
            return False
            





# EXERCISE 10.11 - UNFINISHED; UNCHECKED
# EXERCISE 10.12 - UNFINISHED; UNCHECKED





# DRIVERS

# total = nested_sum([[1, 2], [3], [4, 5, 6]]) # Eoc ex 10.1
# print(total)

# cumulist = cumsum([1, 2, 3, 4]) # Eoc ex 10.2
# print(cumulist)

# mid = middle([1, 2, 3, 4]) # Eoc ex 10.3
# print(mid)

# t = [1, 2, 3, 4] # Eoc ex 10.4
# chop(t)
# print(t)

# sortstat = is_sorted(['b', 'a']) # Eoc ex 10.5
# print(sortstat)

# is_anagram('hello', 'jsbin') # Eoc ex 10.6

# dupstat = has_duplicates([1, 5, 3, 4]) # Eoc ex 10.7
# print(dupstat)

# chance = birthday_paradox() # Eoc ex 10.8
# print(chance)

fin = open("words.txt") # Eoc ex 10.9
wl = wordlist_v1(fin)
# wl = wordlist_v2(fin)
# print(wl)

bisect_result = in_bisect(wl, 'parkways')
print(bisect_result)