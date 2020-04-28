#!/usr/bin/python3
def uai():
	a = list(map(int,input("1st list: ").replace("[","").replace("]","").replace(","," ").split()))
	b = list(map(int,input("2nd list: ").replace("[","").replace("]","").replace(","," ").split()))
	s1 = set(a)
	s2 = set(b)
	print("=> union",list(s1.union(s2)))
	print("=> intersection",list(s1.intersection(s2)))
