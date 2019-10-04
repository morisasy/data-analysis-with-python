#!/usr/bin/env python3

import math
"""
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))
Choose a shape (triangle, rectangle, circle): triangle
Give base of the triangle: 20
Give height of the triangle: 5
The area is 50.000000
Choose a shape (triangle, rectangle, circle): rectangel
Unknown shape!
Choose a shape (triangle, rectangle, circle): rectangle
Give width of the rectangle: 20
Give height of the rectangle: 4
The area is 80.000000
Choose a shape (triangle, rectangle, circle): circle
Give radius of the circle: 10
The area is 314.159265
Choose a shape (triangle, rectangle, circle):
"""

#def triangle()

def main():
    # enter you solution here
   
	shapes = ["triangle", "rectangle", "circle"]
		
	while True:
			shape= input("Choose a shape (triangle, rectangle, circle): ")
			if shape in shapes:
				if shape == shapes[0]:
					b = float(input('Give base of the triangle: '))
					h = float(input('Give height of the triangle: '))
					triangle_area = 0.5 * b * h
					print(f"The area is {triangle_area}")

				elif shape == shapes[1]:
					w = float(input('Give width of the rectangle: '))
					h = float(input('Give height of the rectangle: '))
					rectangle_area =  w * h
					print(f"The area is {rectangle_area}")

				elif shape == shapes[2]:
					r= float(input('Give radius of the circle: '))
					cicle_area = math.pi * r**2
					print(f"The area is {cicle_area}")
			else:
				if shape == "":
					break
				else:
					print("Unknown shape!")


if __name__ == "__main__":
    main()
