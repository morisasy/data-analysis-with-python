#!/usr/bin/env python3
"""
Let us consider throwing two dice. (A dice can give a value between 1 and 6.) Use two nested for loops in the main function to iterate through all possible combinations the pair of dice can give.
 There are 36 possible combinations. Print all those combinations as (ordered) pairs that sum to 5. For example, your printout should include the pair (2,3). Print one pair per line.

"""

def main():

    for i in range(1,7):
        for j in range(1,7):
            if(i + j)==5:
                 print(f'{(i,j)}')

if __name__ == "__main__":
    main()
