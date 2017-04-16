import json
import Epic

# reads in file
def readIn():
    jsonTxt = ""
    f = open('PetStore.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    items = json.loads(jsonTxt)
    return items
        
#this is to look for keyword  in Products
def Search(section):
#variables 
    data = []
    dataString = ""
    strName = ""
    strG = ""
    itemData = []
    count = 0
    dataPrice = []
    
# sees if user wants to look by keyword
    if section.lower() == "k":
        word = "Enter a keyword: "
        searchFor = "Product"
        
# sees if users wants to look by category
    elif section.lower() == "c":
        word = "Enter a category: "
        searchFor = "Category"
# ask users for what they want to look for
    lookingFor = Epic.userString(word)
    items = readIn()
    
# loops through Product
    for iteminfo in items:
        itemData.append(iteminfo["Product"])
        count = count + 1
        
# if keyword is found 
        if iteminfo[searchFor].lower().find(lookingFor.lower()) != -1:
               strName = iteminfo["Product"]
               
# creates an array to hold all Product's names
               data.append(strName)
               strC = iteminfo["Price"]
               
# creates an array to hold all Product's prices
               dataPrice.append(strC)
               
# if what user wants to find is not in the file
    if iteminfo[searchFor].lower().find(lookingFor.lower()) != -1:  
        print "Sorry I couldn't find %s" % lookingFor
    printOut(data, dataPrice)
    
# this prints out data
def printOut(dataKey, dataCategory):
# varables
    counter = 0
    
# loops through each array and makes class and grad come up on same line
    while counter < len(dataKey):
        
# prints out the data
        print "%s - %s " % (dataKey[counter],dataCategory[counter])
        counter = counter + 1
        
# main function
def main():
#varables
    sectionToSearchIn = Epic.userString("Search for category (c) or keyword callable(k)?")

#This will search through the category section
    if sectionToSearchIn.lower() == "c":
        Search("c")
        
#this will search through the keyword section
    elif sectionToSearchIn.lower() == "k":
       Search("k")
        
# calls main function
main()