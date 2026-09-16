def print_fit_parameters(self):
    s = ''
    if self.results and self.results[1] is not None:
        s = s + '\n# FIT RESULTS (reduced chi squared = {:s})\n'.format(str
            (self.reduced_chi_squareds()))
        for n in range(len(self._pnames)):
            s = s + '{:10s} = {:G}\n'.format(self._pnames[n], self.results[
                0][n])
    elif self.results and self.results[1] is None:
        s = s + '\n# FIT DID NOT CONVERGE\n'
        for n in range(len(self._pnames)):
            s = s + '{:10s} = {:G}\n'.format(self._pnames[n], self.results[
                0][n])
    else:
        s = s + '\n# NO FIT RESULTS\n'
    print(s)