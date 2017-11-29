#!/bin/python3

import sys
import itertools
import heapq

def main(argv):

        print("Running binsearch demo..")
        binSearchDemo()

def vanillaBinSearch(elem, arr):

        #TODO Sanity check

        high = len(arr)-1
        low = 0
        print ("In vanilla bin search..")

        while low<=high:

                middle = (high-low)//2 + low
                print("Middle:{}".format(middle))
                if arr[middle]==elem:
                        return True
                elif arr[middle]>elem:
                        high = middle-1
                else:
                        low = middle+1
        return False
        
def binSearchDemo():

        sortedlist = [3,44,55,60,67,89,90,99,101,102,123,242,1245,4565]
        
        element = 203
        element = 4565
        element = 1245   

        isThere = vanillaBinSearch(element, sortedlist)
        if isThere:
                print("Element {} found.".format(element))
        else:
                print("Elem not found")

if __name__ == "__main__":main(sys.argv[0:])
