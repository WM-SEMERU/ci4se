def getPhysicalMinimum(self, chn=None):
    if chn is not None:
        if 0 <= chn < self.signals_in_file:
            return self.physical_min(chn)
        else:
            return 0
    else:
        physMin = np.zeros(self.signals_in_file)
        for i in np.arange(self.signals_in_file):
            physMin[i] = self.physical_min(i)
        return physMin