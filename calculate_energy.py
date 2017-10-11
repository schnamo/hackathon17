import sys
from energy_programmes import calc_energy, read_file

filename = sys.argv[1]
# destDir = sys.argv[2]
path = filename.split('/')
name = path[len(path) - 1].split('.')
# newFile = destDir + name[0] + '_seq.txt'

energyList = []

# read file
content = read_file(filename)
# calculate free energy for each interaction
for line in content:
    if int(line[8]) == 1:
        energy = calc_energy(line[2], (line[6])[::-1])  # directly give the second part reversed
        energyList.append(energy)

# save in file those that pass threshold


