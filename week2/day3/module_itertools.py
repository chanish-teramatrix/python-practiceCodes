from itertools import *

l1 = [1,2,3,4,5,'a','b','c']
#chain function take several iterators and returns as a single iterator
for i in chain(l1):
	print i

#izip function combines elements of several iterator and returns into tuple

for i in izip([1,2,3,4,5],['a','b','c']):
	print i

for i in islice(l1,1,5):
	print i

# tee() function reads from file and writes them to named file

l2,l3 = tee(islice(l1,1,5))



# print l2
print '\n'

# for i in l3:
	# print i




#-----------------------------------------------------------------------------


#  converting inputs - imap()

for i in imap(lambda x:3*x, xrange(10)):
	print i 




#-----------------------------------------------------------------------------
# Filteing

#dropwhile -- iterates over a condition and for first time when condition is false it returns all the upcoming value

def condition_lt1(x):
	print 'Testing',x
	return(x < 1)

print '\n\tdropwhile yield'
for i in dropwhile(condition_lt1,[-1,0,-2,34,5,2,-1,7,2,4523,34]):
	print 'Yield',i

print '\n\ttakewhile yield'
for i in takewhile(condition_lt1,[-1,0,-2,34,5,2,-1,7,2,4523,34]):
	print 'Yield',i

print '\n\tifilter yield'
for i in ifilter(condition_lt1,[-1,0,-2,34,5,2,-1,7,2,4523,34]):
	print 'Yield',i