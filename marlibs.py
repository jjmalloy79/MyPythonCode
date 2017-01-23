# Import Epic to getlyric function
import Epic
#print "Enter the first verse:",
adjective1 = Epic.get_input("Enter adjective:")
adjective2 = Epic.get_input("Enter another adjective:")
noun1 = Epic.get_input("Enter plural noun:")
noun2 = Epic.get_input("Enter another plural noun:")
noun3 = Epic.get_input("Enter a celebrity:")
noun4 = Epic.get_input("Enter a noun:")

sentence = ("In the shadowy world of spies, a/an adj1 organisation like the US government uses spies to infiltrate adj2 groups" 
           "with the purpose of top secret n1. A teacher, n3, or even the little old n4 with a cane and fifteen"
           "pet n2 could be a spy." )

sentence = sentence.replace("adj1", adjective1)
sentence = sentence.replace("adj2", adjective2)
sentence = sentence.replace("n1", noun1)
sentence = sentence.replace("n2", noun2)
sentence = sentence.replace("n3", noun3)
sentence = sentence.replace("n4", noun4)

print sentence

