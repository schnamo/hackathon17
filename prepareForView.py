import sys
import os

from Bio import SeqIO

s = SeqIO.read(sys.argv[1], "fasta").seq.upper()
l = len(s)
size = [l, l]

out = bytearray(l)

for i in range(l):
   out[i] = ord('.')

for line in sys.stdin:
   line = line.rstrip().split()
   pos1 = int(line[0])-1
   pos2 = int(line[2])-1
   m1 = line[1]
   m2 = line[3]
   ml = len(m1)
   under1 = 0
   under2 = 0;
   for i in range(ml):
     if m1[i] == '_':
        under1 = under1+1
     elif m2[ml-1-i] == '_':
        under2 = under2+1
     else:
        out[pos1+i-under1] = ord('(')
        out[pos2-i+under2] = ord(')')

print("> rna seq and II structure")
print(s)
print(out.decode())
