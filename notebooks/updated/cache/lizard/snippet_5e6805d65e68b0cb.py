def calcValueAtBirth(cLvlHist, BirthBool, PlvlHist, MrkvHist, DiscFac, CRRA):
    J = np.max(MrkvHist) + 1
    T = MrkvHist.size
    I = cLvlHist.shape[1]
    u = lambda c: CRRAutility(c, gam=CRRA)
    BirthsByPeriod = np.sum(BirthBool, axis=1)
    BirthsByState = np.zeros(J, dtype=int)
    for j in range(J):
        these = MrkvHist == j
        BirthsByState[j] = np.sum(BirthsByPeriod[these])
    N = np.max(BirthsByState)
    vArray = np.zeros((J, N)) + np.nan
    n = np.zeros(J, dtype=int)
    DiscVec = DiscFac ** np.arange(T)
    for i in range(I):
        birth_t = np.where(BirthBool[:, (i)])[0]
        for k in range(birth_t.size - 1):
            t0 = birth_t[k]
            t1 = birth_t[k + 1]
            span = t1 - t0
            j = MrkvHist[t0]
            cVec = cLvlHist[t0:t1, (i)] / PlvlHist[t0]
            uVec = u(cVec)
            v = np.dot(DiscVec[:span], uVec)
            vArray[j, n[j]] = v
            n[j] += 1
    vAtBirth = np.nanmean(vArray, axis=1)
    return vAtBirth