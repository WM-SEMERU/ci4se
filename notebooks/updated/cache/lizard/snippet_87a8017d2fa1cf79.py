def SAS(self):
    if self.x is None:
        self.x = np.arange(self.dx / 2.0, self.dx * self.qs.shape[0], self.dx)
    if self.filename:
        self.Te = self.configGet('float', 'input', 'ElasticThickness')
        self.qs = self.q0.copy()
        del self.q0
    if self.dimension == 2:
        if self.y is None:
            self.y = np.arange(self.dy / 2.0, self.dy * self.qs.shape[0],
                self.dy)
        try:
            self.qs
        except:
            self.qs = self.q0.copy()
            del self.q0
        from scipy.special import kei