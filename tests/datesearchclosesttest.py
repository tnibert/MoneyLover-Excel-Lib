from moneylover import *

#str = "10/9/2016"	#passed
str = "10/2/2016"	#passed
#str = "11/15/2016"	#passed
#str = "2/13/2016"	#passed


report, hdr = loadMLWorkbook("2016-10-10.xlsx")
report = sortByDate(report)
print "Testing on: " + str
print "up"
print dateSearchClosest(str, 1, report) 
print "down"
print dateSearchClosest(str, -1, report)
