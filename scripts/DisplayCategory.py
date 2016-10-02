from moneylover import *
import sys

try:
	fname = sys.argv[1]
	categoryname = sys.argv[2]
except:
	print "call with python DisplayCategory.py FILENAME CATEGORYNAME"
	print "if CATEGORYNAME is multiple words, enclose in quotes"
	exit()

lsClass, hdr = loadMLWorkbook(fname)

correctcategory = []

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

for entry in correctcategory:
	entry.display()
	amount += entry.amount

print "Total Amount: $" + str(amount) + "\n"
