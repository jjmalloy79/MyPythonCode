import Epic
#global variables
suspects = ["miss scarlet", "col mustard", "mr green"]
weapons = ["candlestick", "wrench", "pipe"]
#gets the possibilities that are left
def possibilities():
    p = []
    for suspect in suspects: # 2 times
        for weapon in weapons: # 3 times
            p.append("%s %s" % (suspect,weapon))
    print "%s possibilities left." %len(p)  
# returns the size of the p array
    return len(p)
# removes suspect that is not guility
def removeSuspects():
    suspectName = Epic.userString("Enter the innocent suspect (%s) " % suspects)
    suspects.remove(suspectName)    
# removes weapon that was not used
def removeWeapons():
    weaponName = Epic.userString("Enter the weapon not used (%s): " % weapons)
    weapons.remove(weaponName)    
def main():
# variables
    noMoreWeapons = False
    noMoreSuspects = False
    size = possibilities()
# runs the program until suspect and weapon are found
    while size is not 1:
        if len(suspects) is not 1 and len(weapons) is not 1:
            findClue = Epic.userString("Is the clue a weapon or a suspect (w or s): ")
# removes suspects
        if findClue.lower() == "s" and len(suspects) is not 1:
            removeSuspects()
# tells user there is no more suspects and sends them to eliminate weapons
        elif findClue.lower() == "s" and noMoreSuspects:
            print "Killer is found try weapons!"
            removeWeapons()
            findClue = "w"
#tells user there is no more weapons to search through and sends them to eliminate suspects       
        elif noMoreWeapons and findClue.lower() == "w":
            print "Weapon that was used was Found! Need to find Killer!!!"  
            removeSuspects()
            findClue = "s"
# removes weapons 
        elif  findClue.lower() == "w":     
            removeWeapons()
# changes no more suspects and nomore weapons to true to prevent going into that section since it is done
        if len(suspects) == 1:
            noMoreSuspects = True
        if len(weapons) == 1:
            noMoreWeapons = True
        size = possibilities()
#gets the suspect and weapon that did the murder       
    murder = suspects[0]
    tool = weapons[0]
#prints out who did and with what
    print "%s used a %s to commit the murder!" % (murder,tool)                   
#calls main
main()