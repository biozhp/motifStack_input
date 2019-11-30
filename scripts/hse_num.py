inf = open("./scripts/temp/temp3.txt","r")
ouf = open("./scripts/temp/temp4.txt","w")
for line in inf:
    line = line.replace("\n","")
    num_A = line.count("A")
    num_C = line.count("C")
    num_G = line.count("G")
    num_T = line.count("T")
    ouf.write("%s\t%s\t%s\t%s\n" % (num_A,num_C,num_G,num_T))