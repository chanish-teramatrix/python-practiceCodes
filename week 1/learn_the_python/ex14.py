from sys import argv
script, user = argv

ans = raw_input("would you like to fill the user's profile")
if ans == 'yes':
	name = raw_input("please type in the name")
	job = raw_input("please type in the job profile")
	print """
name of the person is %s
job profile is        %s """%(name,job)
elif ans == 'no':
	print "have a good day"
	
else:
	print "not an appropriate ans"



