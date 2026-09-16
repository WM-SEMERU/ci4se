def getRankingBruteForce(self, profile):
    candScoresMapBruteForce = self.getCandScoresMapBruteForce(profile)
    reverseCandScoresMap = dict()
    for key, value in candScoresMapBruteForce.items():
        if value not in reverseCandScoresMap.keys():
            reverseCandScoresMap[value] = [key]
        else:
            reverseCandScoresMap[value].append(key)
    if self.maximizeCandScore == True:
        sortedCandScores = sorted(reverseCandScoresMap.keys(), reverse=True)
    else:
        sortedCandScores = sorted(reverseCandScoresMap.keys())
    ranking = []
    for candScore in sortedCandScores:
        for cand in reverseCandScoresMap[candScore]:
            ranking.append(cand)
    return ranking