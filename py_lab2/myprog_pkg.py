#!/usr/bin/python3
import my_pkg.btoc
import my_pkg.uaioi

while True:
	m = int(input("Select menu: 1) conversion 2) union/intersection 3) exit ? "))
	if m == 1:
		my_pkg.btoc.conversion()
	elif m == 2:
		my_pkg.uaioi.uai()
	elif m == 3:
		print("exit the program...")
		break

