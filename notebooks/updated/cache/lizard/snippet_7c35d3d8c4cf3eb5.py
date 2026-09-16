def SetDefault(self, name, value):
    fl = self.FlagDict()
    if name not in fl:
        self._SetUnknownFlag(name, value)
        return
    if self.IsParsed():
        logging.warn(
            'FLAGS.SetDefault called on flag "%s" after flag parsing. Call this method at the top level of a module to avoid overwriting the value passed at the command line.'
            , name)
    fl[name]._set_default(value)
    self._AssertValidators(fl[name].validators)