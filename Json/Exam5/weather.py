import Epic
import urllib2
import json
#this is to verify that user wants to run again
def run(searchAgain):
    valid = False
    if(searchAgain == "y" or searchAgain == "n"):
        valid = True
    else:
        valid = False
    return valid
# this is the print out data
def printOut(degrees, weather):
    if(degrees.lower() == "f"):
        print "Here is the current weather for %s, %s" % (weather['location']['name'],weather['location']['region'])
        print "%s, and %s degrees (f)" % (weather['current']['condition']['text'],weather['current']['temp_f'])
        print "It actually feels like %s (f)." % weather['current']['feelslike_f']
    else:
        print "Here is the current weather for %s, %s" % (weather['location']['name'],weather['location']['region'])
        print "%s, and %s degrees (c)" % (weather['current']['condition']['text'],weather['current']['temp_c'])
        print "It actually feels like %s (c)." % weather['current']['feelslike_c']  

# this varifies that user enter valid data for the type of degrees
def degreeType(degrees):
    degreeagain = False
    if(degrees.lower() == "f" or degrees.lower() == "c"):
        degreesagain = False
    else:
        degreeagain = True
    return degreeagain
def main():
    #variables
    valid = True
    runagain = True
    degreeagain = False
    #runs until users doesnt want to do so 
    while runagain:
        #gets the area the users wants to look for
        area = Epic.userString("Please enter a zip code or a city name: ")
        #gets the url 
        url = 'https://api.apixu.com/v1/current.json?key=2ff34f2dde774cfbb8a40000171804&q=' + area
        #reads in the url 
        jsonTxt = urllib2.urlopen(url).read()
        #convers url to json
        weather = json.loads(jsonTxt)
        # sees if which type of degree user wants to use
        degrees = Epic.userString("Do you want to read in as Fahrenheit (f) or Celsius (c)")
        # calls degreeagain to make sure entry was valid
        degreeagain = degreeType(degrees)
        # if entry is invalid keeps asking for correct entry.
        while (degreeagain):
            degrees = Epic.userString("You entered an invalid entry. Do you want to read in as Fahrenheit (f) or Celsius (c)")
            degreeagain = degreeType(degrees)
        #this is the print out of data section
        printOut(degrees, weather)
        # sees if users wants to run again
        searchAgain =  Epic.userString("Want to check another location? (y/n) ")
        run(searchAgain)
        # this is what keeps the program in the loop or breaks from it.
        while (not valid):
            searchAgain =  Epic.userString("Please enter a valid answer. do you want to check another location? (y/n) ")
            run(searchAgain)
        if searchAgain == "y":
            continue
        else:
            runagain = False
#calls main function
main ()