#!/bin/csh -f

echo "> ${1:t:r}"  > data/Input/${1}_seq.fa
tail --lines=+5 data/all_ct_files/$1.ct | awk '($1 == $6) {printf("%s",$2)}END{print ""}' >> data/Input/${1}_seq.fa
