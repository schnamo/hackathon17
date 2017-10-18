from math import log1p

## stacking
# AU CG GC GU UA UG second this
stacking = [[-93, -224, -208, -55, -110, -136],  # AU first this
[-211, -326, -236, -141, -208, -211],            # CG
[-235, -342, -326, -153, -224, -251],            # GC
[-127, -251, -211, -50, -136, 129],              # GU
[-133, -235, -211, -100, -93, -127],             # UA
[-100, -153, -141, 30, -55, -50]]                # UG

## terminal mismatch
# A C G U second this
terminal_mismatch_AU = [[-80, -100, -80, -100],   # A first this
                         [-60, -70, -60, -70],    # C
                         [-80, -100, -80, -100],  # G
                         [-60, -80, -60, -80]]    # U

terminal_mismatch_CG = [[-150, -150, -140, -150],
                         [-100, -110, -100, -80],
                         [-140, -150, -160, -150],
                         [-100, -140, -100, -120]]

terminal_mismatch_GC = [[-110, -150, -130, -150],
                         [-110, -70, -110, -50],
                         [-160, -150, -140, -150],
                         [-110, -100, -110, -70]]

terminal_mismatch_GU = [[-30, -100, -80, -100],
                         [-60, -70, -60, -70],
                         [-60, -100, -80, -100],
                         [-60, -80, -60, -60]]

terminal_mismatch_UA = [[-100, -80, -110, -80],
                        [-70, -60, -70, -50],
                        [-110, -80, -120, -80],
                        [-70, -60, -70, -50]]

terminal_mismatch_UG = [[-100, -80, -110, -80],
                        [-70, -60, -70, -50],
                        [-50, -80, -80, -80],
                        [-70, -60, -70, -50]]

# Bulge Loops (up to n=30)
bulge_loops = [381, 280, 320, 360, 400, 440, 460, 470, 480, 490, 500, 501, 502, 503, 504, 504, 505, 505, 506, 507, 507, 508, 508, 508, 509, 509, 600, 600, 600, 601]
special_C_bulge = -90
RT = 61.6


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

# todo: dangling ends
# todo: hairpins

def calc_energy(seq1, seq2, seqfollowing1, seqpre2):
    # here we assume the reverse seq2
    specialCaseCounter = 0
    freeEnergy = intermolInitiation
    if len(seq1) != len(seq2):
        print('whuuaat' + ' ' +  seq1 + ' ' + seq2)
    for i in range(0, len(seq1)-1):
        pair1 = determine_pair(seq1[i], seq2[i])
        pair2 = determine_pair(seq1[i+1], seq2[i+1])
        if pair1 < 6 and pair2 < 6:
            freeEnergy = freeEnergy + stacking[pair1][pair2]
            # for special GU case
            if pair1 == 2 and pair2 == 3:
                if i + 3 < len(seq1):
                    specialCase1 = determine_pair(seq1[i + 2], seq2[i + 2])
                    specialCase2 = determine_pair(seq1[i + 3], seq2[i + 3])
                    if specialCase1 == 5 and specialCase2 == 1:
                        specialCaseCounter += 1
        elif pair1 == 7:
            continue
            # dealing with bulges
        elif pair2 == 7:
            bulge_counter = 0
            j = 3
            if pair1 < 6 and i < (len(seq1)-2):
                # bulge of length 1
                if 1 == 1:  # this is just because python is super annoying
                    nextPair = determine_pair(seq1[i + 2], seq2[i + 2])
                    if nextPair < 6:
                        freeEnergy = freeEnergy + stacking[pair1][nextPair]
                        # todo: consider number of possible loops of identical sequence
                        freeEnergy = freeEnergy + bulge_loops[0]  # - RT*log1p(2)
                        if seq1[i + 1] == 'C' or seq2[i + 1] == 'C':
                            freeEnergy = freeEnergy + special_C_bulge
                    # long bulges
                    elif nextPair == 7:
                        while nextPair == 7 and (i + j) < len(seq1):
                            bulge_counter = bulge_counter + 1
                            nextPair = determine_pair(seq1[i + j], seq2[i + j])
                            j = j + 1
                        freeEnergy = freeEnergy + bulge_loops[bulge_counter]
                        # in the case of a bulge with more than 1 nt take end penalties into account
                        if pair1 == 3 or pair1 == 5:
                            freeEnergy = freeEnergy + guEndPenalty
                        if pair1 == 0 or pair1 == 4:
                            freeEnergy = freeEnergy + auEndPenalty
                        # todo: what about they change the strand?

    freeEnergy = freeEnergy + penalties(seq1, seq2)
    # include first non matching base pair after duplex
    freeEnergy = freeEnergy + check_stacking(seq1, seq2, seqfollowing1, seqpre2)
    # special GU case
    freeEnergy += specialCaseCounter * specialGUCase
    freeEnergy -= specialCaseCounter * (stacking[2][3] + stacking[3][5] + stacking[5][1])
    #print(seq1)
    #print(seq2)
    #print(freeEnergy)
    return freeEnergy

def f(x):
    return {
        'A': 0,
        'C': 1,
        'G': 2,
        'U': 3,
        'a': 0,
        'c': 1,
        'g': 2,
        'u': 3,
        'T': 3,
        't': 3
    }.get(x, 9)

def check_stacking(seq1, seq2, following1, pre2):
    freeEnergy = 0
    if len(following1) > 0 and len(pre2) > 0:
        if seq1[-1] == 'A' and seq2[-1] == 'U':
            freeEnergy = terminal_mismatch_AU[f(following1[0])][f(pre2[-1])]
        elif seq1[-1] == 'C' and seq2[-1] == 'G':
            freeEnergy = terminal_mismatch_CG[f(following1[0])][f(pre2[-1])]
        elif seq1[-1] == 'G' and seq2[-1] == 'C':
            freeEnergy = terminal_mismatch_GC[f(following1[0])][f(pre2[-1])]
        elif seq1[-1] == 'G' and seq2[-1] == 'U':
            freeEnergy = terminal_mismatch_GU[f(following1[0])][f(pre2[-1])]
        elif seq1[-1] == 'U' and seq2[-1] == 'A':
            freeEnergy = terminal_mismatch_UA[f(following1[0])][f(pre2[-1])]
        elif seq1[-1] == 'U' and seq2[-1] == 'G':
            freeEnergy = terminal_mismatch_UG[f(following1[0])][f(pre2[-1])]
    return freeEnergy

def penalties(seq1, seq2):
    freeEnergy = 0
    size = len(seq1)
    # calculate end penalties
    if seq1[size - 1] == 'A' and seq2[size - 1] == 'U':
        freeEnergy += auEndPenalty
    if seq1[size - 1] == 'G' and seq2[size - 1] == 'U':
        freeEnergy += guEndPenalty
    if seq1[size - 1] == 'U' and seq2[size - 1] == 'A':
        freeEnergy += auEndPenalty
    if seq1[size - 1] == 'U' and seq2[size - 1] == 'G':
        freeEnergy += guEndPenalty
    # calculate start penalties
    if seq1[0] == 'A' and seq2[0] == 'U':
        freeEnergy += auEndPenalty
    if seq1[0] == 'G' and seq2[0] == 'U':
        freeEnergy += guEndPenalty
    if seq1[0] == 'U' and seq2[0] == 'A':
        freeEnergy += auEndPenalty
    if seq1[0] == 'U' and seq2[0] == 'G':
        freeEnergy += guEndPenalty
    # check self - complementarity
    if seq1 == seq2[::-1]:
        freeEnergy += symmetryCorrection

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

    if firstBase == 'A' and secondBase == 'U':
        return 0
    elif firstBase == 'C' and secondBase == 'G':
        return 1
    elif firstBase == 'G' and secondBase == 'C':
        return 2
    elif firstBase == 'G' and secondBase == 'U':
        return 3
    elif firstBase == 'U' and secondBase == 'A':
        return 4
    elif firstBase == 'U' and secondBase == 'G':
        return 5
    elif firstBase == '_' or secondBase == '_':
        return 7
    else:
        return 6