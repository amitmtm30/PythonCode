
####################### Factorial using while loop ###################
#def factorial(n):
#	result = 1 #factorial of 0 is 1
#	while n >= 1:
#		result = result * n
#		n = n-1
#	return result
#n = int(input("Enter Number to find the Factorial value : "))
#s = factorial(n)
#print("Factorial is : ", s)

################################### Factorial using for Loop #############################################
def factorial(n):
	result = 1
	for x in range(1, n+1):
		result = result * n
		n = n -1
	return result
n = int(input("Enter Number to find the Factorial value : "))
s = factorial(n)
print("Factorial is : ", s)