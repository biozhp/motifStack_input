import re
import os
import argparse
parser = argparse.ArgumentParser(description="Author: Peng Zhao <pengzhao@nwafu.edu.cn>")
parser.add_argument('-name', type=str)
parser.add_argument('-inf', type=str)
args = parser.parse_args()
sample_name = args.name
inf_name = args.inf
inf2 = open(inf_name,"r")
ouf_name = "./scripts/temp/temp.txt"
ouf2 = open(ouf_name,"w")
data_list = []
for line2 in inf2:
    line2 = line2.replace("\n","")
    li2 = re.split("\t",line2)
    hse_len = len(li2[1])
    if li2[0] == sample_name:
        for i in range(hse_len):
            start = int(i)
            end = int(i) + 1
            base = li2[1][start:end]
            data_list.append(base)
    ouf2.write("%s\n" % (data_list))
    data_list = []
ouf2.close()
inf = open("./scripts/temp/temp.txt","r")
ouf = open("./scripts/temp/temp2.txt","w")
for line in inf:
    line = line.replace("[","").replace("]","").replace("\'","").replace(" ","").replace(",","\t").replace("\n","")
    if len(line) != 0:
        ouf.write("%s\n" % (line))
ouf.close()