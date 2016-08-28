import openpyxl
from operator import attrgetter

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


#take a file name as argument and return previously mentioned list of mlRow classes
def loadMLWorkbook(workbkfname):
	#load MoneyLover generated workbook
	originalWorkbook = openpyxl.load_workbook(workbkfname)
	originalSheet = originalWorkbook.active

	#list of rows in mlRow class format
	rowClassList = []

	for line in range(1, originalSheet.max_row):
		rowClassList.append(mlRow(originalSheet.rows[line]))
	return rowClassList	#returns list of mlRow objects


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


#provide mlRows list as an argument and write it out to a new excel file specified by string newFileName
def exportToNewWorkbook(mlWkbkClassList, newFileName):
	#we use the generateArray() function so that we can double iterate
	#with for loops and easily assign the cells in the new sheet
	genArray = generateArray(mlWkbkClassList)

	newWorkbook = openpyxl.Workbook()
	newSheet = newWorkbook.active

	i = 1		#sometimes I wish I was working in C
	for arrObj in genArray:		#for each row
		for j in range(0,6):	#for each column
			newSheet.cell(row=i, column=(j+1)).value = arrObj[j]
		i+=1

	newWorkbook.save(newFileName)

