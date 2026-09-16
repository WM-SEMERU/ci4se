def rotateCoords(coords, R):
    newlist = list()
    for pp in coords:
        rpp = matrixTimesVector(R, pp)
        newlist.append(rpp)
    return newlist