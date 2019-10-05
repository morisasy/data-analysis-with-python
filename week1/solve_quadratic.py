#!/usr/bin/env python3

import math

"""
In mathematics, the quadratic equation ax2+bx+c=0 can be solved with the formula x=−b±b2−4ac√2a.

Write a function solve_quadratic, that returns both solutions of a generic quadratic as a pair (2-tuple) when the coefficients are given as parameters. It should work like this:

print(solve_quadratic(1,-3,2))
(2.0,1.0)
print(solve_quadratic(1,2,1))
(-1.0,-1.0)

"""

def solve_quadratic(a, b, c):
	# d: discriminant
	d = (b**2) - (4*a*c)
	s1 = (-b + math.sqrt(d))/(2*a)
	s2 = (-b - math.sqrt(d))/(2*a)
	return(s1,s2)


def main():
	a = float(input('Enter coefficient of a: '))
	b = float(input('Enter coefficient of b: '))
	c = float(input('Enter coefficient of c: '))
	if a == 0:
		print("coefficient of a should not equal to zero")

	x = solve_quadratic(a, b, c)
	print('{x}')
    

if __name__ == "__main__":
    main()
