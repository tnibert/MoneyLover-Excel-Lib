from moneylover import *

#this file has more high level functions for tasks

#take a rowlist and start and end dates as args, return a dict of category:amount
def tallyCategories(rowlist, startdate=-1, enddate=-1):
#still need to implement date splicing

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
