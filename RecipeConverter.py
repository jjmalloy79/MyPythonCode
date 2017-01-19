#Joshua J. Malloy
#RecipeConverter.py
#1-22-2017

#Gets Original Recipe amounts in Cups
print "Enter the amount of Flour (cups):",
flour = raw_input()
print "Enter the amount of water (cups):",
water = raw_input()
print "Enter the amount of salt (teaspoons):",
salt = raw_input()
print "Enter the amount of yeast (teaspoons):",
yeast = raw_input()
print "Enter the loaf adjustment factor (e.g. 2.0 double the size):",
size = raw_input()

#Converting to new size
newFlour = float(flour) * float(size)
newWater = float(water) * float(size)
newSalt = float(salt) * float(size)
newYeast = float(yeast) * float(size)

#Convert into grams
gramFlour = float(newFlour) * 120
gramWater = float(newWater) * 236.59
gramSalt = float(newSalt) * 2
gramYeast = float(newYeast) * 3

#Print Original Recipe
print 
print "-- Original Recipe --"
print "BreadFlour: %s cups." % flour
print "Water: %s cups." % water
print "Salt: %s teaspoons." % salt 
print "Yeast: %s teaspoons." % yeast

#Print Data cups
print 
print "-- Modified Recipe --"
print "BreadFlour: %s cups." % newFlour 
print "Water: %s cups." % newWater
print "Salt: %s teaspoons." % newSalt 
print "Yeast: %s teaspoons." % newYeast

#Print Data grams
print 
print "-- Modified Recipe in Grams --"
print "BreadFlour: %.2f g." % gramFlour
print "Water: %.2f g." % gramWater
print "Salt: %.2f g." % gramSalt
print "Yeast: %.2f g." % gramYeast