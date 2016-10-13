from moneylover import *

str = "10/9/2016"
print "Testing on: " + str
date = convertStrToDatetime(str)
print type(date)
print date
date = convertDatetimeToStr(date)
print type(date)
print date
