import time #do not forget about importing time
import calendar

#time.time() function returns current system time in ticks since 12a.m 1 jan 1970
ticks = time.time()
print ticks

localtime = time.localtime(ticks)
print "localtime",localtime

localtime = time.asctime(localtime)
print localtime

print '\n'

month_august = calendar.month(2015,8)
print month_august,'\n'

print "clock time",time.clock()

print time.ctime() #it's more like time.asctime(time.localtime(ticks))


