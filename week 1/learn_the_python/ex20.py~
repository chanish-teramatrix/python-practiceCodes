from sys import argv
script, f = argv

def print_file(file):
	print file.read()
	
def rewind(file):
	file.seek(0)

def line_print(file):
	print file.readline()

current_file = open(f,'w+')
content = """1. gatthering information
2. making flowchart
3. coding
4. testing"""

current_file.write(content)
#current_file.close()
#current_file = open(f,'r+')
rewind(current_file)
print_file(current_file)
rewind(current_file)
for i in range(0,3,1):
	line_print(current_file)
current_file.close()
