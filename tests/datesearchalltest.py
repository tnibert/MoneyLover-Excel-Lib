from moneylover import *

report, hdr = loadMLWorkbook("2016-10-10.xlsx")
#date = datetime.datetime.strptime("6/17/2016", "%m/%d/%Y")
report = sortByDate(report)
test = dateSearchAll("7/29/2016", report)
print test
if test == -1:
	print "NOT FOUND"
	exit()
for i in test:
	report[i].display()

#test date with many, with one, with none
#consider a shift to solely utilizing datetime objects in interface
#run through list with a flag on the function section suspected unneeded
