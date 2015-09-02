
def print_it(**kwargs):
	for key, value in kwargs.iteritems():
		print value 

p = {3:'c', 5:'b', 9:'a'}
print_it(**p)