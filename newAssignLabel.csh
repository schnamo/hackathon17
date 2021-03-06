#!/bin/csh -f

#balign data/Input/${1}_seq.txt data/Input/${1}_seq.txt .param | awk -f ~/develop/RNApredict/format.awk `grep CONTEXT .param` > data/Results/${1}_motifs.txt
#awk -F\  '{print $1+1, $2, $3, $4, $5, $6, $7, $8, $9, $10}' data/Results/${1}_motifs.txt | sort -k 1,1 > sortedMotifs
#awk -F\  '{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10}' data/Results/${1}_motifs.txt | sort -k 1,1 > sortedMotifs
#tail --lines=+5 data/all_ct_files/$1.ct | sort -b -k 1,1 | join -1 1 -2 1 sortedMotifs - | sort -n -k 1,1 | awk -F\  '{print $1, $3, $4, $5, $6, $8, $9, $10, ($6==$14)}'

#balign data/Input/${1}_seq.fa data/Input/${1}_seq.fa .param  | awk '($2 <= $7 && $2-$1 < 13) {print $0}' > data/Results/${1}_motifs.txt

balign data/Input/${1}_seq.fa data/Input/${1}_seq.fa .param  | awk '($2 <= $7) {print $0}' > data/Results/${1}_motifs.txt
python ~/develop/RNApredict/checkCoordinates.py data/Input/${1}_seq.fa data/all_ct_files/${1}.ct data/Results/${1}_motifs.txt | cut -d\  -f 1,3-6,8-
