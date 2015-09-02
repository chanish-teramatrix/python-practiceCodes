prams = []
try:
	war, crit = prams
except ValueError:
	war = 1
	crit = 2
	print "value has been entered defaultly %d   %d"%(war,crit)	
else:
	print war,crit
