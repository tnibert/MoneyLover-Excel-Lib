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
import matplotlib.patches as mpatches
#from pylab import rcParams
#rcParams['figure.figsize'] = 25, 15

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
    return plt


#create a pie graph of all categories
def categoryPieGraph(rowlist, type=0):
    """
    takes argument of mlRow list and type of data to graph (negative number is spending, positive is income, 0 is all)
    returns pyplot
    """

    #prepare our inputs

    categoryamountdict = tallyCategories(rowlist)

    if(type > 0):           #if graphing income
        for i, j in categoryamountdict.items():
            if j <= 0:
                categoryamountdict.pop(i)
    elif(type < 0):         #if graphing expenses
        for i, j in categoryamountdict.items():
            if j >= 0:
                categoryamountdict.pop(i)
    positivevalues = map(abs, categoryamountdict.values())
    categories = categoryamountdict.keys()

    #make colors
    colors = plt.cm.Set1(np.linspace(0,1,len(categories)))

    #set figure size to accomodate legend
    plt.figure(figsize=(20,10))

    #create pie chart
    patches = plt.pie(positivevalues, autopct='%1.1f%%', labels=categories, colors=colors, startangle=140)

    #generate labels for legend
    labels = ['{0} - ${1} - {2:2.2f} %'.format(i,j,k) for i,j,k in zip(categories, positivevalues, [100*(x/sum(positivevalues)) for x in positivevalues])]

    #plt.legend(patches, categories, loc='best', #bbox_to_anchor=(-0.1, 1.), (1.1, 1.05)
    #       fontsize=8)

    #create legend
    plt.legend(labels, bbox_to_anchor=(1.1, 1), fontsize=10)


    #plt.savefig('piechart.png', bbox_inches='tight')

    plt.axis('equal')
    #plt.tight_layout()
    plt.show()
    return plt


#new function: graph one category over time - bar graph
