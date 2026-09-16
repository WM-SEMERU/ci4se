def get_point_distance(point1, point2, metricParams, fUpper):
    aMass1 = point1[0]
    aMass2 = point1[1]
    aSpin1 = point1[2]
    aSpin2 = point1[3]
    bMass1 = point2[0]
    bMass2 = point2[1]
    bSpin1 = point2[2]
    bSpin2 = point2[3]
    aXis = get_cov_params(aMass1, aMass2, aSpin1, aSpin2, metricParams, fUpper)
    bXis = get_cov_params(bMass1, bMass2, bSpin1, bSpin2, metricParams, fUpper)
    dist = (aXis[0] - bXis[0]) ** 2
    for i in range(1, len(aXis)):
        dist += (aXis[i] - bXis[i]) ** 2
    return dist, aXis, bXis