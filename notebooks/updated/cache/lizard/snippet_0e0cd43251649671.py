def getEarliness(self):
    maxtime = self.getMaxTimeAllowed()
    if not maxtime:
        return 0
    return api.to_minutes(**maxtime) - self.getDuration()