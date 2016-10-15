from moneylover import *

report, hdr = loadMLWorkbook("2016-10-10.xlsx")
start = "2/10/2016"
end = "12/10/2016"

#report = sortByCategory(report)

splice = spliceDateRange(start, end, report)
if splice == -1:
	print "Error"
	exit()
for entry in splice:
	entry.display()

#for testing:
#test equal start and end dates - passed
#test start and end dates that go out of bounds - passed
#test providing an unsorted list - passed
#test end date that is prior to start date - passed
#test small and large ranges - passed
#test start and end dates that aren't present within list - passed
