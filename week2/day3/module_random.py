import random
import itertools
import time

random.seed(1)
print 'random.random() function wihich produces random number between 0 to 1'
for i in xrange(5):
	#  will always generate floating point numbers between o to 1
	print "random number %.3f"%random.random()

print 'random.uniform() generates random num between given range in floating point '
for i in xrange(5):
	print "random number %.3f"%random.uniform(5,10)

print 'random.randint(a,b) generates integer in given range'
for i in xrange(5):
	print "random number %d"%random.randint(-5,10)

print 'random.randrange(start,stop,step) generates integer in '
for i in xrange(5):
	print "random number %d"%random.randrange(1,10,2)



#___________________________________________________________________________________

# picking random items

toss = {'head':'win','tail':'loss'}
for i in xrange(10):
	print toss[random.choice(toss.keys())]

name = ['achal','akshita','mridul','puneet']
for i in xrange(10):
	print random.choice(name)


# Multiple simultaneous generators
seed = time.time()

r1 = random.Random(seed)
r2 = random.Random(seed)


print 'seed time',seed

for i in xrange(8):
	print '%0.4f \t %.04f'%(r1.random(),r2.random())




#-----------------------------------------------------------------------------


#  converting inputs - imap()

for i in imap(lambda x:3*x,xrange(10)):
	print i 