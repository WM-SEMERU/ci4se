def get_null_snr(self):
    null_snr_sq = (numpy.asarray(self.get_sngl_snrs().values()) ** 2).sum(
        ) - self.snr ** 2
    if null_snr_sq < 0:
        return 0
    else:
        return null_snr_sq ** (1.0 / 2.0)