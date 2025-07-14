fin = open('words.txt') #fin is a file object
def filter_20char(file):
    """
    
    file = file object used for input
    """
    for line in file: 
        word = line.strip()
        length = len(word)
        if length > 20: 
            print(word)
        else:
            pass

def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True

def print_no_e(file):
    for line in file:
        word = line.strip()
        status = has_no_e(word)
        if status: # has no e
            print(word)
        
def avoids(word, list):
    for letter in list:
        if letter in word:
            return False
    return True

def forbidden_letters(file): 
    forbid_list = input("Type some forbidden letters:\n")
    count = 0
    for line in file:
        word = line.strip()
        if avoids(word, forbid_list):
            count += 1
    print(count)
    return count

def uses_only(word, letters):
    for char in word:
        if not (char in letters):
            return False
    return True

def uses_all(word, letters):
    for char in letters: 
        if not (char in word): 
            return False
    return True

def is_abecedarian(word):
    index = 0
    length = len(word)
    while index < (length - 1): 
        if word[index] > word[index + 1]:
            return False
        else: 
            index += 1
    return True

def filter_abecedarian(file):
    for line in file:
        word = line.strip()
        status = is_abecedarian(word)
        if status: 
            print(word)




#filter_20char(fin)
#print_no_e(fin)
#forbidden_letters(fin)
#filter_abecedarian(fin)