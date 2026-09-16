def force_to_voltage(self, force, frequency):
    c_drop = self.calibration.c_drop(frequency)
    if self.calibration._c_filler:
        c_filler = self.calibration.c_filler(frequency)
    else:
        c_filler = 0
    return np.sqrt(force * 1e-09 / (0.5 * (c_drop - c_filler)))