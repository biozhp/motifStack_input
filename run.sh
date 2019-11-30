#!/bin/bash
inf=$1
sample=$2
ouf=$3
cat ${sample} | while read line
do
python ./scripts/sample_hse.py -in ${inf} -name ${line} && \
dos2unix ./scripts/temp/temp2.txt
awk '{for(i=1;i<=NF;i=i+1){a[NR,i]=$i}}END{for(j=1;j<=NF;j++){str=a[1,j];for(i=2;i<=NR;i++){str=str " " a[i,j]}print str}}' ./scripts/temp/temp2.txt > ./scripts/temp/temp3.txt && \
python ./scripts/hse_num.py && \
dos2unix ./scripts/temp/temp4.txt
awk '{for(i=1;i<=NF;i=i+1){a[NR,i]=$i}}END{for(j=1;j<=NF;j++){str=a[1,j];for(i=2;i<=NR;i++){str=str " " a[i,j]}print str}}' ./scripts/temp/temp4.txt > ./scripts/temp/temp5.txt && \
paste ./scripts/pcm_header ./scripts/temp/temp5.txt > ./scripts/temp/temp6.txt
python ./scripts/hse_replace.py && \
mv ./scripts/temp/temp7.txt ${ouf}"/"${line}".pcm"
done
rm ./scripts/temp/*
