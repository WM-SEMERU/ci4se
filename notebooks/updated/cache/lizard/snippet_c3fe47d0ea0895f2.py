def transformByDistance(wV, subModel, alphabetSize=4):
    nc = [0.0] * alphabetSize
    for i in xrange(0, alphabetSize):
        j = wV[i]
        k = subModel[i]
        for l in xrange(0, alphabetSize):
            nc[l] += j * k[l]
    return nc