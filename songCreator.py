#Joshua J. Malloy
#songCreator.py
#1-29-2017

# Import Epic to get_input function
import Epic
#print "Enter the first verse:",
verse1 = Epic.get_input("Enter the first verse:")
verse2 = Epic.get_input("Enter the second verse:")
verse3 = Epic.get_input("Enter the third verse:")
verse4 = Epic.get_input("Enter the forth verse:")
chorus = Epic.get_input("Enter the chorus:")

# removes bad word cookie
verse1 = Epic.remove_cookie(verse1)
verse2 = Epic.remove_cookie(verse2)
verse3 = Epic.remove_cookie(verse3)
verse4 = Epic.remove_cookie(verse4)
chorus = Epic.remove_cookie(chorus).lower()

#Gets how many times to repeat Chorus
repeat = Epic.get_int("Enter the chorus repeat:")
chorus = chorus + " "
#Set song first half
song = [verse1, (chorus * repeat), verse2, (chorus * repeat), verse3, (chorus * repeat), verse4, (chorus * (repeat + 1)) ]

# adds one more time to song
repeat = ["...one more time!..." ]

# repeats the song and puts it into a list
lyrics = song
for i in range(2): 
      if i == 0:
          lyrics = lyrics + repeat
      else:
           lyrics = lyrics + song
           
# prints the list out
print lyrics

for words in lyrics:
    print " %s" % words

