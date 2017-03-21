import random 

# Variables
rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

# this section builds the deck of cards
def buildDeck(rank, suit):
    deck = []
    for i in range(13): # this is for the rank of the cards
        for j in range(4): # this is for the suit of the cards
            deck.append(rank[i] + ' of ' + suit[j])
    return deck
    
#shuffles the deck
def shuffle(deck):
# variables
     newDeck = []
     randShuffle = 0
     
#cuts the deck in half
     firstHalf = deck[0:26]
     secondHalf = deck[26:]
#this calls the halfShuffle to shuffle each half separately 
     newFirst = halfShuffle(firstHalf)
     newSecond = halfShuffle(secondHalf)
     
#this adds one card from each half deck to the newDeck
     for i in range(26):
            newDeck.append(newFirst[i])
            newDeck.append(newSecond[i])
     return newDeck
     
#deals player the top five cards in the deck
def deal(deal):
        return deal[0:5]

#this shuffles half a deck         
def halfShuffle(half):

# Variables
     used = random.choice(half) # places random card into used
     cardsUsed = []

# Goes through loop until all cards are placed into deck
     while len(cardsUsed) < 26: 

# Places card into cardsUsed if card is not already in cardsUsed
        if not used in cardsUsed:
            cardsUsed.append(used)
# gets a new card 
        else:
            used = random.choice(half)
            
     return cardsUsed
    
def main():
#this section creates deck, shuffles it, and deals a hand out to a single player
    d = buildDeck(rank,suit)
    s = shuffle(d)
    hand = deal(s)
#prints users hand
    print hand
main()