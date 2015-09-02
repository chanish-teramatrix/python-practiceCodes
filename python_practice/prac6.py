"""functions
four types of argument:
1. Required argument
	function(name,age)
2.keyword argument 
	function(name,age)	
	function(age=value,name=value)but accepts if arguments are not according to their place utill their 	argument_name are as mentioned in function
3. Default arguments
	function(name,age = 21) if function is defined like that then at calling time if function is function(name) will be accepted and age value will be default as mentioned above
	
4. variable-length argument
	useful when arguments could be more or less
	function(var1,*var2)"""
	
	
	
def fn12(name,age):
	print "name : %s \nage : %s"%(name,age)
	
	
name = 'chanish'
age = 21
fn12(name,age)
fn12(age = 21,name = 'nikhil')


def f3(name, age='private'):
	print "name : %s \nage : %s"%(name,age)
	
f3(name,age)
f3('chanish')

def f4(*activities):
	for act in activities:
		print act
		
act = ['gym','yoga','shooting','martialArts']
f4(act)
