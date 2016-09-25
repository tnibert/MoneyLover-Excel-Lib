from moneylover import *
#import calculations as calc

#sortByCategory("test.xlsx")
lsClass, hdr = loadMLWorkbook("test.xlsx")
hdr.display()
#for x in lsClass:
#	x.display()
lsList = generateArray(lsClass)
#print lsList
sortedClassList = sortByCategory(lsClass)
#for x in sortedClassList:
#       x.display()
exportToNewWorkbook(hdr, sortedClassList, "testexport.xlsx")
#calc.addByCategory()
