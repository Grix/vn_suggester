import csv
import numpy

#users = List()

with open("data/votes2", "r", newline="") as data:

    print("Opened data")

    vns = dict()
    csvreader = csv.reader(data, delimiter=" ")
    for vote in csvreader:
        if not vote[0] in vns:
            vns[vote[0]] = 1
        else:
            vns[vote[0]] = vns[vote[0]]+1

    vns_pruned = list()

    for vn in vns:
        if vns[vn] > 100:
            vns_pruned.append(vn)

    print("Found %d suitable VNs" % len(vns_pruned))

#with open("data/users", "w") as output: