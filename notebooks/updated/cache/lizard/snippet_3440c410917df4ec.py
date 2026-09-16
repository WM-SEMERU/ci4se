def _GetShowInfo(self, stringSearch):
    goodlogging.Log.Info('RENAMER', 'Looking up show info for: {0}'.format(
        stringSearch))
    goodlogging.Log.IncreaseIndent()
    showInfo = self._GetShowID(stringSearch)
    if showInfo is None:
        goodlogging.Log.DecreaseIndent()
        return None
    elif showInfo.showID is None:
        goodlogging.Log.DecreaseIndent()
        return None
    elif showInfo.showName is None:
        showInfo.showName = self._db.SearchTVLibrary(showID=showInfo.showID)[0
            ][1]
        goodlogging.Log.Info('RENAMER', 'Found show name: {0}'.format(
            showInfo.showName))
        goodlogging.Log.DecreaseIndent()
        return showInfo
    else:
        goodlogging.Log.DecreaseIndent()
        return showInfo