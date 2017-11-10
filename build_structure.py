import sys
from read_file import readFile

file = sys.argv[1]

#read in file
content = readFile(file)

for line in content:
