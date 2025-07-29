# PAGE 72 EXERCISE - FINISHED
def backwards(s): 
    """
    Takes string and prints out characters backwards one by one.

    s = string
    """
    i = len(s) - 1
    while i >= 0:
        letter = s[i]
        print(letter)
        i -= 1

# PAGE 73 EXERCISE - FINISHED
def duck_names(s): 
    """
    Takes string of letters in alphabetical order and lists the duck names one by one.

    s = string
    """
    for letter in s: 
        if letter == 'O' or letter == 'Q':
            print(letter + 'uack')
        else: 
            print(letter + 'ack')

# PAGE 75 EXERCISES - FINISHED
def find(word, letter, start): 
    """
    Given starting index, traverses word until letter is found or is exhausted.

    word = string to traverse
    letter = character to which word items are compared
    start = integer that represents starting index
    """
    index = start
    length = len(word)
    while index < length: 
        cur_letter = word[index]
        if cur_letter == letter:
            return index
        index += 1
    return -1

def count(s, l):
    """
    traverses string s and counts number of times l appears, returning l

    s = string passed
    l = letter of interest
    """
    freq = 0
    index = 0
    length = len(s)
    while index < length:
        if s[index] == l:
            freq += 1
        index += 1
    return freq

def count_modified(s, l):
    """
    returns number of times character l appears in string s

    s = string 
    l = character
    """
    index = 0
    freq = 0
    while index < len(s):
        index = find(s, l, index + 1)
        if index == -1:
            return freq
        else: 
            freq += 1
    return freq

# PAGE 76 DEMO CODE
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

# PAGE 78 EXERCISE - FINISHED
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2) - 1

    while j >= 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    
    return True

# EXERCISE 8.1 (See drivers) - FINISHED; UNCHECKED

# EXERCISE 8.2 (See drivers) - FINISHED; UNCHECKED

# EXERCISE 8.3 - FINISHED; UNCHECKED
def is_palindrome(s):
    """
    Returns true if string is a palindrome, false if not

    params
        s (str): string to test
    returns
        stat (bool): True if palindrome, False if not
    raises
        UnexpectedSequenceError
    """
    try: 
        stat = s == s[::-1]
        return stat
    except:
        print('Expected string type.')
    
# EXERCISE 8.4 (See Ex_8_4_text.txt) - FINISHED; UNCHECKED

# EXERCISE 8.5 - FINISHED; UNCHECKED
def rotate_word(s, r):
    """
    returns string rotated by r characters in alphabet (caesar cypher)

    params:
        s (str): string to be rotated
        r (int): number of positions in alphabet to rotate by
    returns:
        (str): rotated string
    raises:
        None
    """
    new_s = ''
    for c in s:
        raw = (ord(c) + r ) - ord('a')
        wrapped = ord('a') + (raw % 26)
        new_c = chr(wrapped)
        new_s += new_c
    return new_s


# DRIVERS
backwards('Hello') # Page 72 ex 

duck_names('JKLMNOPQ') # Page 73 ex

find('Hello', 's', 2) # Page 75 ex 1
count('Hello', 'l') # Page 75 ex 2
count_modified('Hello', 'l') # Page 75 ex 3

in_both('hello', 'jewwo') # Page 76 demo code

is_reverse('pots', 'stop') # Page 78 ex 

new = " hello ".strip(' h') # Eoc ex 8.1
print(new)
new = "moo, milk, moo, butter".replace("moo", "cow", 1)
print(new)

a_count = "banana".count("a") # Eoc ex 8.2
print(a_count) 

stat = is_palindrome("hellolleh") # Eoc ex 8.3
print(stat)
stat = is_palindrome(1.0)

rotated = rotate_word('abcz', 1) # Eoc ex 8.5
print(rotated)