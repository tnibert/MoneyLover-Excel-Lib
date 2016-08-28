from moneylover import *
import calculations as calc

#sortByCategory("test.xlsx")
lsClass = loadMLWorkbook("test.xlsx")
#lsList = rowsToList(lsClass)
#print lsList
#sortedClassList = sortByCategory(lsClass)
#for x in sortedClassList:
#       x.display()
#exportToNewWorkbook(sortedClassList, "testexport.xlsx")
calc.addByCategory()
