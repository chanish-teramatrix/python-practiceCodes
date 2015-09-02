#!/usr/bin/python
import re
def regexp_match(pattern,string):
	match = re.search(pattern,string)
	if match:
		print "match:",match.group()
	else:
		print "not match"

string = "name chanish email id chanish.agarwal@teramatrix.in ppppppeeppppppppppp  sector14	sector38"
email = "cha-nish.agarwal1@tera-matrix.in"
string1 = "<tr align='right'><td>33</td><td>Benjamin</td><td>Victoria</td>"
pat = r'\S*@\S*'
regexp_match(pat,string)
print '\n'
pat = r'\w+'
regexp_match(pat,string)  # prints left most word

pat = r'p+'
regexp_match(pat,string)  # prints left most longest sequence of p (minimum 1)

pat = r'\s\s+\w+\s+\w+'
regexp_match(pat,string)

pat = r'\w+\d+'
regexp_match(pat,string)

pat = r'[ncha\w.-]+@[\w.-]+'  # use of square brackets to find email
regexp_match(pat,string)

pat = r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>'  # use of square brackets to find email
regexp_match(pat,string1)


