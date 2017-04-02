#Joshua J. Malloy
#temperatureAnalytics.py
#2-5-2017

#read in files
def readTemps():
    file = open('temps.txt', 'r')
    dataInfo = []
    for line in file:
        data = line.split(" ")
        dataInfo.append(line.replace("\n" , ""))
    return dataInfo
    
#print data
def printOut(section,stop, average, posTemp):
    
    print "During the %s %s years, the average deviation from the tempature anomoly is %s." % (section,stop, average)
    print "During the %s %s years, %s had a postive tempature anomoly.\n" % (section,stop, posTemp)
    return 0
#Calculates ave of temp
def getAve(temp, start, stop):
    count = stop - start
    totalAmount = 0
    totalAverage = 0
    
    #gets total amount
    while(start < stop):
        totalAmount = float(temp[start]) + totalAmount
        start = start + 1
    # gets average
    aveAmount = totalAmount / count
    return aveAmount
    
#temperature positive
def count(temp, start, stop):
   
    counter = 0 
    while(start < stop):
       if(float(temp[start]) > 0):
            counter = counter + 1
       start = start + 1
    return counter
 
   
def main():

#varibles
    start1 = 0
    stop2 = 116
    
    #gets the percentage the user wants to use
    percent = raw_input("Please enter the percent you want to analysis (e.g. 70  for 70%) ")
    
    # gets the stop point for first percentage section 
    stop1 = int((float(percent) / 100) * 116)
    start2 = stop1
    
    #reads infile
    temp = readTemps()
    
    #gets average
    average1 = getAve(temp, start1, stop1)
    average2 = getAve(temp, start2, stop2)
    
    #gets number of times a positive temp occurs
    posTemp1 = count(temp,start1,stop1)
    posTemp2 = count(temp,start2,stop2)
    
    #gets the starting point for last half to analysis
    lastYears = 116 - stop1
    
    #determines what the percent is being used
    firstPercent = float(percent) 
    secondPercent = 100 - float(percent)
    
    #displays all the data used first: the user selected percentage points then with the data of first section and then second
    print "You have selected the first percent of %s and second half percent of %s.\n" % (firstPercent , secondPercent)
    printOut("first",stop1, average1, posTemp1)
    printOut("second",lastYears, average2, posTemp2)
    
main()
    


