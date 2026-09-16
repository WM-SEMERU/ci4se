def save(self, X=None, w=None, A=None):
    self.X.append(X)
    self.wgt.append(w)
    self.A.append(A)