import csv
import vndb
import numpy

#users = List()

with open("data/votes2", "r", newline="") as data:

    print("Opened data")

    vns = dict()
    csvReader = csv.reader(data, delimiter=" ")
    for vote in csvReader:
        if not vote[0] in vns:
            vns[vote[0]] = 1
        else:
            vns[vote[0]] = vns[vote[0]]+1

    vnsPruned = list()

    for vn in vns:
        if vns[vn] > 100:
            vnsPruned.append(vn)

    print("Found %d suitable VNs" % len(vnsPruned))

    userVotes = dict()

    data.seek(0)
    for vote in csvReader:
        if not vote[0] in vnsPruned:
            continue
        
        if not vote[1] in userVotes:
            userVotes[vote[1]] = numpy.empty([len(vnsPruned)])
            userVotes[vote[1]].fill(numpy.nan)
    
        userVotes[vote[1]][vnsPruned.index(vote[0])] = numpy.float(vote[2])
        
    print("Processed %d users with at least one vote on suitable VNs" % len(userVotes))

    userVotesPruned = list()

    for user in userVotes:
        numVotes = 0
        for i in userVotes[user]:
            if not numpy.isnan(i):
                numVotes += 1
        if numVotes > 1:
            userVotesPruned.append(user)

    userVotes = None

    print("Pruned to %d users with at least two votes on suitable VNs" % len(userVotesPruned))

    for user in userVotesPruned:
        scoreStd = numpy.nanstd(user)
        scoreSum = numpy.nansum(user)
        scoreMean = numpy.nanmean(user)
        userNew = numpy.empty([len(vnsPruned)])
        userNew.fill(scoreMean)
        for i in user:
            if numpy.isnan(i):
                userNew

    # for user in userVotes:
    #     scoreSum = user.nansum()
    #     scoreStd = user.nanstd()

#vndb = vndb.VNDB("VN_Suggester", "0.1")

#print(vndb.get("user","basic","(id = 0)",""))

#with open("data/users", "w") as output: