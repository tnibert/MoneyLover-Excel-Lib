from moneylover import *

test, hdr = loadMLWorkbook("short.xlsx")
test2 = removeEntry(test, test[0])	#the modification affects the original passed list 
					#AND the original list that has been modified is returned
exportToNewWorkbook(hdr, test, "remove1.xlsx")
exportToNewWorkbook(hdr, test2, "remove2.xlsx")

#noticed that short.xlsx had IDs '20, '21 etc
#whereas remove.xlsx had 20, 21, etc
#hmm...
