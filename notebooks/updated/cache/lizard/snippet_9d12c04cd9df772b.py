def RWSelection(self, mating_pool_size):
    A = numpy.zeros(self.length)
    mating_pool = numpy.zeros(mating_pool_size)
    [F, S, P] = self.rankingEval()
    P_Sorted = numpy.zeros(self.length)
    for i in range(self.length):
        P_Sorted[i] = P[S[i]]
    for i in range(self.length):
        A[i] = P_Sorted[0:i + 1].sum()
    i = 0
    j = 0
    while j < mating_pool_size:
        r = numpy.random.random()
        i = 0
        while A[i] < r:
            i += 1
        if numpy.shape(numpy.where(mating_pool == i))[1] == 0:
            mating_pool[j] = S[i]
            j += 1
    return mating_pool