def createRandomObjectDescriptions(numObjects, numLocationsPerObject,
    featurePool=('A', 'B', 'C')):
    return dict(('Object %d' % i, zip(xrange(numLocationsPerObject), [
        random.choice(featurePool) for _ in xrange(numLocationsPerObject)])
        ) for i in xrange(1, numObjects + 1))