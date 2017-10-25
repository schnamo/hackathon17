import sys
from energy_programmes import calc_energy, read_file

filename = sys.argv[1]
destDir = sys.argv[2]
path = filename.split('/')
name = path[len(path) - 1].split('.')
newFile = destDir + name[0] + '_energy.txt'

energyList = []

# read file
content = read_file(filename)
outputFile = open(newFile, "w")
# calculate free energy for each interaction
for line in content:
    energy = calc_energy(line[2], (line[6])[::-1], line[3], line[5])  # directly give the second part reversed
    # save in file those that pass threshold
    outputFile.write(str(line[0]) + '\t' + str(line[1]) + '\t' + str(line[2]) + '\t' + str(line[3]) + '\t' + str(line[4]) + '\t' + str(line[5]) + '\t' + str(line[6]) + '\t' + str(line[7]) + '\t' + str(energy) + '\n')
outputFile.close()




