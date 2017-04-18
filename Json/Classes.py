import json
import Epic

# reads in file
def readIn():
    jsonTxt = ""
    f = open('classes.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    classes = json.loads(jsonTxt)
    professor(classes)
    
# gets what professor to look up
def professor(classes):
# varables
    dataString = ""
    strC = ""
    dataClass = []
    strG = ""
    dataGrade = []
    profName = []
    count = 0
# gets professor user wants to find what classes and grades they got
    name = Epic.userString("Enter a Professors name:")
    for classinfo in classes:
        profName.append(classinfo["Name"])
        count = count + 1
        if classinfo["Name"].upper() == name.upper():
# this gets each class and stores it into an array to printout
            for classes in classinfo["Class"]:
                strC = classes
                dataClass.append(strC)
# this gets each grade and stores it into an array to printout                
            for grade in classinfo["Grade"]:
                strG = grade
                dataGrade.append(strG) 
# if the professor is not found
        if classinfo["Name"].upper() != name.upper() and count == len(classes):
# print out that the professor is not in the json file
            print "Sorry!! That professor was not found."
            profList(profName)
# calls printout if professor was found in json file
    printOut(dataClass,dataGrade)
# gets professors listed if user enters wrong data
def profList(proList):
# varables
    counter = 0
# prints out a title for the professor list
    print "List of Professors"
# loops through and prints out all professors in the json file
    while counter < len(proList):
        print proList[counter]
        counter = counter + 1
# Prints out data with class then grade

def printOut(dataClass,dataGrade):
# varables
    counter = 0
# loops through each array and makes class and grad come up on same line
    while counter < len(dataClass):
# prints out the data
        print "'%-10s   %s'" % (dataClass[counter],dataGrade[counter])
        counter = counter + 1

def main():
#varables
    run = True
# loops until user wants to stop
    while run:
# calls read in file to read in json file
        readIn()
# finds out if user wants to run again
        runAgain = Epic.userString("Search again? (y or n)")
# determines if user wants to run again or not
        if runAgain == "y":
            continue
        else:
            run = False
# calls main function
main()