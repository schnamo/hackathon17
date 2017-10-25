import sys
import os

from Bio import SeqIO

s = SeqIO.read(sys.argv[1], "fasta").seq.upper()
l = len(s)
size = [l, l]

from PIL import Image

im = Image.new("L",size,255)

for i in range(l):
   for j in range(l):
      c1 = s[i]
      c2 = s[j]
      if c1 == c2:
         im.putpixel([i,j], 255)
      elif c1 == 'A' and c2 == 'U':
         im.putpixel([i,j], 0)
      elif c1 == 'U' and c2 == 'A':
         im.putpixel([i,j], 0)
      elif c1 == 'C' and c2 == 'G':
         im.putpixel([i,j], 0)
      elif c1 == 'G' and c2 == 'C':
         im.putpixel([i,j], 0)
      elif c1 == 'G' and c2 == 'U':
         im.putpixel([i,j], 128)
      elif c1 == 'U' and c2 == 'G':
         im.putpixel([i,j], 128)

im.save(sys.argv[2])

im1 = Image.new("L",size,255)

for line in sys.stdin:
   line = line.rstrip().split()
   im1.putpixel([int(line[0])-1, int(line[1])-1],0) 

im1.save(sys.argv[3])
