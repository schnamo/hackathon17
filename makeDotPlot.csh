#!/bin/csh -f

set f=${1:t:r}

tail --lines=+5 data/all_ct_files/$f.ct | awk '($5 != 0) {print $1, $5}' | python ~/develop/RNApredict/dotplot.py data/Input/${f}_seq.txt data/Images/${f}_dp.jpg data/Images/${f}_target.jpg
