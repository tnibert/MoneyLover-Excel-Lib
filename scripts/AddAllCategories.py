from moneylover import *
import sys

try:
	fname = sys.argv[1]
except:
	print "call with python AddAllCategories.py FILENAME"
	exit()


lsClass, hdr = loadMLWorkbook(fname)

separatedcats = spliceByCategory(lsClass)
for x in separatedcats:
	if len(x) == 0:
		print "EMPTY"
	else: 
		amount = 0
		print x[0].category + " contains " + str(len(x)) + " entries"
		for y in x:
			amount += y.amount
		print "Amount: " + str(amount) + "\n"
