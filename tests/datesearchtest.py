from moneylover import *

report, hdr = loadMLWorkbook("2016-10-10.xlsx")
date = datetime.datetime.strptime("10/10/2016", "%m/%d/%Y")
test = dateSearch(date, report)
print type(test)
print test
test.display()

#implement checking for datetime object in dateSearch()
#implement a function to convert date strings to datetime object

#returning last item in date

#checking a date with lots of entries, a date with one entry, and a date with no entries
#start of list and end of list
