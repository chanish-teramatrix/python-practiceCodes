profile1 = {
	'name' : 'chanish',
	'age' : '21',
	'father_name' : 'Mukesh Agarwal',
	'mother_name' : 'Saroj Agarwal',
	'mail_id' : 'chanish.agarwal@teramatrix.in',
	'company' : 'Teramatrix',
	'job_type' : 'Associate software engineer'}
	
profile2 = {}
profile2.setdefault('residence','NOT_FIXED') #creates a key value pair and sets the default value to key
print profile2.items()


profile2.update(profile1)
print profile2.items()

print profile2.values()

if profile1.get('ag'):
	print profile1['age']
