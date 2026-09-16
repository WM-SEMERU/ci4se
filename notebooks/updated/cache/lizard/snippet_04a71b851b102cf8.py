def plot_pdf(self, names=None, Nbest=5, lw=2):
    assert Nbest > 0
    if Nbest > len(self.distributions):
        Nbest = len(self.distributions)
    if isinstance(names, list):
        for name in names:
            pylab.plot(self.x, self.fitted_pdf[name], lw=lw, label=name)
    elif names:
        pylab.plot(self.x, self.fitted_pdf[names], lw=lw, label=names)
    else:
        try:
            names = self.df_errors.sort_values(by='sumsquare_error').index[
                0:Nbest]
        except:
            names = self.df_errors.sort('sumsquare_error').index[0:Nbest]
        for name in names:
            if name in self.fitted_pdf.keys():
                pylab.plot(self.x, self.fitted_pdf[name], lw=lw, label=name)
            else:
                print('%s was not fitted. no parameters available' % name)
    pylab.grid(True)
    pylab.legend()