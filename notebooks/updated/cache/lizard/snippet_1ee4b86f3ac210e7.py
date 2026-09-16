def getCandScoresMap(self, profile):
    elecType = profile.getElecType()
    if elecType != 'soc' and elecType != 'toc':
        print('ERROR: unsupported election type')
        exit()
    copelandScores = dict()
    for cand in profile.candMap.keys():
        copelandScores[cand] = 0.0
    preferenceCounts = profile.getPreferenceCounts()
    wmgMap = profile.getWmg()
    for cand1, cand2 in itertools.combinations(wmgMap.keys(), 2):
        if cand2 in wmgMap[cand1].keys():
            if wmgMap[cand1][cand2] > 0:
                copelandScores[cand1] += 1.0
            elif wmgMap[cand1][cand2] < 0:
                copelandScores[cand2] += 1.0
            else:
                copelandScores[cand1] += self.alpha
                copelandScores[cand2] += self.alpha
    return copelandScores