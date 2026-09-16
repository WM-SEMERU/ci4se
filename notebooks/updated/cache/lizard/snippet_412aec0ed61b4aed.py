def update_rwalk(self, blob):
    self.scale = blob['scale']
    accept, reject = blob['accept'], blob['reject']
    facc = 1.0 * accept / (accept + reject)
    norm = max(self.facc, 1.0 - self.facc) * self.npdim
    self.scale *= math.exp((facc - self.facc) / norm)
    self.scale = min(self.scale, math.sqrt(self.npdim))