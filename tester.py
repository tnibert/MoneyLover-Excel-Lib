from moneylover import *
#import calculations as calc

#sortByCategory("test.xlsx")
lsClass, hdr = loadMLWorkbook("sample.xlsx")
#hdr.display()
#for x in lsClass:
#	x.display()
lsList = generateArray(lsClass)
#print lsList
#sortedClassList = sortByCategory(lsClass)
#sortedClassList = sortByDate(lsClass)
separatedcats = spliceByCategory(lsClass)

for x in separatedcats[6]:
	x.display()
#for x in separatedcats:
#	for y in x:
#		print y.category
#		y.display()

#for x in sortedClassList:
#       x.display()
#exportToNewWorkbook(hdr, sortedClassList, "datesorted.xlsx")
#calc.addByCategory()
