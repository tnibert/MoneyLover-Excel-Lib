from moneylover import *
import sys

#take command line args
try:
	fname = sys.argv[1]
	categoryname = sys.argv[2]
except:
	print("call with python DisplayCategory.py FILENAME CATEGORYNAME")
	print("if CATEGORYNAME is multiple words, enclose in quotes")
	exit()

#load file
lsClass, hdr = loadMLWorkbook(fname)

correctcategory = []

#splice category and find the correct category
separatedcats = spliceByCategory(lsClass)
for type in separatedcats:
	if(type[0].category == categoryname):
		correctcategory = type
		break

#check for if category exists
if(correctcategory == []):
	print("Category not found")
	exit()

#init amount variable and print how many entries
amount = 0
print(correctcategory[0].category + " contains " + str(len(correctcategory)) + " entries\n")

#display entries in category and calculate total
for entry in correctcategory:
	entry.display()
	amount += entry.amount

print("Total Amount: $" + str(amount) + "\n")
