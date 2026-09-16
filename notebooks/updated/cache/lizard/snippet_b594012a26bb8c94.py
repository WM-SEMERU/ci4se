def get_mfd(self, slip, fault_width, shear_modulus=30.0, disp_length_ratio=
    1.25e-05):
    beta = np.sqrt(disp_length_ratio * 10.0 ** C_VALUE / (shear_modulus * 
        10000000000.0 * (fault_width * 100000.0)))
    dbar = D_VALUE * np.log(10.0)
    bbar = self.b_value * np.log(10.0)
    mag = np.arange(self.mmin - self.bin_width / 2.0, self.mmax + self.
        bin_width, self.bin_width)
    if bbar > dbar:
        print(
            'b-value larger than 1.5 will produce invalid results in Anderson & Luco models'
            )
        self.occurrence_rate = np.nan * np.ones(len(mag) - 1)
        return self.mmin, self.bin_width, self.occurrence_rate
    self.occurrence_rate = np.zeros(len(mag) - 1, dtype=float)
    for ival in range(0, len(mag) - 1):
        self.occurrence_rate[ival] = RECURRENCE_MAP[self.mfd_type
            ].cumulative_value(slip, self.mmax, mag[ival], bbar, dbar, beta
            ) - RECURRENCE_MAP[self.mfd_type].cumulative_value(slip, self.
            mmax, mag[ival + 1], bbar, dbar, beta)
        if self.occurrence_rate[ival] < 0.0:
            self.occurrence_rate[ival] = 0.0
    return self.mmin, self.bin_width, self.occurrence_rate