import collections
person = collections.namedtuple('person','name age gender')
chanish = person(name = 'chanish',age = 21, gender = 'male')
nikhil = person(name = 'nikhil',age = 19, gender = 'male')

print chanish

for p in [chanish,nikhil]:
		print '%s %d %s'%p