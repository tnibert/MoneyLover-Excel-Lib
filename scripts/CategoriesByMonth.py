#script to splice into one month date blocks and tell how much was spent in each category in each month
#6/01/2016 - 10/01/2016
from moneylover import *
import sys

#take command line argument
try:
	fname = sys.argv[1]
except:
	print "call with python CategoriesByMonth.py FILENAME"
	exit()

#load file
record, hdr = loadMLWorkbook(fname)

#create a category divided double indexed array
record = spliceByCategory(record)

for category in record:
	months = []
	
	#create date splices
	month1 = spliceDateRange("06/01/2016", "07/01/2016", category)
        month2 = spliceDateRange("07/02/2016", "08/01/2016", category)
	month3 = spliceDateRange("08/02/2016", "09/01/2016", category)
        month4 = spliceDateRange("09/02/2016", "10/01/2016", category)

	#add splices to an iterable list
	months.append(month1)
	months.append(month2)
	months.append(month3)
	months.append(month4)

	#print each category and within each category add up amounts for each month
	#and display
	print "Category: " + category[0].category
	i = 1
	for month in months:
		amount = 0
		for entry in month:
			amount += entry.amount
		print "\t" + "Month " + str(i) + ": " + str(amount)
		i+=1
