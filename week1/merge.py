#!/usr/bin/env python3
import copy
from heapq import merge as mg
"""
Suppose we have two lists L1 and L2 that contain integers which are sorted in ascending order. Create a function merge that gets these lists as parameters and returns a new sorted list L that has all the elements of L1 and L2. So, len(L) should equal to len(L1)+len(L2). Do this using the fact that both lists are already sorted. You can’t use the sorted function or the sort method in implementing the merge method. You can however use these functions in the main function for creating inputs to the merge function. Test with a couple of examples in the main function that your solution works correctly.

Note: In Python argument lists are passed by reference to the function, they are not copied! Make sure you don’t modify the original lists of the caller.
"""

def merge(L1, L2):
	L = list(mg(L1, L2)) 
	print(L)
	return L

def main():
	L1 = [-91, -87, -81, -78, -72, -33, -31, -23, -21, 1, 22, 25, 34, 44, 50, 58, 61, 66, 78,80]
	L2 = [-91, -81, -35, -33, -31, -22, -2, 10, 16, 52]
	Lab = merge(L1, L2)

if __name__ == "__main__":
    main()
