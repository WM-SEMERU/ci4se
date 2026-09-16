def _fixup_val(self, x):
    if isinstance(x, (list, tuple)):
        return type(x)(v if v is None or isinstance(v, FlagValue) else
            FlagValue(v, self.names) for v in x)
    return x if x is None or isinstance(x, FlagValue) else FlagValue(x,
        self.names)