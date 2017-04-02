import random
import Epic
#global variables
global nameOfItems
nameOfItems = ["bird", "dog", "snake", "fish","cat","mouse","starfish","woodchuck","crab"]
global gameBoard
# sets gameboard with Items in game minus the duplicate card
gameBoard = nameOfItems

#shuffles deck
def shuffleCards():
#randomizes game board    
    random.shuffle(gameBoard)
    
# adds a duplicate card from list
def addCard():
    gameBoard = nameOfItems
# gets random word
    duplicated = random.randrange(0,9)
    tempWord = nameOfItems[duplicated]
#adds random word to list
    gameBoard.append(tempWord)
    
# sees if user made a match   
def match(pickOne, pickTwo):
#if there is a match returns false to end game
    if(gameBoard[int(pickOne)] == (gameBoard[int(pickTwo)])):
        return False
    else: 
        return True
        
def main():
# variables
    run = True
    numberOfTries = 0
# calls addCard to add a word
    addCard()
# calls shuffle to shuffle deck
    shuffleCards()
    
#plays game until users gets a match
    while run:
# gets first Card
        pickOne = Epic.userInt("Please pick the first card to turn over (0 -9)")
#gets second card
        pickTwo = Epic.userInt("Please pick the second card to turn over (0 -9)")
#if invaild number is made makes users selected until valid number it made
        while (pickOne > 9 or pickOne < 0 or pickTwo > 9 or pickTwo < 0 or pickTwo == pickOne):
            print "Invaild choice. Must be a different number cards and cards must be a number from 0-9"
            pickOne = Epic.userInt("Please pick the first card to turn over (0 -9)")
            pickTwo = Epic.userInt("Please pick the second card to turn over (0 -9)")
        print "card 0 is a %s" % gameBoard[pickOne]
        print "card 1 is a %s" % gameBoard[pickTwo]
#sees if there is a match if there is game over
        run = match(pickOne, pickTwo)
# keeps track of how many tries the users makes
        numberOfTries = numberOfTries + 1
    print "Congrates you won! It took you %s tries." % numberOfTries
main() #calls main