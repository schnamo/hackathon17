import sys
import os

from Bio import SeqIO

cmd = "balign data/Input/{}_seq.txt data/Input/{}_seq.txt .param | awk -f ~/develop/RNApredict/format.awk CONTEXT=7 | paste -d\  - data/Results/{}_final.txt | cut -d\  -f 1,3-6,8-10,15 > data/Results/{}_new.txt"
cmd = "balign data/Input/{}_seq.txt data/Input/{}_seq.txt .param | awk -f ~/develop/RNApredict/format.awk `grep CONTEXT .param` > data/Results/{}_motifs.txt"

with open(sys.argv[1],"r") as f:
   for line in f:
     line = line.rstrip()
     #os.system(cmd.format(line,line,line,line))
     os.system(cmd.format(line,line,line))

f.close()
