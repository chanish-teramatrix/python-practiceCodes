#programm includes access to list deleiton and updation

list1 = ['india','america',1947,1990,'pak','Aus']
list2 = ['a','b','c','d','e']

print list1
print "\nvalue from position 1 to 4"
print list1[1:5]
print "\nvalues from position 0 to 3"
print list2[:4]

list1[1] = "America"  #list update
print list1

del list1[1] #deletion of element at position 1
print list1

del list1 # deleiton of list
#print list1       will give you error here
