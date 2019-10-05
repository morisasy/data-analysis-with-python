#!/usr/bin/env python3
import copy
from heapq import merge as mg

def merge(L1, L2):
	L = list(mg(L1, L2)) 
	print(L)
	return L

def main():
	L1 = [-91, -87, -81, -78, -72, -33, -31, -23, -21, 1, 22, 25, 34, 44, 50, 58, 61, 66, 78,80]
	L2 = [-91, -81, -35, -33, -31, -22, -2, 10, 16, 52]
	Lab = merge(L1, L2)
	#print(len(La))
	#print(len(Lb))

	#L1 = copy.copy(L2)
	#print(len(Lb))
	#Lab = merge(La, Lb)
	#print(Lab)
	#print(len(Lab))
	#print(len(Lab))

if __name__ == "__main__":
    main()
