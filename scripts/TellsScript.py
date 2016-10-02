#so the missus said give me all groceries from June 6 2016 onward that cost over $30
#tada
from moneylover import *
import sys

try:
	fname = sys.argv[1]
	categoryname = "Groceries"
except:
	print "call with python TellsScript.py FILENAME"
	exit()

lsClass, hdr = loadMLWorkbook(fname)

correctcategory = []

spliceDateRange("06/06/2016", "10/02/3016", lsClass)

separatedcats = spliceByCategory(lsClass)
for type in separatedcats:
	if(type[0].category == categoryname):
		correctcategory = type
		break

if(correctcategory == []):
	print "Category not found"
	exit()

amount = 0
print correctcategory[0].category + " contains " + str(len(correctcategory)) + " entries\n"

criteriatransactions = 0

for entry in correctcategory:
	if(entry.amount < -30):
		entry.display()
		amount += entry.amount
		criteriatransactions += 1

print str(criteriatransactions) + " transactions over $30 from 6th of June 2016"
print "Total Amount of transactions over $30: $" + str(amount) + "\n"
