#!/bin/csh -f

set context = `grep CONTEXT .param | awk -F\= '{print $2}'`

foreach f (`cat $1`)
    echo $f
    ~/develop/RNApredict/newAssignLabel.csh $f > data/Results/${f}_good.txt
    #~/develop/RNApredict/assignLabel.csh $f > data/Results/${f}_new.txt

    python ~/develop/RNApredict/postprocess.py data/Results/${f}_good.txt $context > data/Results/${f:r}_good.csv
end
