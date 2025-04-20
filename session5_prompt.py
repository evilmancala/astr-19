import numpy as np
from tabulate import tabulate
from astropy.table import Table
import math
'''
Write a Python program that writes out a table of the function sin(x) vs. x, 
where x is tabulated between 0 and 2 with a thousand entries. 
Follow the basic Python program structure, 
including a main program function.
'''

x = np.linspace(0,2 * math.pi,1000) #generate 10 valyes from 0 to 2pi
y = x**2

#Tables using standard
#create list of tuples of size 2 w/ all x and y values
table_data = [(a,b) for a,b in zip(x,y)]


#create table
table_header = ["x", "y"]
python_table = tabulate(table_data, tablefmt="grid", 
	headers=table_header,floatfmt=".3f")

def main():
	print(python_table) #show table

#main
if __name__ == "__main__":
	main()