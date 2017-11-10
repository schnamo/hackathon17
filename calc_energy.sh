#!/bin/bash
#start for each file in directory
DIR=$1
SEQDIR=$2
DESTDIR=$3
FILES=$DIR/'*'

for f in $FILES
do
  # take action on each file. $f store current file name
  #pre-pre-processing with 0
  #pre-processing with 1
  echo $f
  SEQNAME="$(echo $f | rev | cut -d"/" -f1  | rev | cut -d _ -f -2)"
  filename=$SEQDIR'/'$SEQNAME'_seq.txt'
  seq=$(<$filename)
  #get sequence
  seqcut="$(echo $seq | cut -d ' ' -f 2)"
  #use RNAplfold
  echo $seqcut | RNAplfold --ulength=10
  plfoldfile=$DESTDIR'/'$SEQNAME'_pflod_lunp'
  cp plfold_lunp $plfoldfile
  echo $plfoldfile

  echo $seqcut
  #calculate free energy and use RNAplfold output
  python3.5 /Users/lotti/PycharmProjects/Hackathon/calculate_energy.py $f $DESTDIR $plfoldfile $seqcut || {
  	echo 'problem with' $f $'\n'
  }

done
