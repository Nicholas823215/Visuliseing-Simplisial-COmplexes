from Simplitial_Complises import *
import sys
import time

try:
    arg1 = sys.argv[1]
    if arg1[0].lower() == "t":
        debug = True
    else:
        debug = False
except:
    debug = False
file1 = open("triangluatin.txt","r")

lines = []

line1 = file1.readline()
while line1[0] == "#":
    line1 = file1.readline()

line1 = line1.split(",")
line1[-1] = line1[-1][:-1]
for i in line1:
    lines.append([i])

file1.readline()
line1 = file1.readline()


while line1 != "":
    if debug:
        print(line1)
    while line1[0] == "#":
        line1 = file1.readline()
    line1 = line1.strip(" ")
    line1 = line1[1:-2]
    line1 = line1.split(",")
    lines.append(line1)
    line1 = file1.readline()
Simplex = []
for i in lines:
    if debug:
        print(i)
    Simplex.append(Set(i))

SimC = SC(Simplex)
if debug:
    print(SimC)

time1 = time.perf_counter()
SimC.findNoOfCrit_Meth1()
time2 = time.perf_counter()

if __name__ == "__main__":
    print("The Simplitial complex with simplisies of",SimC,f"\nTook {time2-time1} seconds to calculate\nAnd found a Morse Function with {SimC.No_crit_Meth1} critical simplisies" )
