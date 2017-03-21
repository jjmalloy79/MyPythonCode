import Epic
rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

def buildDeck(rank, suit):
    deck = []
    for i in range(13):
        for j in range(4):
            deck.append(rank[i] + ' of ' + suit[j])
    return deck
    
#shuffles the deck
def shuffle(deck):
     newDeck = []
# creates the two deck halves
     firstHalf = deck[0:26]
     secondHalf = deck[26:]
# this takes one card from each deck and goes back an forth
     for i in range(26):
            newDeck.append(firstHalf[i])
            newDeck.append(secondHalf[i])
     return newDeck
#deals player the top five cards
def deal(deal):
        return deal[0:5]
        
def main():
# variables
    shuffling = 2 # this needs to be two because we start at 0 in the 
    # array we shuffle once before going into loop
    d = buildDeck(rank,suit)
    s = shuffle(d)
# gets the number of times  users wants to shuffle
    timesShuffle = Epic.userInt("How many times do you want to shuffle? ")
# this shuffles the deck 
    while shuffling <= timesShuffle:     
        s = shuffle(s)
        shuffling = shuffling + 1
    hand = deal(s)
#prints users hand
    print hand
main()