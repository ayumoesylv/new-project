import string
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
    for line in file:
        word = line.strip()
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


#change_file(fin)
testdict = count_words(gutefin)
wordlist = ['abacada', 'lalalaa', 'oopsies']
get_most_frequent(testdict, fin)

