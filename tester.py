from moneylover import *
#import calculations as calc

#sortByCategory("test.xlsx")
lsClass, hdr = loadMLWorkbook("sample.xlsx")
#hdr.display()
#for x in lsClass:
#	x.display()
lsList = generateArray(lsClass)
#print lsList
sortedClassList = sortByCategory(lsClass)
#sortedClassList = sortByDate(lsClass)
test = 0
for x in sortedClassList:
	test += 1
separatedcats = spliceByCategory(lsClass)
totalelements = 0
for x in separatedcats:
	if len(x) == 0:
		print "EMPTY"
	else: 
		totalelements += len(x)
		print x[0].category + " " + str(len(x))

print "\n----\n" + str(totalelements)
print "test: " + str(test)
#for x in separatedcats[6]:
#	x.display()
#for x in separatedcats:
#	for y in x:
#		print y.category
#		y.display()

#for x in sortedClassList:
#       x.display()
#exportToNewWorkbook(hdr, sortedClassList, "datesorted.xlsx")
#calc.addByCategory()
