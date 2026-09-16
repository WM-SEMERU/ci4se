def cxx(self):
    return (np.cos(self.orientation) / self.semimajor_axis_sigma) ** 2 + (np
        .sin(self.orientation) / self.semiminor_axis_sigma) ** 2