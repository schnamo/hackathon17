#!/bin/csh -f

set context = `grep CONTEXT .param | awk -F\= '{print $2}'`
if (-f $1) then
	set ll = `cat $1`
else
	set ll = $1
endif

foreach f ($ll)
set out = /tmp/${f:t:r}
#balign $1 $1 .param | awk -f ~/develop/RNApredict/format.awk `grep CONTEXT .param` | awk '{print $1+1,$3,$4,$5,$6,$8,$9,$10, "0"}' > $out.txt
balign data/Input/${f}_seq.txt data/Input/${f}_seq.txt .param |  awk '($2 <= $7 && $2-$1 < 13) {print $1,$3,$4,$5,$6,$8,$9,$10, "0"}' > $out.txt

python ~/develop/RNApredict/postprocess.py $out.txt $context > ${out}.csv
python ~/develop/RNApredict/RNApredict.py ${out}.csv ${out}.csv pred "$2" | paste -d\  - ${out}.txt | awk '($1 == 1) {print $0}' | cut -d\  -f 2-9 > data/Results/${f}.predicted
end
