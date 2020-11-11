########### Fundametal Python ##################################
a,b = 10, 20
print(a,b)

###############################
#a,b,c,d = 10,20,30,40,50
#print(a,b,c,d) ##### Value Error, as too many Arguments

############################################################

a,b,c,d = 10,20,30,40
print(a,b,c,d)

############################################################

a = 10 
print(type(a)) # <class 'int'>

############################

a = True
print(type(a)) # < class 'boolean'

##################################
#for i in range(10): # start with 0 and end 9
#	print(i)
#	print(i , end = '') #0123456789a 

######################################
print()
a = 30
b = 20
x=10 if a > b else 20
print(x)
