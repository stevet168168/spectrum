#! /usr/bin/python3

import bisect
import sys



if len(sys.argv) < 4:
    print("Usage: %s <pasmo sym file> <fuse profile> <output file>" % sys.argv[0])
    sys.exit(1)



labels=[]
cycles={}
output=[]



file = open(sys.argv[1], "r")
syms = file.read().split("\n")
for sym in syms:
    if len(sym) > 0:
        sym_split=sym.split("\t")
        labels.append((sym_split[2][5:9], sym_split[0]))
labels.sort()
file.close()



file = open(sys.argv[2], "r")
counts = file.read().split("\n")
for count in counts:
    if len(count) > 0:
        count_split=count.split(",")
        addr=count_split[0][2:6].upper()
        number= int(count_split[1])
        i=bisect.bisect_right(labels, (addr, '£')) - 1
        if i > 0:
            label=labels[i][1]
            cycles[label] = cycles.get(label, 0) + number
file.close()



for k, v in cycles.items():
    output.append((v, k))
output.sort(reverse=True)



file = open(sys.argv[3], "w")
file.write("\n".join(str(o[0]) + ',' + o[1] for o in output))
file.close()



#print(labels)
#print(cycles)
#print(output)

