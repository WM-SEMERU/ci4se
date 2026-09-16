def timescale_sensitivity(T, k):
    eValues, rightEigenvectors = numpy.linalg.eig(T)
    leftEigenvectors = numpy.linalg.inv(rightEigenvectors)
    perm = numpy.argsort(eValues)[::-1]
    eValues = eValues[perm]
    rightEigenvectors = rightEigenvectors[:, (perm)]
    leftEigenvectors = leftEigenvectors[perm]
    eVal = eValues[k]
    sensitivity = numpy.outer(leftEigenvectors[k], rightEigenvectors[:, (k)])
    if eVal < 1.0:
        factor = 1.0 / numpy.log(eVal) ** 2 / eVal
    else:
        factor = 0.0
    sensitivity *= factor
    return sensitivity