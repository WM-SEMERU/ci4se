def predict(self, X, batch_size=1, show_progressbar=False):
    dist = self.transform(X, batch_size, show_progressbar)
    res = dist.__getattribute__(self.argfunc)(1)
    return res