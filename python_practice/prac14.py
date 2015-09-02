#messing up with list and tuples

basic_detail = {
	'profile1' : ('chanish',21),
	'profile2' : ('nikhil',20),
	'profile3' : ('sunny',21)}
name,age = basic_detail['profile1']
print "name and age are as follows",name,"  ",age

if basic_detail.items():
	print basic_detail.items()

print ('nikhil',20) in basic_detail.values()

search = lambda x,y : (x,y) in basic_detail.values()

print search('sunny',21)

even_no = [i for i in range(0,34,2)]
print even_no
