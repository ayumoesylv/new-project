import logging
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

# EXERCISE 10.7 - UNFINISHED; UNCHECKED
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

# EXERCISE 10.8 - UNFINISHED; UNCHECKED


# EXERCISE 10.9 - UNFINISHED; UNCHECKED
# EXERCISE 10.10 - UNFINISHED; UNCHECKED
# EXERCISE 10.11 - UNFINISHED; UNCHECKED
# EXERCISE 10.12 - UNFINISHED; UNCHECKED





# DRIVERS
total = nested_sum([[1, 2], [3], [4, 5, 6]]) # Eoc ex 10.1
print(total)

cumulist = cumsum([1, 2, 3, 4]) # Eoc ex 10.2
print(cumulist)

mid = middle([1, 2, 3, 4]) # Eoc ex 10.3
print(mid)

t = [1, 2, 3, 4] # Eoc ex 10.4
chop(t)
print(t)

sortstat = is_sorted(['b', 'a']) # Eoc ex 10.5
print(sortstat)

is_anagram('hello', 'jsbin') # Eoc ex 10.6

dupstat = has_duplicates([1, 5, 3, 4]) # Eoc ex 10.7
print(dupstat)

