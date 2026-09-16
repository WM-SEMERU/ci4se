def getFixedStarList(IDs, date):
    starList = [getFixedStar(ID, date) for ID in IDs]
    return FixedStarList(starList)