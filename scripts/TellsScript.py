#so the missus said give me all groceries from June 6 2016 onward that cost over $30
#tada
from moneylover import *
import sys

#Take command line arg and assign category
try:
	fname = sys.argv[1]
	categoryname = "Groceries"
except:
	print "call with python TellsScript.py FILENAME"
	exit()

#load excel file
lsClass, hdr = loadMLWorkbook(fname)

correctcategory = []

#create a date splice with a time faaaarrrr in the future
lsClass = spliceDateRange("06/06/2016", "10/02/3016", lsClass)

#separate into different categories, double indexed array
separatedcats = spliceByCategory(lsClass)

#find the category
for type in separatedcats:
	if(type[0].category == categoryname):
		correctcategory = type
		break

#if we didn't find it
if(correctcategory == []):
	print "Category not found"
	exit()

#initialize amount variable and print category data
amount = 0
print correctcategory[0].category + " contains " + str(len(correctcategory)) + " entries\n"

criteriatransactions = 0

#add up all transactions costing over $30
for entry in correctcategory:
	if(entry.amount < -30):
		entry.display()
		amount += entry.amount
		criteriatransactions += 1

#display information
print str(criteriatransactions) + " transactions over $30 from 6th of June 2016"
print "Total Amount of transactions over $30: $" + str(amount) + "\n"
