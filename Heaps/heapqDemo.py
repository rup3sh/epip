#!/bin/python3

import sys
import itertools
import heapq
import collections

def main(argv):

        print("Running top K ..")
        init_names = ['Ravi', 'Shastri', 'Goverdhan Lal Oberoi', 'Xu Xu', 'Meatloaf']
        names = ['MKD', 'Arnold Swarzenegger', 'Zellwegger', 'Don Juan de marco',
                'Snoop Dogg', 'Mihai Czisentmihailyi', 'Rowan Atkinson', 'FDR',
                'Jalal-u-din-mohd-akbar']

        #heapqDemo()
        records = topKStr(5, init_names, names)
        print("Records: {}".format(records))

        records = leastKStr(5, init_names, names)
        print("Records: {}".format(records))

# As python only has min heap, you have to use negative numbers to get max heap

def leastKStr(k, init_names, stream):
        
        init_list = [(-1*len(s), s) for s in init_names]    
        heapq.heapify(init_list)
        
        for s in stream:
                heapq.heappush(init_list, (-1*len(s),s))
                heapq.heappop(init_list)

        return heapq.nsmallest(5, init_list)

#Demo problem, find K longest names (so we will use a min heap, so that minimums can be removed)
def topKStr(k, init_names, stream):

        #rec = collections.namedtuple('rec', ('len','name'))
        #make a tuple of length & names
        #init_list = [rec(len(s), s) for s in init_names]
        init_list = [(len(s), s) for s in init_names]    
        heapq.heapify(init_list)
        
#       print(init_list[0][0], init_list[0][1])
        #print(init_list[0].len)       
        
        for s in stream:
         
                if len(s) > init_list[0][0]:
                        heapq.heappush(init_list, (len(s),s))
                        heapq.heappop(init_list)
        #print("HEAP:::::::", str(init_list))
        return heapq.nlargest(5, init_list)

def heapqDemo():

        alist = [3,44,656,2,55,66,959,234,1242, 2,24,33,1,55]
        
        heapq.heapify(alist)
        
        print("In-place heapified {}".format(str(alist)))

        largest = heapq.nlargest(3,alist)
        print("Largest:{}".format(str(largest)))        
        
        smallest = heapq.nsmallest(3,alist)
        print("Smallest:{}".format(str(smallest)))        
        
        heapq.heappush(alist, 0)

        print("After push {}".format(str(alist)))

        ##heapq.heappop(alist)
        ##print("After pop {}".format(str(alist)))
        
        min_popped = heapq.heappushpop(alist, 5)
        print("After {} popped, push-pop is {}".format(min_popped, str(alist)))

        print("Peek smallest element without popping {}".format(alist[0]))
if __name__ == "__main__":main(sys.argv[0:])
