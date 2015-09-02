""" Anonymous function
Lambda function is small anonymous function
"""

square = lambda x: x*x
print square(5)

remainder = lambda v,r: v%r
print remainder(100,8)

def remainder(x):
	lambda y:x%y
	
f1 = remainder(100)
f2 = remainder(2344)

print f1(3)
print f1(4)
