from moneylover import *

test, hdr = loadMLWorkbook("short.xlsx")
test2 = addEntry(test, "a category", 5000, "this is a test", "cash money", "AUD", "11/11/2016")
#print test
#print test2
exportToNewWorkbook(hdr, test2, "addentryreturn.xlsx")
#print "pass one"
exportToNewWorkbook(hdr, test, "addentryoriginal.xlsx")
