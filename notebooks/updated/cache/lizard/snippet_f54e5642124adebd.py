def GetBestMatch(target, matchList):
    bestMatchList = []
    if len(matchList) > 0:
        ratioMatch = []
        for item in matchList:
            ratioMatch.append(GetBestStringMatchValue(target, item))
        maxRatio = max(ratioMatch)
        if maxRatio > 0.8:
            matchIndexList = [i for i, j in enumerate(ratioMatch) if j ==
                maxRatio]
            for index in matchIndexList:
                if maxRatio == 1 and len(matchList[index]) == len(target):
                    return [matchList[index]]
                else:
                    bestMatchList.append(matchList[index])
    return bestMatchList