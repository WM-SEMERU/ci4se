def pass_time(self):
    date = self.date
    nt = self._dimensions['cycle']
    N = self._dimensions['record']
    for t in np.arange(nt):
        poly = np.polyfit(np.arange(N)[~date.mask[(t), :]], date[(t), :][~
            date.mask[(t), :]], 1)
        date[(t), :][date.mask[(t), :]] = poly[0] * np.arange(N)[date.mask[
            (t), :]] + poly[1]
    date.mask = False
    return date[:, (N / 2)]