#! /usr/bin/env python

#plan for the moment:
#implement a bar graph of amount in each category
#different colors for negative and positive values, maybe side by side?
#splice by category, then by date, then add the values of each category together.  Maybe separate into negatives and positives, probably create a tally function to do all of this.

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def categorybargraph(rowlist):
    categorysplit = spliceByCategory(rowlist)
    objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    y_pos = np.arange(len(objects))
    performance = [10,8,6,4,2,1]
 
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')

    plt.show()
