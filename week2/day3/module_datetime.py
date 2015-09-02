import datetime

t = datetime.time(5,23,44)
print 'hour :',t.hour
print 'minute :',t.minute
print 'seconds :',t.second
print datetime.date.today().timetuple()

print datetime.date.max
print datetime.date.resolution


# creating a new date
d1 = datetime.date(2015, 8, 25)
d2 = datetime.date(2015, 7, 15)
print d1
print d2


#timedelta  useful to calculate past/future dates
print datetime.timedelta(seconds=1)
print datetime.timedelta(minutes=1)
print datetime.timedelta(hours=1)
print datetime.timedelta(days=1)
print datetime.timedelta(weeks=1)


#comparing values

print "d1 > d2",d1 > d2

# combining dates and times
print 'Now time: ',datetime.datetime.now()
print 'Today time: ',datetime.datetime.today()
print 'UTC Now: ',datetime.datetime.utcnow()

"""we can access iterated values also because results are list which contains ['year','month','day','hour','minute','seconds','microseconds']"""
d = datetime.datetime.now()
for i in ['year','month','day','hour','minute','second','microsecond']:
	print i,getattr(d,i)

# Accessing previous dates
for i in ['year','month','day']:
	print i,getattr(d1,i)

#formatting time

format = '%a %b %d %H:%M:%S'
print 'stringformating time',datetime.datetime.now().strftime(format)
