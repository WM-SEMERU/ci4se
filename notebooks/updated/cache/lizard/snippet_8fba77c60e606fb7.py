def do_rmfit(self, arg):
    if arg in self.curargs['fits']:
        del self.curargs['fits'][arg]
    if 'timing' in arg:
        fitvar = '{}|fit'.format(arg)
    else:
        fitvar = '{}.fit'.format(arg)
    if fitvar in self.curargs['dependents']:
        self.curargs['dependents'].remove(fitvar)