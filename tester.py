from moneylover import *
#import calculations as calc

#sortByCategory("test.xlsx")
lsClass, hdr = loadMLWorkbook("category.xlsx")
#hdr.display()
#for x in lsClass:
#	x.display()
lsList = generateArray(lsClass)
#print lsList

test = spliceDateRange("07/05/2016", "07/12/2016", lsClass)
#for x in test:
#	x.display()

#sortedClassList = sortByCategory(lsClass)
#sortedClassList = sortByDate(lsClass)
#indexlist = dateSearchAll("7/05/2016", sortedClassList)
#for i in indexlist:
#	sortedClassList[i].display()
#test = 0
#for x in sortedClassList:
#	test += 1
#separatedcats = spliceByCategory(lsClass)
#totalelements = 0
#for x in separatedcats:
#	if len(x) == 0:
#		print "EMPTY"
#	else: 
#		amount = 0
#		totalelements += len(x)
#		print x[0].category + " " + str(len(x))
#		for y in x:
#			amount += y.amount
#		print "amount: " + str(amount)

#for x in separatedcats[2]:
#	x.display()

#print "\n----\n" + str(totalelements)
#print "test: " + str(test)
#for x in separatedcats[6]:
#	x.display()
#for x in separatedcats:
#	for y in x:
#		print y.category
#		y.display()

#for x in sortedClassList:
#       x.display()
exportToNewWorkbook(hdr, test, "datesplice.xlsx")
#calc.addByCategory()
