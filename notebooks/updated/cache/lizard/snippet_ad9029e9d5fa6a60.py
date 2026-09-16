def computeStrongestPaths(self, profile, pairwisePreferences):
    cands = profile.candMap.keys()
    numCands = len(cands)
    strongestPaths = dict()
    for cand in cands:
        strongestPaths[cand] = dict()
    for i in range(1, numCands + 1):
        for j in range(1, numCands + 1):
            if i == j:
                continue
            if pairwisePreferences[i][j] > pairwisePreferences[j][i]:
                strongestPaths[i][j] = pairwisePreferences[i][j]
            else:
                strongestPaths[i][j] = 0
    for i in range(1, numCands + 1):
        for j in range(1, numCands + 1):
            if i == j:
                continue
            for k in range(1, numCands + 1):
                if i == k or j == k:
                    continue
                strongestPaths[j][k] = max(strongestPaths[j][k], min(
                    strongestPaths[j][i], strongestPaths[i][k]))
    return strongestPaths