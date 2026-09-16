def force(self, Ly=None):
    if self.calibration._c_drop:
        c_drop = self.calibration.c_drop(self.frequency)
    else:
        c_drop = self.capacitance()[-1] / self.area
    if self.calibration._c_filler:
        c_filler = self.calibration.c_filler(self.frequency)
    else:
        c_filler = 0
    if Ly is None:
        Ly = np.sqrt(self.area)
    return 1000.0 * Ly * 0.5 * (c_drop - c_filler) * self.V_actuation() ** 2