#!/usr/bin/python3
x=0
y=1
z=0

n=int(input('fibonacci number? '))
while z<n:

	if z==(n-1):
		print(y)
		print("F%d = %d" % (n,y))
		break
	print(y,end=",")

	u=x
	x=y
	y=u+y
	z=z+1 
