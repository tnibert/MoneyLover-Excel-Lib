#call with python GenerateDateSplice.py FILENAME STARTDATE ENDDATE NEWFILENAME
import sys
from moneylover import *

try:
	fname = sys.argv[1]
	startdate = sys.argv[2]
	enddate = sys.argv[3]
	newfname = sys.argv[4]
except:
	print "call with python GenerateDateSplice.py FILENAME STARTDATE ENDDATE NEWFILENAME"
	exit()

lsClass, hdr = loadMLWorkbook(fname)

datesplice = spliceDateRange(startdate, enddate, lsClass)
for x in datesplice:
	x.display()

exportToNewWorkbook(hdr, datesplice, newfname)
