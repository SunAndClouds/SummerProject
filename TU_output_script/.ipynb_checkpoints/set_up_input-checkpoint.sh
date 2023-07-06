#!/bin/bash

input_head=../templates/PWR_head
tuplot_inp=../templates/TuPlot.inp

for ph in $(find ../truncated_ph -name '*txt' ! -name '*checkpoint*'); do 

  name=$(basename $ph | sed s/TU_// | sed s/.txt//)

  echo "Setting up input for case: $name"

  mkdir -p $name

  cat $input_head > $name/input
  cat $ph >> $name/input

  cp $tuplot_inp $name/TuPlot.inp

done
