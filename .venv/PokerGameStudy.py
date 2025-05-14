from DeckStudy import Deck, Card

class PokerHand:
    def __init__(self, deck):

        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self._cards)

    @property
    def is_flush(self):
        for card in self.cards[1:]: #loops through all the cards in the hand dealt, starting from the second one, as these will be compared to the first one
            if self.cards[0].suit != card.suit: #compares the suit of the first card to the suit of the current card in the loop
                return False
        return True

    @property
    def number_of_matches(self):
        matches = 0 #sets the initial pair counter at 0
        for i in range(len(self.cards)): #one loop for each card
            for j in range(len(self.cards)): #one loop for every other card
                if i == j: #if the card from loop 1 is the same as the card from loop 2, then this iteration is skipped
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1 #if a card from loop 1 has the same rank as a card from loop 2, then the pair counter is increased by 1
        return matches #yields the total number of paris after the loops are completed

    @property
    def is_pair(self): #if you call is_pair, this returns True for a pair, which is 2 matches, and False otherwise
        if self.number_of_matches == 2:
            return True
        return False

    @property
    def is_two_pair(self): #same as the is_pair above, but this time with 4 matches
        return self.number_of_matches == 4 # more complicated method
# ^ shorter; returns True when conditional satisfied & if not, automatically False

    @property
    def is_three_pair(self):
        return self.number_of_matches == 6 #is 6 because there are 2 matches for each card

    @property
    def is_four_pair(self):
        return self.number_of_matches == 12 #is 12 because there are 3 matches for each card

# Full house = if is_three_pair & is_two_pair
    @property
    def is_full_house(self):
        return self.number_of_matches == 8 #is 8 because there are 6 matches for three pair and 2 matches for two pair

    @property
    def is_straight(self):
        self.cards.sort() #sorts hands by rank from lowest to highest
        distance = Card.RANKS.index(self.cards[4].rank)  #calculate the distance between the highest ranking card (number 4 in index)
        Card.RANKS.index(self.cards[0].rank) #and the lowest ranking (number 0 in index)
        return self.number_of_matches == 0 and distance == 4 #in a straight, there are 0 matches and 4 distance between the highest and lowest card

count = 0
matches = 0
while matches < 1000: #creates a loop that runs until 1000 straights are found
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_flush:
        matches += 1 #how many straights have been dealt
        print(hand)
    count += 1 #how many hands have been tried in total

print(f"Probability of a flush is {100*matches/count}%")

# Probability of each type of pair:
# single pair ~ 42.405% (10k)
# two pair ~ 4.719% (10k)
# three pair ~ 2.091% (10k)
# four pair ~ 0.026% (100)
# full house ~ 0.146% (1k)
# straight flush ~ 0.351% (1k)