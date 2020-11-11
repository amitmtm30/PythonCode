### WAF that takes as an argument and print square of the number

def square(n):
	s = n * n
	print("Square of Number is : ", s)
n = eval(input("Enter number to check the square : "))
square(n)
print("*" * 30)

########################################

def factorial(n):
	result = 1
	while n > 1:
		result = result * n
		n = n -1
	return result

n = eval(input("Enter number for Factorial value : "))
print("The Factorial of Number is : ", factorial(n))
print("*" * 30)

################################################################

def sum (a,b):
	result = a + b
	return result

add = sum (10,20)
print("Addition of two number is : ", add)
print("*" * 30)

####################################################################

def sub (a,b):
	result = a - b
	return result

substraction = sub (20, 10)
print("Substraction of two number is : ", substraction)
print("*" * 30)

####################################################################

###Swap Function #######

def swap(a,b):
	a,b = b,a
	return a, b
print("Swap of the number is : ", swap(10,20))
print("*" * 30)

##########################################################################

def evenodd(n):
	if n%2 == 0:
		print("Number {} is even: ".format(n))
	else:
		print("Number {} is odd : ".format(n))
n = eval(input("Enter number to check whether it is Even or Odd : "))
evenodd(n)
print("*" * 30)

##########################################################################
##Calculator function:

def calculator(a,b):
	sum = a + b
	print("The Addition of number is : ", sum)
	sub = a - b
	print("The Substraction of number is : ", sum)
	mul = a * b
	print("The Multiplication of number is : ", sum)
	div = a / b
	print("The division of number is : ", sum)

	return sum, sub, mul, div
x, y = eval(input("Enter two number to find the sum, sub, mul and div : "))

calculator(x,y)




















































