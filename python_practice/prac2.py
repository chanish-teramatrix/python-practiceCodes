#built in function, methods of list

list1 = ['india','america',1947,1990,'pak','Aus']
rand1 = [54,564,654,4,52,12,85,41,21,841,521,212,1,64,66,72]
rand2 = [54,5,521,1,8,4,12,1,584,854,31313,896,34,66,12,82]
list2 = ['a','b','c','d','e']
tupl = ('x','y','z')


print list1[:-2] #start from 2+1 element from right and prints towards left till the end of list
print list1[-1]  #will print right most element of list

print cmp(rand1, rand2) #list comparision 

print len(rand1) #will give length of list

print max(rand1) #returns maximum value of list

print min(rand1) #returns minimum value of list

print list(tupl) #tuple to list conversion

#appending is next- appending value -3 to rand1

rand1.append(-3)
print rand1

print rand1.count(1) #will tell how many times 1 has been appeared in list rand1

list1.extend(tupl) #will append values of tupl in list
print list1

print rand1.index(841) # tell the indexing of vlaue in list

rand1.insert(1,55) # will add 55 at poisition in list rand1
print rand1

rand1.remove(55) #removes obj in list
print rand1

rand1.reverse()
print rand1
print max(rand1)
rand1.sort()
print rand1 #provides sorted sequence of elements



rand2.reverse()
print rand2
print max(rand2)
rand2.sort()
print rand2 #provides sorted sequence of elements

