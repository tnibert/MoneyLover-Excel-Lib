#! /usr/bin/env python

#plan for the moment:
#implement a bar graph of amount in each category
#different colors for negative and positive values, maybe side by side?
#splice by category, then by date, then add the values of each category together.  Maybe separate into negatives and positives, probably create a tally function to do all of this.

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from moneylover import *
from calculations import *

def categoryBarGraph(rowlist):
    categoryamountdict = tallyCategories(rowlist)

    #plt.bar(range(len(categoryamountdict)), categoryamountdict.values(), align='center')
    plt.bar(np.arange(len(categoryamountdict)), categoryamountdict.values(), align='center', alpha=0.5)
    plt.xticks(np.arange(len(categoryamountdict)), categoryamountdict.keys())
    plt.ylabel('Amount')
    plt.title('Spending By Category')
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=30, horizontalalignment='right')

    plt.show()


#create a pie graph of all categories
def categoryPieGraph(rowlist):
    categoryamountdict = tallyCategories(rowlist)
    positivevalues = map(abs, categoryamountdict.values())

    plt.pie(positivevalues, labels=categoryamountdict.keys(), autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()


#new function: graph one category over time
