from moneylover import *
from graph import *
import sys

#take command line args
try:
    fname = sys.argv[1]
except:
    print("call with python categorybargraph.py FILENAME")
    exit()

success = True

#load file
lsClass, hdr = loadMLWorkbook(fname)

#test the function
categoryBarGraph(lsClass)

