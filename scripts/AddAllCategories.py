from moneylover import *
import sys

#take command line args
try:
	fname = sys.argv[1]
except:
	print "call with python AddAllCategories.py FILENAME"
	exit()


#load file
lsClass, hdr = loadMLWorkbook(fname)

#separate out list by categories
separatedcats = spliceByCategory(lsClass)

#iterate through categories and add up the total prices of each
for category in separatedcats:
	amount = 0
	print category[0].category + " contains " + str(len(category)) + " entries"
	for entry in category:
		amount += entry.amount
	print "Amount: " + str(amount) + "\n"
