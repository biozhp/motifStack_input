inf = open("./scripts/temp/temp6.txt","r")
ouf = open("./scripts/temp/temp7.txt","w")
for line in inf:
    line = line.replace("\t"," ").replace("\n","")
    ouf.write("%s\n" % (line))