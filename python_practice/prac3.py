#All about dicitonary

profile1 = {
	'name' : 'chanish',
	'age' : '21',
	'father_name' : 'Mukesh Agarwal',
	'mother_name' : 'Saroj Agarwal',
	'mail_id' : 'chanish.agarwal@teramatrix.in',
	'company' : 'Teramatrix',
	'job_type' : 'Associate software engineer'}

profile2 = {
	'name' : 'nikhil',
	'age' : '20',
	'father_name' : 'Mukesh Agarwal',
	'mother_name' : 'Saroj Agarwal',
	'mail_id' : 'nikhilagarwal@gmail.com',
	'company' : 'niim',
	'job_type' : 'C.A'}

profile = ['name','age','father_name','mother_name','mail_id','companu','job_type']

print profile1['name']
print "working @%s"%profile1['company']

profile1['job_type'] = 'Software engineer trainee'

print profile1

print cmp(profile1,profile2)

print len(profile1)

print str(profile1)

print type(profile1) # returns value is dictionary type

profile3 = profile1.copy()
print profile3

profile3 = profile3.fromkeys(profile) #not working if i use new variable like profile4
print profile3,"\n"

if profile1.has_key('mail_id') == True :
	print "\n yeah mail_id exsist \n "		#checks if key exsist

print profile1.items()

print profile1.keys()

profile3.setdefault(residence,default=None)

