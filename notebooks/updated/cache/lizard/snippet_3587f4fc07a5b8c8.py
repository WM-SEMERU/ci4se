def to_capabilities(self):
    caps = self._caps
    opts = self._options.copy()
    if len(self._arguments) > 0:
        opts[self.SWITCHES] = ' '.join(self._arguments)
    if len(self._additional) > 0:
        opts.update(self._additional)
    if len(opts) > 0:
        caps[Options.KEY] = opts
    return caps