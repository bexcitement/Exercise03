# Exercise03 Calculator

# import functions from arithmetic.py (wrote for Exercise02)
from arithmetic import *

i = 1

while(i > 0):
	equation_input = raw_input("> ")

	equation_parts = equation_input.split(" ")

	if equation_parts[0] == "+":
		print add(int(equation_parts[1]),int(equation_parts[2]))
	elif equation_parts[0] == "-":
		print subtract(int(equation_parts[1]),int(equation_parts[2]))
	elif equation_parts[0] == "*":
		print multiply(int(equation_parts[1]),int(equation_parts[2]))
	elif equation_parts[0] == "/":
		print divide(float(equation_parts[1]),int(equation_parts[2]))
	elif equation_parts[0] == "square":
		print square(int(equation_parts[1]),int(equation_parts[2]))
	elif equation_parts[0] == "cube":
		print cube(int(equation_parts[1]),int(equation_parts[2]))	
	elif equation_parts[0] == "pow":
		print power(int(equation_parts[1]),int(equation_parts[2]))
	elif equation_parts[0] == "mod":
		print mod(int(equation_parts[1]),int(equation_parts[2]))
	elif equation_parts[0] == "q":
		quit()






