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
def printOut(stop, average, posTemp):
    print "During the first %s years, the average deviation from the tempature anomoly is %s." % (stop, average)
    print "During the first %s years, %s had a postive tempature anomoly.\n" % (stop, posTemp)
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
    percent = raw_input("Please enter the percent you want to analysis (e.g. for 70 percent type .7 or .70 : ")
    stop1 = int(float(percent) * 116)
    start2 = stop1
    temp = readTemps()
    average1 = getAve(temp, start1, stop1)
    average2 = getAve(temp, start2, stop2)
    posTemp1 = count(temp,start1,stop1)
    posTemp2 = count(temp,start2,stop2)
    lastYears = 116 - stop1
    firstPercent = float(percent) * 100
    secondPercent = 100 - firstPercent
    print "You have selected the first percent of %s and second half percent of %s.\n" % (firstPercent , secondPercent)
    printOut(stop1, average1, posTemp1)
    printOut(stop2, average2, posTemp2)
    
main()
    


