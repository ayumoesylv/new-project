fin = open('words.txt') #fin is a file object

# SECTION 9.2 EXERCISE 9.1 - FINISHED; UNCHECKED
def filter_20char(file):
    """
    Reads a file and prints words longer than 20 characters excluding whitespace
    
    params
        file (File object) = file object used for input
    returns
        None
    raises 
        None
    """
    for line in file: 
        word = line.strip()
        length = len(word)
        if length > 20: 
            print(word)
        else:
            pass

# SECTION 9.2 EXERCISE 9.2 - FINISHED; UNCHECKED
def has_no_e(word):
    if 'e' in word:
        return False
    return True

def print_no_e(file):
    count = 0
    total = 0
    for line in file:
        total += 1
        word = line.strip()
        status = has_no_e(word)
        if status: # has no e
            count += 1
            # print(word)

    return count / total

# SECTION 9.2 EXERCISE 9.3 - FINISHED; CHECKED
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


# SECTION 9.2 EXERCISE 9.4 - FINISHED; CHECKED
def uses_only(word, letters):
    for char in word:
        if not (char in letters):
            return False
    return True

# SECTION 9.2 EXERCISE 9.5 - FINISHED; CHECKED
def uses_all(word, letters):
    """
    Solution:
    
    def uses_all(word, letters):
        return uses_only(letters, word)

    """
    for char in letters: 
        if not (char in word): 
            return False
    return True


# SECTION 9.2 EXERCISE 9.6 - FINISHED; CHECKED
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

# PAGE 86 DEMO CODE
def is_palindrome(word):
    """
    
    Alternative:
    def is_palindrome(word):
        return is_reverse(word, word) (from chapter 8)

    """
    i = 0
    j = len(word) - 1

    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

# EXERCISE 9.7 - UNFINISHED; CHECKED
def double_letters(file):
    """
    Finds a word among a file with three consecutive double letters

    Solution:

    def is_triple_double(word):
        i = 0
        count = 0
        while i < len(word) - 1:
            if word[i] == word[i+1]:
                count += 1
                if count == 3:
                    return True
                i += 2
            else: 
                i = i + 1 - 2*count
                count = 0
        return False
    
    def find_triple_double():
        fin = open('words.txt')
        for line in fin:
            word = line.strip()
            if is_triple_double(word):
                print(word)

    """
    for line in file: 
        word = line.strip()
        if len(word) < 6:
            return False
        i = 0
        while i <= len(word) - 6:
            req1 = word[i] == word[i+1]
            req2 = word[i+2] == word[i+3]
            req3 = word[i+4] == word[i+5]
            if req1 and req2 and req3:
                print(word)
            i += 1

# EXERCISE 9.8 - FINISHED; UNCHECKED
def odometer():
    """
    Finds and prints 6 digit numbers that satisfy the condition that 
    last 4 digits are palindromic, 
    1 mile later last 5, 
    1 mile later middle 4,
    1 mile later whole number
    """
    for i in range(100000, 999997):
        first = is_palindrome(str(i)[2:])
        second = is_palindrome(str(i+1)[1:])
        third = is_palindrome(str(i+2)[1:5])
        fourth = is_palindrome(str(i+3))
        
        if first and second and third and fourth:
            print(str(i))

# EXERCISE 9.9 - UNFINISHED; UNCHECKED



# DRIVERS

#filter_20char(fin) # Section 9.2 ex 9.1
percent = print_no_e(fin) # Section 9.2 ex 9.2 
print(percent)

#forbidden_letters(fin)
#filter_abecedarian(fin)

double_letters(fin) # Eoc ex 9.7

odometer() # Eoc ex 9.8
