# ------------------------------------------------------------
# For a badge do the following:
#
# After each user query print out the bird that has been seen 
# most often.  If there is a tie, print all of birds that are 
# tied for most sightings.
#
# Allow the user to enter a bird name as often as the like.
# When they want to stop entering bird names they can type 
# 'Exit'.
#
# Make the lookup case insensitive.  In other words, I should
# be able to type ROBIN or RoBiN and get the count for Robin.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------

def countBirds(filename):
    d = {}
    global seen
    seen = 0
    temp = 0
    tempSeen = 0
    totalBirdSeen = 0 
    for line in open(filename):
        temp = line.split(",")
        birdName = (temp[0].strip()).lower()
        birdSeen = (temp[1].strip()).lower()
        if(birdName in d.keys()):
           birdSeen = int(birdSeen) + int(d.get(birdName))
           d[birdName] = birdSeen 
        else:
            d[birdName] = birdSeen
        if(birdSeen > seen):
            seen = int(birdSeen)
    return d

# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    totalBirdSeen = 0
    print "Enter exit to exit or enter a bird name: "
    n = raw_input()
    if(n.lower() != "exit"):
        
        if (n in d):
            totalBirdSeen = d[n]
        else:
            totalBirdSeen = 0
        print "I have have seen that bird %s time(s)." % (totalBirdSeen) 
        return True
    else:
        return False


def main():
    
    counter = 0
    seenMost = ""
    run = True
    d  = countBirds("Birds.txt")

    while(run):
       run = askUser(d)
       for name, saw in d.iteritems():
           if seen == saw:
               if name in seenMost:
                   break
               else:
                   seenMost =  name  + ","  + seenMost
       print "The bird(s) seen the most was the %s and they were seen %s times" %  (seenMost, seen)
    
main()