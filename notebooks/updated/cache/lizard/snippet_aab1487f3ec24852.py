def setup(self, **kwargs):
    clobber = self.clobber
    self.clobber = False
    if not self.load_model('nPLD'):
        raise Exception("Can't find `nPLD` model for target.")
    self.clobber = clobber
    self.piter = kwargs.get('piter', 3)
    self.pmaxf = kwargs.get('pmaxf', 300)
    self.ppert = kwargs.get('ppert', 0.1)