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
    count = 0
# gets professor user wants to find what classes and grades they got
    name = Epic.userString("Enter a Professors name:")
    for classinfo in classes:
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
            print "Sorry!! That professor was not found."
    printOut(dataClass,dataGrade)
    
# Prints out data with class then grade
def printOut(dataClass,dataGrade):
# varables
    counter = 0
    while counter < len(dataClass):
        print dataClass[counter] + ":     " + dataGrade[counter]
        counter = counter + 1

def main():
    readIn()

               
                
                
main()