from moneylover import *
import sys
from calculations import *

#take command line args
try:
	fname = sys.argv[1]
except:
	print("call with python tallyCategories.py FILENAME")
	exit()

success = True

#load file
lsClass, hdr = loadMLWorkbook(fname)

#test the function
test = tallyCategories(lsClass)

#separate out list by categories
separatedcats = spliceByCategory(lsClass)

#iterate through categories and add up the total prices of each
for category in separatedcats:
    amount = 0
    print(category[0].category + " contains " + str(len(category)) + " entries")
    for entry in category:
        amount += entry.amount
    print("Amount: " + str(amount) + "\n")
    if(test[category[0].category] != amount):
        success = False


#print resulting dict from tallyCategories()
print test

if(success):
    print("\ntallyCategories() test passed")
else:
    print("\ntallyCategories() test failed")
