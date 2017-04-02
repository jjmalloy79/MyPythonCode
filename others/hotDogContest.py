import time
import random
import Epic


def printOut(name, eaten):
    print "%s has eaten %s hot dogs!"  % (name, eaten)

#this gets the total hot dogs eaten by contestant
def getsEatenHotDogs(hotDogs):
    hotDogs = hotDogs + random.randrange(0, 6)
    return hotDogs

#this displays winner
def printWinner(Tom, Sally, Fred, picked):
  
    #This displays if Tom wins.
    if(int(Tom > Sally and Tom > Fred)):
       if(picked.lower() == "tom"):
           print "You guessed right, Tom wins!"
           return True
       else:
            print "Tom wins!"
            return False
            
    #This display if sally wins.        
    if(int(Tom < Sally and Sally > Fred)):
       if(picked.lower() == "sally"):
           print "You guessed right, Sally wins!"
           return True
       else:
           print "Sally Wins"
           return False
           
    #This display if Fred wins.
    if(int(Fred > Sally and Tom < Fred)):
       if(picked.lower() == "fred"):
           print "You guessed right, Fred wins!"
           return True
       else:           
           print "Fred Wins"
           return False

#this gets what the users wants to bet
def getBet(money):
    betNumber = 0
    print "How much do you want to bet? (cash = %s)" % money
    betNumber = int(raw_input())
# this sees if user has that amount of money if they do let them to continue to play
    if(betNumber <= money and betNumber > 0):
        return betNumber
    
    else:
# this area keeps asking user for the money until they continue to enter invalid amount
# of  money example cash is 50 and user puts 51 or more or a negative number.
        while (betNumber > money or betNumber < 0):
           print "Please enter a valid amount. Enter an amount less than or equal to %s .(cash = %s)" % (money, money)
           betNumber = int(raw_input())
           if (betNumber <= money and betNumber > 0):
                return betNumber

#this will get user money after contest
def totalMoney(money, gain, bet):
    if(gain):
        return (money + bet)
    else:
        return (money - bet)

#starts program
def main():

#variable money available
    money = 100
    bet = 0
    winnings = 0
    gain = True

#variable to end loop
    run = True
    while run:

#variables
        hotdogsTom = 0
        hotdogsSally = 0
        hotdogsFred = 0
        maxDog = 50
        eat = True
        #gets users guess on who will win
        playerPicked = Epic.userString("Pick a winner (Tom, Sally, or Fred)")
        if(playerPicked.lower() != "sally" or playerPicked.lower() != "tom" or playerPicked.lower() != "fred" ):
            playerPicked = Epic.userString("Invalid choice please pick Tom, Sally, Or Fred!")
        bet = getBet(money)

#starts eatting contest      
        print "Ready, set, eat!"
# slows down contest 
        time.sleep(2)

# This while loop runs until a contestant has eaten more than 50 hotdogs
        while(eat):

            print "chomp... chomp... chomp..."
            hotdogsFred = getsEatenHotDogs(hotdogsFred)
            hotdogsSally= getsEatenHotDogs(hotdogsSally)
            hotdogsTom = getsEatenHotDogs(hotdogsTom)

#prints out hot dogs eaten by each contestant
            print ""
            printOut("Tom", hotdogsTom)
            printOut("Sally", hotdogsSally)
            printOut("Fred", hotdogsFred)
            print ""

#this ends the contest if  a contestant eats more than 50 hotdog
            if(hotdogsFred <= maxDog and hotdogsSally <= maxDog and hotdogsFred <= maxDog ):
                eat = True
            else:
                eat = False
                
#slows down contest      
            time.sleep(3)
    
#This gets the winner of the contest and see if player choosed the winner
        gain = printWinner(hotdogsTom, hotdogsSally, hotdogsFred, playerPicked)   
        money = totalMoney(money, gain, bet)
        
# this will end game if user has no money    
        if money == 0:
            run = False
            
# prints end of game
    print "Game Over!"
    
main()