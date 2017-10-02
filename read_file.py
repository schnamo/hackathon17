distance = 5
offset = 5

def readFile(filename):
    File = open(filename)
    counter = 0
    content = []

    while 1:
        line = File.readline()
        if len(line) == 0:
            return content
        if line[0] != "#":
            counter = counter + 1
            if(counter > 1):
                values = line.split()
                content.append(values)

def readOtherFile(filename):

    File = open(filename)
    content = []

    while 1:
        line = File.readline()
        if len(line) == 0:
            return content
        values = line.split()
        content.append(values)

def extractInteractions(content):

    interactions = []
    sequence = ''
    gapList = []
    acceptedNt = ['A', 'U', 'T', 'C', 'G', 'a', 'u', 't', 'c', 'g']
    gapCount = 0

    newContent = []

    for k in range(0, len(content)):
        if content[k][1] in acceptedNt:
            if content[k][1] == 'T' or content[k][1] == 't':
                content[k][1] = 'U'
            sequence = sequence + content[k][1]
            gapList.append(gapCount)
            newContent.append(content[k])
        else:
            gapCount = gapCount + 1
            gapList.append(gapCount)

    for l in range(0, len(newContent)):
        newContent[l][4] = int(newContent[l][4]) - gapList[int(newContent[l][4]) - 1]

    content = newContent

    for i in range(0, len(content)):
        motifCounter = 0
        motif = True

        if int(content[i][4]) > 0:
            j = i + 1
            #allowing for 1 bulge and some distance
            while j < len(content) and motifCounter < 2 and motif is True:
                if int(content[j][4]) == 0:
                    motifCounter = motifCounter + 1
                else:
                    if int(content[j-1][4]) == 0:
                        compareValue = int(content[j-2][4])
                    else:
                        compareValue = int(content[j-1][4])
                    if abs(int(content[j][4]) - compareValue) > distance:
                        motif = False
                j = j + 1
            j = j - 1
            #in case the last two entries are 0
            if int(content[j][4]) == 0:
                j = j - 1
            if int(content[j][4]) == 0:
                j = j - 1
            if motif == False:
                j = j - 1
            if int(content[j][4]) == 0:
                j = j - 1
            if j - i > 2:
                lengthJ = abs(int(content[i][4]) - int(content[j][4])) + 1
                interactions.append([i + 1, abs(j - i) + 1, int(content[i][4]), lengthJ])
            else:
                interactions.append([i + 1, 0, -1, 0])
        else:
            interactions.append([i + 1, 0, -1, 0])

    #print(sequence)

    return interactions, sequence


def generateInput(otherFile, interactions, sequence):

    content = readOtherFile(otherFile)
    finalOutput = []

    for element in content:
        j = len(sequence) - int(element[5])
        interact = 0
        for i in range(0, len(interactions)):
            if int(interactions[i][2]) > 0:
                if abs(int(element[0]) - i) < offset and abs(interactions[i][2]-j) < offset:
                    interact = 1
        finalOutput.append([element[0], element[2], element[3], element[4], str(j), element[7], element[8], element[9], interact])

    return finalOutput






