#this script tests the getByID() function and the idSearch() function
from moneylover import *

test, hdr = loadMLWorkbook("spreadsheets/category.xlsx")

#toGenerateID = sortByID(test)
#rand in range?
ids = [1, 10, 50, 20000, 24, 90, 147]

for id in ids:
	print "Testing: " + str(id)
	obj = getByID(test, id)
	try: obj.display()
	except AttributeError: print obj	#if obj is not mlRow
