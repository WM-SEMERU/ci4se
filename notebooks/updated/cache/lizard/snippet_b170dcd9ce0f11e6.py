def printDuplicatedTPEDandTFAM(tped, tfam, samples, oldSamples, prefix):
    outputTPED = None
    try:
        outputTPED = open(prefix + '.duplicated_samples.tped', 'w')
    except IOError:
        msg = "%(prefix)s.duplicated_samples.tped: can't write file" % locals()
        raise ProgramError(msg)
    for row in tped:
        print >> outputTPED, '\t'.join(row)
    outputTPED.close()
    nbSamples = len(tped[0][4:])
    newTFAM = [(0) for i in xrange(nbSamples)]
    for samples, indexes in samples.iteritems():
        oldIndexes = oldSamples[samples]
        for i, index in enumerate(indexes):
            oldIndex = oldIndexes[i]
            newTFAM[index] = tfam[oldIndex]
    outputTFAM = None
    try:
        outputTFAM = open(prefix + '.duplicated_samples.tfam', 'w')
    except IOError:
        msg = "%(prefix)s.duplicated_samples.tfam: can't write file" % locals()
        raise ProgramError(msg)
    for row in newTFAM:
        print >> outputTFAM, '\t'.join(row)
    outputTFAM.close()