import random

"""
Exercises to complete:
    Page 174: Use __lt__ method for Time objects
    End of chapter 3 exercises 
"""

# PAGE 172 DEMO CODE
class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
    
    # PAGE 174 DEMO CODE
    """
    Written in comments to prevent redundancy 

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        # suits are the same...check ranks
        return self.rank < other.rank
    """
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    
# PAGE 174 DEMO CODE
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4): 
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    # PAGE 175 DEMO CODE
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    # PAGE 176 EXERCISE - UNFINISHED
    def sort(self): 
        self.cards.sort()

    # PAGE 177 DEMO CODE
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
        

# PAGE 176 DEMO CODE
class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


# PAGE 178 DEMO CODE
def find_defining_class(obj, meth_name):
    for ty in type(obj).mro:
        if meth_name in ty.__dict__:
            return ty


# PAGE 179 DEMO CODE
class Markov:
    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()
    
    def process_word(self, word, order=2):
        if len(self.prefix) < order:
            self.prefix += (word,)
            return
    
        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            # if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = word
        
        self.prefix = shift(self.prefix, word)

# DRIVER CODE
queen_of_diamonds = Card(1, 12) # Page 172 demo code
card1 = Card(2, 11)
print(card1)

deck = Deck() # Page 174 (technically 175) demo code
print(deck)

deck.sort() # Page 176 ex 1; Looked at answer

hand = Hand('new hand') # Page 176 demo code
card = deck.pop_card()
hand.add_card(card)
print(hand)

print(find_defining_class(hand, 'shuffle')) # Page 178 demo code