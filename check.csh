#!/bin/csh -f

foreach f (`cat $1`)
	echo -n $f
	set n = `wc -l data/Results/${f}_final.txt | cut -f 1 -d\ `
	set m = `wc -l data/Results/${f}_new.txt | cut -f 1 -d\ `
	if ($n != $m) then
		echo " wrong"
        else
		echo " ok"
	endif
end
