def updateIgnoredEntry(self):
    dps = []
    for item, dp in self.wdplv.getItemDPList():
        if dp and not dp.archived:
            if dp.policy != 'banish':
                self.wdplv.setItemPolicy(item, 'ignore')
                dp.set_policy('ignore')
            dps.append(dp)
    return Purr.LogEntry(time.time(), dps=dps, ignore=True)