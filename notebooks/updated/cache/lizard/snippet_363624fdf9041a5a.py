def chooseCellsToLearnFrom(self, c, i, s, n, timeStep):
    if n <= 0:
        return []
    tmpCandidates = []
    if timeStep == 't-1':
        tmpCandidates = numpy.where(self.learnState['t-1'] == 1)
    else:
        tmpCandidates = numpy.where(self.learnState['t'] == 1)
    if len(tmpCandidates[0]) == 0:
        return []
    if s is None:
        cands = [syn for syn in zip(tmpCandidates[0], tmpCandidates[1])]
    else:
        synapsesAlreadyInSegment = set((syn[0], syn[1]) for syn in s.syns)
        cands = [syn for syn in zip(tmpCandidates[0], tmpCandidates[1]) if 
            (syn[0], syn[1]) not in synapsesAlreadyInSegment]
    if n == 1:
        idx = self._random.getUInt32(len(cands))
        return [cands[idx]]
    self._random.getUInt32(10)
    indices = array([j for j in range(len(cands))], dtype='uint32')
    tmp = zeros(min(n, len(indices)), dtype='uint32')
    self._random.getUInt32Sample(indices, tmp, True)
    return [cands[j] for j in tmp]