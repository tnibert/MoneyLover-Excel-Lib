#script to splice into one month date blocks and tell how much was spent in each category in each month
#6/14/2016 - 10/10/2016
from moneylover import *

record, hdr = loadMLWorkbook("2016-10-10.xlsx")

#generate double indexed array of [category][entry]
record = spliceByCategory(record)

for category in record:
	months = []

#	for x in category:
#		x.display()

	test1 = spliceDateRange("06/14/2016", "07/14/2016", category)
        test2 = spliceDateRange("07/15/2016", "08/14/2016", category)
	test3 = spliceDateRange("08/15/2016", "09/14/2016", category)
        test4 = spliceDateRange("09/15/2016", "10/14/2016", category)

	months.append(test1)
	months.append(test2)
	months.append(test3)
	months.append(test4)

	print "Category: " + category[0].category
	i = 1
	#outputstring = ""
	for month in months:
		amount = 0
		for entry in month:
			amount += entry.amount
		print "\t" + "Month " + str(i) + ": " + str(amount)
		i+=1
		#for entry in month:
		#	entry.display()
	#outputstring += "\n"
	#print outputstring
