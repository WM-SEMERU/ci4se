def getcoef(self):
    global mp_Z_Y1
    return np.swapaxes(mp_Z_Y1, 0, self.xstep.cri.axisK + 1)[0]