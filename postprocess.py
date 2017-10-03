import sys

RNA2Int = [1, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0 ]

def convert(motif):
    motif = motif.upper()
    for i in range(len(motif)):
      c = chr(ord('0')+RNA2Int[ord(motif[i])-ord('A')])
      if i == 0:
         s = c
      else:
         s += ","+c
    return s

def leftPad(motif, l):
    for i in range(l-len(motif)):
      motif = "X"+motif
    return motif

def rightPad(motif, l):
    for i in range(l-len(motif)):
      motif = motif+"X"
    return motif

with open(sys.argv[1],"r") as f:
   context = int(sys.argv[2])
   n = 2
   for line in f:
     line = line.split()
     motif1 = line[2]
     motif2 = line[6]
     left1 = convert(leftPad(line[1],context))
     right1 = convert(rightPad(line[3],context))
     left2 = convert(leftPad(line[5],context))
     right2 = convert(rightPad(line[7],context))
     #print(convert(motif1[0:6])+","+convert(motif1[len(motif1)-6:])+","+line[4])
     print(left1+","+convert(motif1[0:n])+","+convert(motif1[len(motif1)-n:])+","+right1+","+left2+","+convert(motif2[0:n])+","+convert(motif2[len(motif2)-n:])+","+right2+","+line[8])
     #print(convert(line[1])+","+convert(motif1[0:2])+","+convert(motif1[len(motif1)-2:])+","+convert(line[3])+","+convert(line[5])+","+convert(motif2[0:2])+","+convert(motif2[len(motif2)-2:])+","+convert(line[7])+","+line[8])

f.close()
