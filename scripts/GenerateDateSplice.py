#call with python GenerateDateSplice.py FILENAME STARTDATE ENDDATE NEWFILENAME
import sys
from moneylover import *

#take command line args
try:
	fname = sys.argv[1]
	startdate = sys.argv[2]
	enddate = sys.argv[3]
	newfname = sys.argv[4]
except:
	print "call with python GenerateDateSplice.py FILENAME STARTDATE ENDDATE NEWFILENAME"
	exit()

#load file
lsClass, hdr = loadMLWorkbook(fname)

#create date splice and show
datesplice = spliceDateRange(startdate, enddate, lsClass)
for x in datesplice:
	x.display()

#write out to a new file
exportToNewWorkbook(hdr, datesplice, newfname)
