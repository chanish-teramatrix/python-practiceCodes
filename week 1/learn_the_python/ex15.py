from sys import argv
script, filename = argv
file1 = open(filename,'w+')
content = """
this is going to be written in file
1.name
2.age
3.profile"""
file1.write(content)
file1.close()
file1 = open(filename,'r')

print file1.read()

