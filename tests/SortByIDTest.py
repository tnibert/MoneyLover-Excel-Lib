#test of sortByID() function
from moneylover import *

test, hdr = loadMLWorkbook("spreadsheets/category.xlsx")
sortedlist = sortByID(test)
exportToNewWorkbook(hdr, sortedlist, "idsorted.xlsx")
