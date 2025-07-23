import string
import random
fin = open('words.txt')
gutefin = open('gutenberg.txt')

def change_file(file):
    """
    Reads a text file and converts each line to lowercase words without whitespace or punctuation

    params: 
        file (file object): a text file passed through with words in each line
    
    Other args:
        string.whitespace (str): a string of spaces, tabs, etc. characters
        string.punctuation (str): a string of punctuation
    
    returns:
        None
    
    raises:
        None
    """
    wordlist = []
    for part in file:
        line = part.split()
        for word in line:
            word = change_word(word)
            wordlist.append(word)
        # temp = ''
        # for letter in word:
        #     if (letter not in string.whitespace) and (letter not in string.punctuation):
        #         temp += letter 
        # temp = temp.lower()
    return wordlist

def change_word(word):
    """
    converts each word to lowercase words without whitespace or punctuation

    params
        word (str): passed in raw word to be transformed

    returns
        temp (str): modified word in lowercase without whitespace or punctuation (standardized word)

    raises
        None
    """
    word = word.strip()
    temp = ''
    for letter in word:
        if (letter not in string.whitespace) and (letter not in string.punctuation):
            temp += letter 
    temp = temp.lower()
    return temp

def count_words(file):
    """
    counts number of words and frequency of each words in a file

    params
        file (file object): story that is passed as text file
    
    returns
        None

    raises
        None
    """
    record = dict()
    for line in file:
        collect = line.split(' ')
        for word in collect:
            # print(word)
            standard = change_word(word)
            if standard not in record:
                record[standard] = 1
            else: 
                record[standard] += 1
    return record

def get_most_frequent(record, file):
    """
    Prints out the 20 most frequently used words in a dictionary

    params
        record (dict): dictionary matching words - the keys - to frequency - values-
        file (file object): list of words

    returns
        None

    raises
        None
    """
    # traverse dictionary entries and create a new dictionary with reversed elements
    # sort keys
    # print top 20 in a loop 
    
    new_record = dict()
    wordlist = change_file(file)
    not_in_wordlist = []
    print(len(wordlist))

    for entry in record:
        val = record[entry]
        new_record[val] = entry
        if entry not in wordlist:
            not_in_wordlist.append(entry)
    key_list = sorted(new_record)
    i = len(key_list) - 1
    stop = i - 19
    while i >= stop:
        temp = key_list[i]
        print(temp, new_record[temp])
        i -= 1

    print(len(not_in_wordlist))

# RANDOM EXERCISES
def histogram(s):
    """
    takes a sequence and returns a dictionary matching element to frequency

    params
        s (list): some kind of linear sequence such as list or string

    returns
        hist (dict): dictionary mapping of element to frequency in sequence

    raises
        None
    """
    hist = {}
    for letter in s: 
        if letter not in hist: 
            hist[letter] = 1
        else: 
            hist[letter] += 1
    return hist

def choose_from_hist(histogram):
    """
    takes a histogram and returns a random value from histogram, as well as probability
    
    params
        histogram (dict): mapping of histogram categories and their frequency

    returns
        result (str): element and its probability

    raises
        None
    """
    randomkey = random.choice(list(histogram.keys()))

    sum = 0
    for letter in histogram:
        sum += histogram[letter]
    fraction = str(histogram[randomkey])+'/'+str(sum)
    
    return (randomkey, fraction)


# MARKOV EXERCISES

def markov_analysis(file, length):
    """
    takes a text and creates a dictionary that maps prefixes to suffixes

    params
        file (str): file name 
        length (int): prefix length
    returns
        (dict): dictionary that maps prefixes in the text to suffixes
    raises
        None
    """

    # Open and read file line by line
    fin = open(file)

    # Get cleaned words and add them to a word list
    wordlist = change_file(fin)

    # iterate from 0 index to prefix length away from the last index
    # in the next loop, the next word should be appended to the current word to make the new prefix and this should be repeated
    # a conditional is to be made, where if the prefix is in the dictionary already, to append the next word to the empty list directly
    markov = dict()
    for i in range(len(wordlist) - length): 
        # create a prefix using current word + next word, then add that tuple to dictionary with a value of an empty list 
        prefix = tuple(wordlist[i:i+length])

        # the list should append the next word 
        markov[prefix] = markov.get(prefix, []) + [wordlist[i+length]]
    
    return markov

def generate(markov, length):
    """
    generates text based on markov dictionary 

    params
        markov (dict): a markov dictionary mapping prefixes to suffixes 
        length (int): the prefix length
    returns
        text (str): A final string made up of all the words following the markov dictionary and random choices
    raises
        None

    other notes:
        For now, hardcode the number of words of text to be 10, starting key to be the first item in the dictionary
    
    implementation:
        1 Add the first prefix to sequence: loop (length) times to iterate through the tuple, and concatenate each element to empty string
        2 Find suffix: search dictionary for the value of the prefix tuple, which you have, then make a random choice
            list = markov[new tuple] (which is a list of values)
            suffix = random.choice(list)
        3 Add suffix to sequence: concatenate the suffix to the existing string
        4 Create the new prefix: concatenate tuple splice to suffix using tuple concatenation
        5 Repeat steps 2-4
    """
    text = '' # our starting empty string

    # add first prefix to the sequence, hardcode to be first key in dict for first draft
    mkeys = list(markov.keys())
    prefix = random.choice(mkeys)
    for word in prefix:
        text += (word + ' ')

    # establish a loop 
    for i in range(40):
        # find suffix
        slist = markov[prefix]
        suffix = random.choice(slist)
        
        # add suffix to sequence
        text += (suffix + ' ')

        # Create the new prefix
        prefix = prefix[1:] + (suffix,)

    print(text)

    pass


# DRIVERS

# change_file(fin)
# testdict = count_words(gutefin)
# wordlist = ['abacada', 'lalalaa', 'oopsies']
# get_most_frequent(testdict, fin)


# t = ['a', 'a', 'b']
# hist = histogram(t)
# elem, prob = choose_from_hist(hist)
# print(elem, prob)


# mdict = markov_analysis("test.txt", 2)
mdict = markov_analysis("gutenberg.txt", 7)
generate(mdict, 7)