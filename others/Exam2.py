#Joshua J. Malloy
# Exam 2 
#this reads in file
def readInTimes(filename):
    #variables 
    d = {}
    #reads in file 
    for line in open(filename):
        temp = line.split(",")
        playersName = (temp[0].strip()).lower()
        playersTime = (temp[1].strip()).lower()
        d[playersTime] = playersName
    
    return d
# this prints and organizes data
def printData(d):
    #Variables
    codeHead = ""
    squareMaster = ""
    advancedTwister = ""
    intimediateTurner = ""
    averageTurner = ""
    pathetic = ""

    #this section put players name into the category they belong into
    for time in d: 
        if float(time) < 10:
           codeHead = (codeHead + "\n" + d.get(time))
           
        if float(time) >= 10 and float(time) < 20:
           squareMaster = (squareMaster + "\n" + d.get(time))
 
        if float(time) >= 20 and float(time) < 30:
           advancedTwister = (advancedTwister + "\n" + d.get(time))

        if float(time) >= 30 and float(time) < 40:
           intimediateTurner = (intimediateTurner + "\n" + d.get(time))
 
        if float(time) >= 40 and float(time) < 60:
           averageTurner = (averageTurner + "\n" + d.get(time))

        if float(time) >= 60:
           pathetic = (pathetic + "\n" + d.get(time))
    #this part prints all users in the category they belong in
    print "Cube Head (0 - 9.99): " + codeHead
    print "\nSquare Master (10 - 19.99): " + squareMaster
    print "\nAdvance Twister (20 - 29.99): " + advancedTwister
    print "\nIntimediate Turner (30 - 39.99): " + intimediateTurner
    print "\nAverage Mover (40 - 59.99): " + averageTurner
    print "\nPathetic (60 and beyond): " + pathetic
        
#this starts the program
def main():
    #this is the calls the readInTimes and printData
    d = readInTimes("timings.txt")
    printData(d)
    
main()