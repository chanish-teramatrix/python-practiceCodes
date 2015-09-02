import Queue

q1 = Queue.Queue()
q2 = Queue.LifoQueue()
q3 = Queue.PriorityQueue()

for i in xrange(10):
	q1.put(i)
	q2.put(i)

print 'Queue 1 FIFO type'
while not q1.empty():	
	print q1.get()

print 'Queue 2 LIFO type'
while not q2.empty():
	print q2.get()

q3.put(300,'achal')
q3.put(88,'mridul')
q3.put(250,'puneet')
q3.put('puneet')
q3.put('mridul')
q3.put('achal')

while not q3.empty():
	print q3.get()
