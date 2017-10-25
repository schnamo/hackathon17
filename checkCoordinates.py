import sys
import os

from Bio import SeqIO

s = SeqIO.read(sys.argv[1], "fasta").seq.upper()
l = len(s)
size = [l, l]

from PIL import Image

im1 = Image.new("L",size,255)

with open(sys.argv[2],"r") as f:
   i = 1
   for line in f:
      line = line.rstrip().split()
      if len(line) == 6 and line[0] == line[5]:
         if int(line[4]) > 0:
            try:
              im1.putpixel([int(line[0])-1, int(line[4])-1],0) 
            except IndexError:
              print(line[0]+" "+line[4])
      i = i+1

f.close()

threshold = 0.1

with open(sys.argv[3],"r") as f:
  for lines in f:
    lines = lines.rstrip()
    line = lines.split()
    n = 0
    for x in range(int(line[0])-1,min(int(line[1]),l)):
      for y in range(int(line[5])-1,max(-1,int(line[6])),-1):
        if im1.getpixel((x, y)) < 255:
           n = n+1
    score = float(n)/(float(line[1])-float(line[0]))
    if score >= threshold:
       print(lines+" {}".format(1))
    else:
       print(lines+" {}".format(0))

f.close()
