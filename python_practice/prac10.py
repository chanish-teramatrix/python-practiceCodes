#!/usr/bin/python


import prac9 #imports prac9.py
import prac8 #imports prac8.py

reload(prac8) #reload function to reload module if changes happens in that modules outside
reload(prac9)

print prac8.square(4)
print prac8.cube(4)
print '\n \n'
name = 'peter'
age = 46
prac9.even_odd(10)

print "module prac8 contains :",dir(prac8)
print "\nmodule prac9 contains :",dir(prac9)
print '\n\n'
print locals() #function to know locals in programm
print '\n'
print globals()

print prac8.cube(9)


