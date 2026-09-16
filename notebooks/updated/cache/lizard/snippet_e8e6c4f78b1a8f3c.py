def predict_is(self, h=5, fit_once=True):
    predictions = []
    for t in range(0, h):
        x = NLLEV(family=self.family, integ=self.integ, data=self.
            data_original[:-h + t])
        x.fit(print_progress=False)
        if t == 0:
            predictions = x.predict(h=1)
        else:
            predictions = pd.concat([predictions, x.predict(h=1)])
    predictions.rename(columns={(0): self.data_name}, inplace=True)
    predictions.index = self.index[-h:]
    return predictions