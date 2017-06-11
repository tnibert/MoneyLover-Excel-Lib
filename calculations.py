from moneylover import *

#take a list and add together all of the amounts in each category
#return a hash table
#def addAmountByCategory(mlRowList):
	#making a design decision between taking a presorted list or sorting it on the fly
	#for now we sacrifice cpu cycles so others can be lazy
#	sortedList = sortByCategory(mlRowList)

	#compare row's category with the previous row's category
	#if they are the same, add together
	#if they are different, push the previous added value into the hash w/ category name
	#and begin anew

	#have to pop first element off of sortedList
#	for row in sortedList:

#	return

#take a rowlist and start and end dates as args, return a dict of category:amount
def tallyCategories(rowlist, startdate=-1, enddate=-1):

    #separate out list by categories
    separatedcats = spliceByCategory(rowlist)

    tallydict = {}

    #iterate through categories and add up the total prices of each
    for category in separatedcats:
        amount = 0
	    #print(category[0].category + " contains " + str(len(category)) + " entries")
        for entry in category:
            amount += entry.amount
	    #print("Amount: " + str(amount) + "\n")
        tallydict[category[0].category] = amount

    return tallydict
