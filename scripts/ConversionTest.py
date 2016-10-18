from moneylover import *

datestr1 = "7/4/2016"
datestr2 = "7/8/2016"
dateobj1 = convertStrToDatetime(datestr1)
dateobj2 = convertStrToDatetime(datestr2)

report, hdr = loadMLWorkbook("2016-10-15.xlsx")

indexlist1 = dateSearchAll(datestr1, report)
closestdate1 = dateSearchClosest(datestr1, 1, report)
splice1 = spliceDateRange(datestr1, datestr2, report)

indexlist2 = dateSearchAll(dateobj1, report)
closestdate2 = dateSearchClosest(dateobj1, 1, report)
splice2 = spliceDateRange(dateobj1, dateobj2, report)

if(closestdate1 == closestdate2):
	print "dateSearchClosest() passed"
	print closestdate1
	print closestdate2

if(indexlist1 == indexlist2):
	print "dateSearchAll() passed"
	print indexlist1
	print indexlist2

if(splice1 == splice2):
	print "spliceDateRange() passed"
	for x in splice1: x.display()
	for x in splice2: x.display()
