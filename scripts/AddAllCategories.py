from moneylover import *
import sys

try:
	fname = sys.argv[1]
except:
	print "call with python AddAllCategories.py FILENAME"
	exit()


lsClass, hdr = loadMLWorkbook(fname)

separatedcats = spliceByCategory(lsClass)
for category in separatedcats:
	amount = 0
	print category[0].category + " contains " + str(len(category)) + " entries"
	for entry in category:
		amount += entry.amount
	print "Amount: " + str(amount) + "\n"
