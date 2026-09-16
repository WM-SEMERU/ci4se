def crpss(self):
    crps_f = self.crps()
    crps_c = self.crps_climo()
    return 1.0 - float(crps_f) / float(crps_c)