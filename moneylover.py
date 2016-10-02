import openpyxl
from operator import attrgetter
import datetime

#this class is a MoneyLover row
#each row in the excel file becomes a class
#we use a list of these to represent the whole file
class mlRow():
	def __init__(self, wbRow):
		#wbRow is the row list as passed from the original sheet.rows[index] list returned
		self.id = wbRow[0].value
		self.category = wbRow[1].value
		self.amount = wbRow[2].value
		self.note = wbRow[3].value
		self.wallet = wbRow[4].value
		self.currency = wbRow[5].value
		self.date = wbRow[6].value
	def display(self):
		print "ID: " + str(self.id)
		print "Category: " + str(self.category)
		print "Amount: $" + str(self.amount)
		print "Note: " + str(self.note)
		print "Wallet: " + str(self.wallet)
		print "Currency: " + str(self.currency)
		print "Date: " + str(self.date)
		print ""

#take a file name as argument and return tuple containing previously mentioned list of mlRow classes and header
def loadMLWorkbook(workbkfname):
	#load MoneyLover generated workbook
	originalWorkbook = openpyxl.load_workbook(workbkfname)
	originalSheet = originalWorkbook.active

	#list of rows in mlRow class format
	rowClassList = []
	header = mlRow(tuple(originalSheet.rows)[0])		#figure out how to keep green color for header

	for line in range(1, originalSheet.max_row):		#start at 1, line 0 is category names (header)
		#print tuple(originalSheet.rows)[1]
		rowClassList.append(mlRow(tuple(originalSheet.rows)[line]))

	#convert all dates to datetime objects
	#we may want to put this in the mlRow constructor
	for elem in rowClassList:
                elem.date = datetime.datetime.strptime(elem.date, "%m/%d/%Y")

	return rowClassList, header	#returns list of mlRow objects, header


#take the mlRow class list and generate a double indexed array
#return said double indexed array
#the purpose for this is that it is easier to work with in some contexts
#for example, writing out to a new excel file
#I believe that currently that is the only place this is used... be on look out for problems with datetime object conversions...
def generateArray(rowClassList):	#takes argument of mlRows class and converts to a conventional array
	numRows = len(rowClassList)
	rowArrayList = []		#array is [rows][columns]
	
	for i in range(0, numRows):
		rowArrayList.append([])		#create first index of array

		#create second index
		rowArrayList[i].append(rowClassList[i].id)
		rowArrayList[i].append(rowClassList[i].category)
		rowArrayList[i].append(rowClassList[i].amount)
		rowArrayList[i].append(rowClassList[i].note)
		rowArrayList[i].append(rowClassList[i].wallet)
		rowArrayList[i].append(rowClassList[i].currency)
		rowArrayList[i].append(rowClassList[i].date)

	return rowArrayList


#take the mlRows list as an argument, sort it, and return the sorted list
def sortByCategory(workbklist):	

	return sorted(workbklist, key=attrgetter('category'))

def sortByDate(workbklist):

	return sorted(workbklist, key=attrgetter('date'))

#splice mlRows list based on criteria, return list of uniform category lists
def spliceByCategory(workbklist):
	catsortedlist = sortByCategory(workbklist)
	workinglist = []
	workinglist.append(catsortedlist[0])		#what if passed empty list?
	toreturn = []
	i = 0
	while(i < len(catsortedlist)-1):
		if(catsortedlist[i].category == catsortedlist[i+1].category):
			workinglist.append(catsortedlist[i+1])
		else:
			toreturn.append(workinglist)
			workinglist = []
			workinglist.append(catsortedlist[i+1])
		i+=1

	toreturn.append(workinglist)
	return toreturn

#CURRENT WORKING PLACE
#takes three arguments, the first two are date strings in mm/dd/yyyy format, the third is the list to splice from
#returns the spliced list sorted by date, returns original list if unable to splice
def spliceDateRange(startdate, enddate, workbklist):
#what if there is no transactions on one of the start or end dates?
#we must find all dates WITHIN THE RANGE
#we must verify that startdate is before enddate
	try:
		dtstartdate = datetime.datetime.strptime(startdate, "%m/%d/%Y")
		dtenddate = datetime.datetime.strptime(enddate, "%m/%d/%Y")
	except:
		print "incorrect date format passed"
		return workbklist	#return original list
	
	#there may be a chance that one of the next three statements is removing a row or two
	#correct entries are returned but the indexes might be wrong...
	datesortedlist = sortByDate(workbklist)		#sort the list by date
	
	startindexes = dateSearchAll(startdate, datesortedlist)
	endindexes = dateSearchAll(enddate, datesortedlist)
#	for x in startindexes:
#		datesortedlist[x].display()
#	for x in endindexes:
#		datesortedlist[x].display()

	begin = startindexes[0]
	end = endindexes[-1]
#	print endindexes
#	print endindexes[-1]
	workinglist = []
	for i in range(begin, end+1):
		workinglist.append(datesortedlist[i])

	return workinglist

#recursive function for binary search
#returns object of first instance found of given date
#takes a datetime object and a sorted mlRow class list as arguments
#for internal library use, reference directly from your code at your own peril
def dateSearch(date, lst):
	#base case here
	if len(lst) == 1:
		return lst[0]

	mid = len(lst)/2
	#print "length: " + str(len(lst)) + " mid: " + str(mid)
	if lst[mid].date > date:
		return dateSearch(date, lst[:mid])
	elif lst[mid].date < date:
		return dateSearch(date, lst[mid:])	#originally mid+1, 
							#apparently changing it allows us to search outside bounds of list 
							#and return closest item
	else:
		return lst[mid]

#we must implement a way to enforce sorted vs unsorted lists

#takes a date string in "mm/dd/yyyy" format and a sorted mlRow list as arguments
#returns a list of the indexes of all entries on that date
def dateSearchAll(date, sortedlist):
	try:
		date = datetime.datetime.strptime(date, "%m/%d/%Y")		#convert date to a datetime object
	except:
		print "invalid format"
		return 0

	#get the index from the object returned by dateSearch()
	index = sortedlist.index(dateSearch(date, sortedlist))
	workinglist = []
	i = index
	
	#verify that both loops work
	
	#scan list forward
	while(i < len(sortedlist) and sortedlist[index].date == sortedlist[i].date):
		workinglist.append(i)
		i+=1
	#scan list backward
	i = index-1
	while(i >= 0 and sortedlist[index].date == sortedlist[i].date):
		workinglist.append(i)
		i-=1
	workinglist.sort()
	return workinglist

#provide mlRows list as an argument and write it out to a new excel file specified by string newFileName
def exportToNewWorkbook(header, mlWkbkClassList, newFileName):
	for elem in mlWkbkClassList:
		elem.date = datetime.datetime.strftime(elem.date, "%m/%d/%Y")   #restore date to original text format

	#we use the generateArray() function so that we can double iterate
	#with for loops and easily assign the cells in the new sheet
	mlWkbkClassList.insert(0, header)
	genArray = generateArray(mlWkbkClassList)

	newWorkbook = openpyxl.Workbook()
	newSheet = newWorkbook.active

	i = 1		#sometimes I wish I was working in C
	for arrObj in genArray:		#for each row
		for j in range(0,7):	#for each column
			newSheet.cell(row=i, column=(j+1)).value = arrObj[j]
		i+=1

	newWorkbook.save(newFileName)
