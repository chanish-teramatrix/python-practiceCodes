#!/usr/bin/python
import re
def regexp_match(pattern,string):
	match = re.findall(pattern,string)
	if match:
		return match
	else:
		print "not match"

string = "chanish.agarwal1@gmail.com chanish.agarwal@teramatrix.in"
pat = r'([\w.-]+)@([\w.]+)'
match = regexp_match(pat,string)
print match[0][0],"\t",match[0][1]
print match[1][0],"\t",match[1][1]
