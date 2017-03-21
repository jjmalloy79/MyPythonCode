import Epic
import random
rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

# this section builds the deck of cards
def buildDeck(rank, suit):
    deck = []
    for i in range(13):
        for j in range(4):
            deck.append(rank[i] + ' of ' + suit[j])
    return deck
    
#shuffles the deck
def shuffle(deck):
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
     
#deals player the top five cards
def deal(deal):
        return deal[0:5]

#this shuffles half a deck         
def halfShuffle(half):
     used = random.choice(half)
     cardsUsed = []
     while len(cardsUsed) < 26:
        if not used in cardsUsed:
            cardsUsed.append(used)
        else:
            used = random.choice(half)
     return cardsUsed
    
def main():
# variables
    d = buildDeck(rank,suit)
    s = shuffle(d)
    hand = deal(s)
#prints users hand
    print hand
main()