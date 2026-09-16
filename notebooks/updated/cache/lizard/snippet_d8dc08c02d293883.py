def getMonth(s):
    monthOrSeason = s.split('-')[0].upper()
    if monthOrSeason in monthDict:
        return monthDict[monthOrSeason]
    else:
        monthOrSeason = s.split('-')[1].upper()
        if monthOrSeason.isdigit():
            return monthOrSeason
        else:
            return monthDict[monthOrSeason]
    raise ValueError('Month format not recognized: ' + s)