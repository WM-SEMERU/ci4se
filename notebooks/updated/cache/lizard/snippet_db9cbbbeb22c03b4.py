def adjustChildren(self, delta, secs=False):
    if self.adjustmentsBlocked('children'):
        return
    if self.itemStyle() != self.ItemStyle.Group:
        return
    if not delta:
        return
    for c in range(self.childCount()):
        child = self.child(c)
        child.blockAdjustments('range', True)
        if secs:
            dstart = child.dateTimeStart()
            dstart = dstart.addSecs(delta)
            child.setDateStart(dstart.date())
            child.setTimeStart(dstart.time())
        else:
            child.setDateStart(child.dateStart().addDays(delta))
        child.blockAdjustments('range', False)