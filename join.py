import sys
import os

from Bio import SeqIO

cmd = "paste -d\  data/Results/{}_motifs.txt data/Results/{}_final.txt | cut -d\  -f 1,3-6,8-10,19 > data/Results/{}_new.txt"

with open(sys.argv[1],"r") as f:
   for line in f:
     line = line.rstrip()
     #os.system(cmd.format(line,line,line,line))
     os.system(cmd.format(line,line,line))

f.close()
