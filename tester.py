from moneylover import *
#import calculations as calc

#sortByCategory("test.xlsx")
lsClass, hdr = loadMLWorkbook("catsorted.xlsx")
hdr.display()
#for x in lsClass:
#	x.display()
lsList = generateArray(lsClass)
#print lsList
#sortedClassList = sortByCategory(lsClass)
sortedClassList = sortByDate(lsClass)
#for x in sortedClassList:
#       x.display()
exportToNewWorkbook(hdr, sortedClassList, "datesorted.xlsx")
#calc.addByCategory()
