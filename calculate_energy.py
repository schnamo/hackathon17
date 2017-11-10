import sys
from energy_programmes import calc_energy, read_file
from heapq import nlargest

counter = 0

filename = sys.argv[1]
destDir = sys.argv[2]
filename2 = sys.argv[3]
sequence = sys.argv[4]
path = filename.split('/')
name = path[len(path) - 1].split('.')
if destDir[-1] == '/':
    newFile = destDir + name[0] + '_energy.txt'
else:
    newFile = destDir + '/' + name[0] + '_energy.txt'
energyList = []
# read file
content = read_file(filename)
outputFile = open(newFile, "w")
# calculate free energy for each interaction
for line in content:
    energy = calc_energy(line[2], (line[6])[::-1], line[3], line[5])  # directly give the second part reversed
    #energyList.append(line, energy)
    # save in file those that pass threshold
    if energy < 0:
        counter = counter + 1
        outputFile.write(str(line[0]) + ' ' + str(line[1]) + ' ' + str(line[2]) + ' ' + str(line[3]) + ' ' + str(line[4]) + ' ' + str(line[5]) + ' ' + str(line[6]) + ' ' + str(line[7]) + ' ' + str(energy/100) + '\n')

#combine with results from RNAplfold
content2 = read_file(filename2)
#generate list and find max values
problist = []
indexlist = []
for i in range(2,len(content2)):
    newlist = []
    for j in range(4,len(content2[i])):
        if str(content2[i][j]) == 'NA':
            newlist.append(0)
        else:
            newlist.append(float(content2[i][j]))
    value = max(newlist)
    index = newlist.index(value)
    problist.append(value)
    indexlist.append(index)

largest = nlargest(counter/2, problist)
for large in largest:
    newindex = problist.index(large)
    length = int(indexlist[newindex]) + 4
    print(length)
    outputFile.write(str(newindex + 1) + ' Y ' + str(sequence[newindex:(newindex+length)]) + ' Y 0 Y Y Y 0' + '\n')

outputFile.close()