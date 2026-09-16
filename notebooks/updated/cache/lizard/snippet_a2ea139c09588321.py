def get_gadf(self):
    adam = np.abs(self.y - np.median(self.y)).sum()
    gadf = 1 - self.adcm / adam
    return gadf