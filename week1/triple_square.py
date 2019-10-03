#!/usr/bin/env python3

def triple(i):
	return 3*i
def square(i):
	return i**2
def main():
	
	for i in range(1,11):
		tr = triple(i)
		sqr = square(i)
		if(sqr > tr):
			break
		print(f"triple({i})=={tr} square({i})=={sqr}")		

if __name__ == "__main__":
    main()
