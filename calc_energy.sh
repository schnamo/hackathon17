#!/bin/bash
#start for each file in directory
DIR=$1
DESTDIR=$2
FILES=$DIR/'*'

for f in $FILES
do
  # take action on each file. $f store current file name
  #pre-pre-processing with 0
  #pre-processing with 1
  echo $f
  python3.5 /Users/lotti/PycharmProjects/Hackathon/calculate_energy.py $f $DESTDIR || {
  	echo 'problem with' $f $'\n'
  }
done
