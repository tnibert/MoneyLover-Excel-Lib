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
		print self.id
		print self.category
		print self.amount
		print self.note
		print self.wallet
		print self.currency
		print self.date

		print "\n"

#take a file name as argument and return tuple containing previously mentioned list of mlRow classes and header
def loadMLWorkbook(workbkfname):
	#load MoneyLover generated workbook
	originalWorkbook = openpyxl.load_workbook(workbkfname)
	originalSheet = originalWorkbook.active

	#list of rows in mlRow class format
	rowClassList = []
	header = mlRow(tuple(originalSheet.rows)[0])		#figure out how to keep green color for header

	for line in range(1, originalSheet.max_row):		#start at 1, line 0 is category names
		#print tuple(originalSheet.rows)[1]
		rowClassList.append(mlRow(tuple(originalSheet.rows)[line]))
	return rowClassList, header	#returns list of mlRow objects, header


#take the mlRow class list and generate a double indexed array
#return said double indexed array
#the purpose for this is that it is easier to work with in some contexts
#for example, writing out to a new excel file
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
	for elem in workbklist:
		elem.date = datetime.datetime.strptime(elem.date, "%m/%d/%Y")	#turn into datetime obj
	sortedlist = sorted(workbklist, key=attrgetter('date'))
	for elem in workbklist:
		elem.date = datetime.datetime.strftime(elem.date, "%m/%d/%Y")	#restore to original text formate
	return sortedlist

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

#takes three arguments, the first two are date strings in mm/dd/yyyy format, the third is the list to splice from
#returns the spliced list, returns original list if unable to splice
def spliceDateRange(startdate, enddate, workbklist):
#what if there is no transactions on one of the start or end dates?
#we must find all dates WITHIN THE RANGE
	try:
		dtstartdate = datetime.datetime.strptime(startdate, "%m/%d/%Y")
		dtenddate = datetime.datetime.strptime(enddate, "%m/%d/%Y")
	except:
		print "incorrect date format passed"
		return workbklist	#return original list

	datesortedlist = sortByDate(workbklist)
	for elem in datesortedlist:			#bah
                elem.date = datetime.datetime.strptime(elem.date, "%m/%d/%Y")   #turn into datetime obj

	#find first instance of startdate using binary search
	#startindex=len(datesortedlist)/2
	#while(datesortedlist[startindex].date != dtstartdate):
	#	print datesortedlist[startindex].date
	#	if(dtstartdate < datesortedlist[startindex].date):
	#		startindex = startindex/2
	#		print "down " + str(startindex)
	#	elif(dtstartdate > datesortedlist[startindex].date):
	#		startindex = startindex+(startindex/2)
	#		print "up " + str(startindex)
	index = datesortedlist.index(dateSearch(dtstartdate, datesortedlist))
	print index

	print datesortedlist[index].date
	return 0

#recursive function for binary search
#and the challenge is to return an index for the original list
#right now it returns the object, we might be able to use it with 
def dateSearch(date, lst):
	#base case here
	if len(lst) == 1:
		return lst[0]

	mid = len(lst)/2
	print "length: " + str(len(lst)) + " mid: " + str(mid)
	if lst[mid].date > date:
		return dateSearch(date, lst[:mid])
	elif lst[mid].date < date:
		return dateSearch(date, lst[mid+1:])
	else:
		return lst[mid]

#provide mlRows list as an argument and write it out to a new excel file specified by string newFileName
def exportToNewWorkbook(header, mlWkbkClassList, newFileName):
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

