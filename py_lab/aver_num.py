#!/usr/bin/python3
n=int(input('How many numbers you input? '))

sum = 0
for i in range(n):

	a=float(input(str(i+1)+"번째 숫자 : "))
	sum=sum+a

if n > 0:
	average=sum/n
	print("average :",average)
else:
	print("error")
