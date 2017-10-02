import sys
from read_file import readFile, extractInteractions, generateInput

file = sys.argv[1]
destDir = sys.argv[2]
otherFile = sys.argv[3]
whatOutput = sys.argv[4]

#read file
content = readFile(file)
path = file.split('/')
name = path[len(path) - 1].split('.')
seqFile = destDir + name[0] + '_seq.txt'
interactionFile = destDir + name[0] + '_interactions.txt'
finalFile = destDir + name[0] + '_final.txt'

otherFile = otherFile + name[0] + '_motifs.txt'

trueCount = 0
falseCount = 0

if len(content) <= 14:
    print('too short')
else:
    #extract interactions
    interactions, sequence = extractInteractions(content)
    if int(whatOutput) == 0:
        #write sequence to file
        seq = open(seqFile, "w")
        seq.write('>' + name[0] + '\n')
        seq.write(sequence)
        seq.close()
        #write interactions to file
        intFile = open(interactionFile, "w")
        for int in interactions:
            intFile.write(str(int[0]) + ' ' + str(int[1]) + ' ' + str(int[2]) + ' ' + str(int[3]) + ' ' + '\n')
        intFile.close()
    else:
        #get output from other programme
        finalOutput = generateInput(otherFile, interactions, sequence)
        finalOutputFile = open(finalFile, "w")
        for output in finalOutput:
            #print(output)
            finalOutputFile.write(str(output[0]) + ' ' + str(output[1]) + ' ' + str(output[2]) + ' ' + str(output[3]) + ' ' + str(output[4]) + ' ' + str(output[5]) + ' ' + str(output[6]) + ' ' + str(output[7]) + ' ' + str(output[8]) + '\n')
            if output[4] == 0:
                falseCount = falseCount + 1
            else:
                trueCount = trueCount + 1
        finalOutputFile.close()
        if trueCount == 0:
            print('No interactions found for ' + name[0])


