import Epic
import urllib2
import json

#this section is to verify that user wants to run program again
def run(searchAgain):
    #variable
    valid = False
    # checks what user enter to what is suppose to be entered
    if(searchAgain == "y" or searchAgain == "n"):
        valid = True
    else:
        valid = False
    #returns true or false if user followed direction correctly
    return valid
    
# this is the print out data
def printOut(degrees, weather):
    # prints out data of the location the user wanted in fahrenheit
    if(degrees.lower() == "f"):
        print "Here is the current weather for %s, %s" % (weather['location']['name'],weather['location']['region'])
        print "%s, and %s degrees (f)" % (weather['current']['condition']['text'],weather['current']['temp_f'])
        print "It actually feels like %s (f)." % weather['current']['feelslike_f']
    # prints out data of the location the user wanted in Celsius
    else:
        print "Here is the current weather for %s, %s" % (weather['location']['name'],weather['location']['region'])
        print "%s, and %s degrees (c)" % (weather['current']['condition']['text'],weather['current']['temp_c'])
        print "It actually feels like %s (c)." % weather['current']['feelslike_c']  

# this varifies that user enter valid data for the type of degrees
def degreeType(degrees):
    #variables
    degreeagain = False
    # see if user followed the direction and entered a f or c for the type of degrees wanted
    if(degrees.lower() == "f" or degrees.lower() == "c"):
        degreesagain = False
    else:
        degreeagain = True
    # returns true or false to show if the user did what was ask of them to enter an
    return degreeagain
    
# this sees if user entered a valid location
def getLocation():
    #gets the area the users wants to look for
    area = Epic.userString("Please enter a zip code or a city name: ")
    #gets the url 
    return 'https://api.apixu.com/v1/current.json?key=2ff34f2dde774cfbb8a40000171804&q=' + area
    
# this ask the user if they want to search again    
def runProgramAgain():
    return Epic.userString("Want to check another location? (y/n) ")
# this is what keeps the program in the loop or breaks from it.
def endOrContinue(valid):
    while (not valid):
        searchAgain =  Epic.userString("Please enter a valid answer. do you want to check another location? (y/n) ")
        run(searchAgain)
    if searchAgain == "y":
        return True
    else:
        return  False  
def main():
    #variables
    valid = True
    runagain = True
    degreeagain = False
    #runs until users doesnt want to do so 
    while runagain:
        url = getLocation()
        #reads in the url 
        while True:
            try:
                jsonTxt = urllib2.urlopen(url).read()
                break
            except: #HTTPException as e:
                print("Oops!  That didnt work.  Try again...")
                url = getLocation()                
        # this reads the url into json to be converted to python
        jsonTxt = urllib2.urlopen(url).read()
        #convers url to json
        weather = json.loads(jsonTxt)
        # sees if which type of degree user wants to use
        degrees = Epic.userString("Do you want to read in as Fahrenheit (f) or Celsius (c)")
        # calls degreeagain to make sure entry was valid
        degreeagain = degreeType(degrees)
        # if entry is invalid keeps asking for correct entry.tat
        while (degreeagain):
            degrees = Epic.userString("You entered an invalid entry. Do you want to read in as Fahrenheit (f) or Celsius (c)")
            degreeagain = degreeType(degrees)
            
        #this is the print out of data section
        printOut(degrees, weather)
        
        # sees if users wants to run again
        searchAgain = runProgramAgain()
        run(searchAgain)
        
        # this is what keeps the program in the loop or breaks from it.
        runagain = runProgramAgain(valid)
#calls main function
main ()