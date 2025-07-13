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
        

# drivers
backwards('Hello')
duck_names('JKLMNOPQ')
find('Hello', 's', 2)
count('Hello', 'l')
count_modified('Hello', 'l')
