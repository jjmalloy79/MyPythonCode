# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
    file = open(filename, 'r')
    dataInfo = []
    for line in file:
        data = line.split(" ")
        dataInfo.append(line.replace("\n" , ""))
    return dataInfo 
    
# ------------------------------------------------------    
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------
def getAverage(l):
#variables    
    totalAmount = 0
    totalAverage = 0
    count = 0
    
# gets the total amount of speed
    for num in l:
        totalAmount = totalAmount + float(num)
        count = count + 1

# gets average
    totalAverage = "{0:.2f}".format(totalAmount / count)
    return totalAverage

# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(l, maxSpeed):
# Variables 
    counter = 0
# gets the number of speeders 
    for speeders in l:
        if(int(speeders) > maxSpeed ):
            counter = counter + 1
            
        else:
            counter = counter
    return counter
            
# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# -----------------------------------------------------

def main():
# variables
   maxSpeed = 69
# reads in file
   dataRushNum = readData("dataRush.txt")
   dataNotRushNum = readData("dataNotRush.txt")
   readData("dataNotRush.txt")
   
# gets average speed
   averageRushHour = getAverage(dataRushNum)
   averageNotRushHour = getAverage(dataNotRushNum)
 
# gets speeders
   speederCountRushHour = countSpeeders(dataRushNum, maxSpeed)
   speederCountNotRushHour = countSpeeders(dataNotRushNum, maxSpeed)
   
 # gets Fine
   fineRushHour =  speederCountRushHour * 150
   fineNotRushHour =  speederCountNotRushHour * 100
# prints data 
   print "The average speed during rush hour was %s" % (averageRushHour)
   print "The average speed not during rush hour was %s" % (averageNotRushHour)
   print "There were %s speeders during rush hour.  Total fine = $%s " % (speederCountRushHour, fineRushHour)
   print "There were %s speeders not during rush hour.  Total fine = $%s" % (speederCountNotRushHour, fineNotRushHour)

# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
main()