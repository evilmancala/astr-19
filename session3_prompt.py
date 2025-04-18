'''
Write a Python program that defines a function
	 f(x) that returns x**3 + 8. 
In the main function of the program, call f(x) 
	with x = 9 and print the result.  
Use an if statement that executes if the 
	result is larger than 27 and prints “YAY!”.
'''

#Define function f(x) that returns x**3 + 8
def f(x):
	return x**3 + 8 #defining function return
	print(f(x))

#Call f(x) w/ x = 9
def main():
	x = 9 #	main function and defining
	result = f(x)
	print(result)

#'if' statement if the result is larger than 27
	if(f(x)>27):
		print("YAY!")


#Run main function...
if __name__ == '__main__':
	main()
