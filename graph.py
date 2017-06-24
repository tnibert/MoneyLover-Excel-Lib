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
from matplotlib import cm
import matplotlib.patches as mpatches

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
    categories = categoryamountdict.keys()

    #make colors
    #cmap = cm.prism
    #colors = cmap(len(positivevalues))
    #color=cm.rainbow(np.linspace(0,10,len(categories)*10))
    my_cmap = cm.get_cmap('rainbow')
    colors = plt.cm.Set1(np.linspace(0,1,len(categories)))

    patches = plt.pie(positivevalues, autopct='%1.1f%%', labels=categories, colors=colors, startangle=140) # radius=1.2)

    #categories = categoryamountdict.keys()

    #patches = [patch.label for patch in patches]

    #positivevalues=np.array(positivevalues)

    labels = ['{0} - ${1} - {2:2.2f} %'.format(i,j,k) for i,j,k in zip(categories, positivevalues, [100*(x/sum(positivevalues)) for x in positivevalues])]

    #sort legend
    #patches, labels, dummy =  zip(*sorted(zip(patches, labels, positivevalues),
                                          #key=lambda categories: categories[2],
                                          #reverse=True))

    #plt.legend(patches, categories, loc='best', #bbox_to_anchor=(-0.1, 1.),
    #       fontsize=8)

    #plt.legend(label=categoryamountdict.keys())

    #colors_lables = zip(colors, categories)
    #colors_lables = list(set(colors_lables))
    #lables = [lable for color,lable in colors_lables]

    # create some patchs of colors
    #lables_patchs = []
    #for item in c_l:
        #add_patch = mpatches.Patch(color=item[0], label=item[1])
        #lables_patchs.append(add_patch)

    plt.legend(labels, loc="upper right", bbox_to_anchor=(1.1, 1.05))


    #plt.savefig('piechart.png', bbox_inches='tight')

    plt.axis('equal')
    #plt.tight_layout()
    plt.show()


#new function: graph one category over time
