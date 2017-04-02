#Exam 4: This program will ask user for a word that they want to find in different files,
#it will print out the name of the file the word was found in and the line it was in.
# import section 
import os
import Epic

#this gets a list of all files in dir and places into a string called files
files = os.listdir(".")

#this section reads in files and searches for term and returns an array
def searchFor(term):
#varable section
    location = []
    temp = ""
    count  = 0
    #opens a file
#this goes through all files in directory   
    for file in files:
        if file.endswith(".txt"):
            infile = open(file)
# goes through each line
            for lines in infile:
# puts all words to upper case and sees if term or user word is in sentence
                if term.upper() in lines.upper():
#puts filename and sentence users word appears in into a temp string to 
#add to 
                    count = count + 1
                    temp =  str(file) + ': ' + lines.strip()
                    location.append(temp)
    printOut(count, location)
#prints out file name, how many times it was found, and location it was found
def printOut(count, fileList):
#prints out how many times the word was found
    print "I found %s results." % count
    for i in fileList:
        print i
#this is the main function
def main():

# this gets the word the user wants to look for by calling a function
#in the epic file.
    term = Epic.userString("Enter a search term:")
    
#this gather all locations where users words were found
    searchFor(term)
    
#calls main to start program    
main()