# AU CG GC GU UA UG second this
stacking = [[-93, -224, -208, -55, -110, -136],  # AU first this
[-211, -326, -236, -141, -208, -211],            # CG
[-235, -342, -326, -153, -224, -251],            # GC
[-127, -251, -211, -50, -136, 129],              # GU
[-133, -235, -211, -100, -93, -127],             # UA
[-100, -153, -141, 30, -55, -50]]                # UG

# special GU case GGUC...GGUC
specialGUCase = -412
# AU end penalty
auEndPenalty = 45
# GU end penalty
guEndPenalty = 45
# self - complementary penalty
symmetryCorrection = 43
# intermolecular initiation
intermolInitiation = 409


def calc_energy(seq1, seq2):
    freeEnergy = intermolInitiation
    for nt1 in seq1:
       # pair1 =
    print(seq1)
    print(seq2)
    return freeEnergy


def read_file(filename):
    File = open(filename)
    content = []

    while 1:
        line = File.readline()
        if len(line) == 0:
            return content
        values = line.split()
        content.append(values)


def determine_pair(firstBase, secondBase):

    if firstBase == 'A' & secondBase == 'U':
        return 0
    elif firstBase == 'C' & secondBase == 'G':
        return 1
    elif firstBase == 'G' & secondBase == 'C':
        return 2
    elif firstBase == 'G' & secondBase == 'U':
        return 3
    elif firstBase == 'U' & secondBase == 'A':
        return 4
    elif firstBase == 'U' & secondBase == 'G':
        return 5
    else:
        return 6