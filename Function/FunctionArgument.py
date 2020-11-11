# There are three types of argument in python :
	# 1. Positional Argument
	# 2. Keyword Argument
	# 3. Default Argument
####################### Positional Argument #############################

def sum(a, b):
	print("The sum is : ", a + b)
#sum (100,50) # Here value is assigened to 100 and b is 50

sum (50, b=10)

################################################################

def wish(name, msg):
	print("Hello", name, msg)

wish("Amit", msg="Good Evening",)