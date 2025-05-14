import random

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♠️", "♥️", "♦️", "♣️"]
    def __init__(self, suit, rank):
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank") #if the inputted ranks does not belong to any of the number in the list 'RANK', then a ValueError is raised with the message 'Invalid Rank'
        if suit not in self.SUITS:
            raise ValueError("Invalid Suit") #same thing as for invalid rank
        self._rank = rank
        self._suit = suit

    def __eq__(self, other): #__eq__ is used to check if two ranks are equal to each other or not
        return self.rank == other.rank #returns True/False

    def __gt__(self, other): #compares the position of two cards in the ranks list
        """
        Compares position of 'self' & 'other' in RANKS list
        :param other:
        :return:
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)
#self.RANKS accesses the in-class list of card ranks, while index(self.rank) gets the rank of the current card and turns it into an index
    def __str__(self): # str for when it will be put in a normal string
        return f"{self._rank}{self._suit}"

    def __repr__(self): # use repr for when it will be put in a list
        return self.__str__()

    @property #property changes a method into a variable. a method performs an action, while a variable stores data
    def suit(self):
        return self._suit

    @property #properties are useful for variables that can take on a range of values, but you want to have as given
    def rank(self):
        return self._rank

class Deck:
    def __init__(self):
        self._deck = [] #loops through each suit and rank in both SUIT and RANKS respectively, and adds each combination to the 'deck' list
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))  #creates a deck of 52 cards

    def __str__(self):
        return str(self._deck)

    def shuffle(self): #shuffles the cards in 'deck'
        random.shuffle(self._deck)

    def deal(self):
        return self._deck.pop(0) #.pop is a method that removes an item from the list and returns it. in this case the item at index 0

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())